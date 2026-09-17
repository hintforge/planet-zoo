# -*- coding: utf-8 -*-
"""Rebuild zoo_planner.html from the Planet Zoo corpus.

Run this after the corpus changes:

    python build.py

It re-extracts species and scenario data from ../animals/ and ../sections/,
then swaps that data into the two JSON islands inside zoo_planner.html.
The page's markup, styling and logic are left untouched -- only the contents
of the <script type="application/json"> blocks are replaced.
"""
import io
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.join(HERE, "zoo_planner.html")
DATA = os.path.join(HERE, "data")

ISLANDS = [
    ("species-data", os.path.join(DATA, "species.json")),
    ("scenario-data", os.path.join(DATA, "scenarios.json")),
]


def run(script):
    """Run an extractor and fail loudly if it does not succeed."""
    path = os.path.join(HERE, script)
    result = subprocess.call([sys.executable, path])
    if result != 0:
        sys.exit("%s failed with exit code %d" % (script, result))


def embed(html, island_id, payload):
    """Replace one JSON island's contents, leaving the rest of the page alone."""
    pattern = re.compile(
        r'(<script id="%s" type="application/json">)(.*?)(</script>)' % island_id,
        re.S,
    )
    if not pattern.search(html):
        sys.exit("island '%s' not found in zoo_planner.html" % island_id)
    # A literal "</" inside a script block would close it early.
    safe = payload.replace("</", "<\\/")
    return pattern.sub(lambda m: m.group(1) + safe + m.group(3), html, count=1)


def main():
    run("extract.py")
    run("extract_scenarios.py")

    html = io.open(PAGE, encoding="utf-8").read()
    for island_id, source in ISLANDS:
        records = json.load(io.open(source, encoding="utf-8"))
        compact = json.dumps(records, ensure_ascii=False, separators=(",", ":"))
        html = embed(html, island_id, compact)
        print("embedded %d records into %s" % (len(records), island_id))

    io.open(PAGE, "w", encoding="utf-8", newline="\n").write(html)
    print("wrote %s (%.0f KB)" % (PAGE, len(html.encode("utf-8")) / 1024.0))


if __name__ == "__main__":
    main()
