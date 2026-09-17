# -*- coding: utf-8 -*-
"""Extract Career scenario presets from the Planet Zoo corpus."""
import io, re, json, os

import os as _os
_HERE = _os.path.dirname(_os.path.abspath(__file__))
_CORPUS = _os.path.dirname(_HERE)   # artifacts/ -> corpus root
BASE = _os.path.join(_CORPUS, "sections") + "/"
OUT = _os.path.join(_HERE, "data", "scenarios.json")

ORDER = [
    u"stately_home_schooling", u"the_aperenticeship", u"bear_essentials",
    u"eye_of_the_taiga", u"go_to_crater_lengths", u"squeezing_the_margins",
    u"power_struggle", u"steeped_in_pollution", u"hiring_freeze",
    u"greener_pastures", u"bailing_out", u"the_last_leg",
]

out = []
for i, slug in enumerate(ORDER, 1):
    path = BASE + slug + u".md"
    if not os.path.exists(path):
        continue
    txt = io.open(path, encoding="utf-8").read()

    name = None
    m = re.search(r"^# Career Scenario \d+ -- (.+?)\s*$", txt, re.M)
    if m:
        name = m.group(1)

    loc = None
    m = re.search(r"## Location / Theme\s*\n+(.+?)(?:\n\n|\n_source)", txt, re.S)
    if m:
        loc = re.sub(r"\s+", u" ", m.group(1)).strip()

    objs = {}
    m = re.search(r"## Objectives\s*\n+(.*?)(?=\n## )", txt, re.S)
    body = m.group(1) if m else u""
    for tier in (u"Bronze", u"Silver", u"Gold"):
        mm = re.search(r"\*\*" + tier + r":\*\*\s*(.+?)(?:\n|$)", body)
        if mm:
            objs[tier.lower()] = re.sub(r"\s+", u" ", mm.group(1)).strip()
    recovered = bool(objs)
    note = None
    if not recovered:
        mm = re.search(r"(not recovered[^.]*\.)", body)
        note = mm.group(1).strip() if mm else u"Objectives not recovered from a working source."

    miss = None
    m = re.search(r"## Missability\s*\n+(.+?)(?:\n\n|\n## |\n_source)", txt, re.S)
    if m:
        miss = re.sub(r"\s+", u" ", m.group(1)).strip()

    out.append({
        u"n": i, u"slug": slug, u"name": name or slug, u"location": loc,
        u"objectives": objs, u"objectives_recovered": recovered,
        u"objectives_note": note, u"missability": miss,
    })

io.open(OUT, "w", encoding="utf-8", newline="\n").write(
    json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True))
print(u"scenarios: %d (with objectives: %d)"
      % (len(out), sum(1 for s in out if s[u"objectives_recovered"])))
