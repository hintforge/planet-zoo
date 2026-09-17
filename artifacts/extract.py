# -*- coding: utf-8 -*-
"""Extract structured species data from the Planet Zoo corpus into JSON."""
import io, os, re, json, glob

import os as _os
_HERE = _os.path.dirname(_os.path.abspath(__file__))
_CORPUS = _os.path.dirname(_HERE)   # artifacts/ -> corpus root
BASE = _os.path.join(_CORPUS, "animals") + "/"
OUT = _os.path.join(_HERE, "data", "species.json")

NUM = r"([0-9][0-9,]*(?:\.[0-9]+)?)"


def n(s):
    try:
        return float(s.replace(u",", u""))
    except Exception:
        return None


def field(txt, *labels):
    """Return the raw value of the first matching '- **Label:** value' line."""
    for lab in labels:
        m = re.search(r"^- \*\*" + re.escape(lab) + r":\*\*\s*(.+?)\s*$", txt, re.M)
        if m:
            return m.group(1)
    return None


def first_area(s):
    """First square-metre figure in a string."""
    if not s:
        return None
    m = re.search(NUM + r"\s*m", s)
    return n(m.group(1)) if m else None


def all_areas(s):
    if not s:
        return []
    return [n(x) for x in re.findall(NUM + r"\s*m", s)]


def parse_land(txt):
    """Returns (base, per_adult, family_total, label_used)."""
    combos = [
        u"Land min / +per adult",
        u"Land min (individual / family)",
        u"Land (individual / family)",
        u"Land +per adult (per-CC scaling)",
        u"Land base +per adult (per-CC scaling)",
        u"Land base +per climb-area",
        u"Land / habitat size",
        u"Land",
        u"Total habitat (land+water)",
        u"Enclosure min (individual / group)",
    ]
    for lab in combos:
        v = field(txt, lab)
        if v is None:
            continue
        areas = all_areas(v)
        if not areas:
            continue
        base = areas[0]
        per = areas[1] if len(areas) > 1 else None
        fam = None
        if u"individual / family" in lab or u"individual / group" in lab:
            fam, per = per, None
        ft = field(txt, u"Family total")
        if ft:
            fam = first_area(ft)
        return base, per, fam, lab
    return None, None, None, None


def parse_temp(txt):
    v = field(txt, u"Temperature range", u"Temperature / Humidity")
    if not v:
        return None, None
    unit = u"(?:degC|°C|C\b)"
    m = re.search(r"(-?[0-9]+(?:\.[0-9]+)?)\s*(?:-|to)\s*(-?[0-9]+(?:\.[0-9]+)?)\s*" + unit, v)
    if m:
        return float(m.group(1)), float(m.group(2))
    return None, None


def parse_group(v):
    """Group size min/max from the social field."""
    if not v:
        return None, None
    m = re.search(r"\b([0-9]+)\s*-\s*([0-9]+)\b", v)
    if m:
        return int(m.group(1)), int(m.group(2))
    m = re.search(r"[Uu]p to ([0-9]+)", v)
    if m:
        return 1, int(m.group(1))
    return None, None


def parse_sex_ratio(v):
    """Male/female caps expressed several ways in the social field."""
    if not v:
        return None, None
    pats = [
        r"([0-9]+)\s*males?\s*/\s*([0-9]+)\s*females?",
        r"\(?\s*(?:up to\s*)?([0-9]+)\s*M\s*,\s*(?:up to\s*)?([0-9]+)\s*F\s*\)?",
        r"([0-9]+)\s*male\s*/\s*([0-9]+)\s*females?\s*max",
    ]
    for p in pats:
        m = re.search(p, v, re.I)
        if m:
            return int(m.group(1)), int(m.group(2))
    m = re.search(r"([0-9]+)\s*-\s*([0-9]+)\s*females?\s*/\s*([0-9]+)\s*-\s*([0-9]+)\s*males?", v, re.I)
    if m:
        return int(m.group(4)), int(m.group(2))
    return None, None


def parse_terrain(txt):
    v = field(txt, u"Terrain composition", u"Terrain")
    if not v:
        return None
    out = {}
    for kind, lo, hi in re.findall(r"([a-z]+)\s+([0-9]+)\s*-\s*([0-9]+)%", v):
        out[kind] = [int(lo), int(hi)]
    for kind, only in re.findall(r"([a-z]+)\s+([0-9]+)%", v):
        if kind not in out:
            out[kind] = [int(only), int(only)]
    return out or None


def split_list(v):
    if not v:
        return []
    v = re.sub(r"\[.*?\]", u"", v)
    parts = re.split(r",|/|;", v)
    out = []
    for p in parts:
        p = p.strip().strip(u'"').strip()
        p = re.sub(r"\s*\(.*?\)\s*", u" ", p).strip()
        if p and len(p) < 60 and not p.lower().startswith(u"not "):
            out.append(p)
    return out



CONTINENTS = [u"North America", u"South America", u"Africa", u"Asia", u"Europe",
              u"Oceania", u"Antarctica"]
BIOMES = [u"Aquatic", u"Desert", u"Grassland", u"Taiga", u"Temperate", u"Tropical",
          u"Tundra"]
IUCN = [u"Critically Endangered", u"Endangered", u"Extinct in the Wild",
        u"Near Threatened", u"Least Concern", u"Vulnerable", u"Data Deficient",
        u"Domesticated"]


def norm_continents(raw):
    """A species may legitimately span continents; keep every canonical hit."""
    if not raw:
        return []
    hits = [c for c in CONTINENTS if c.lower() in raw.lower()]
    if u"North America" in hits and u"South America" in hits:
        pass
    if not hits and u"america" in raw.lower():
        hits = [u"North America"]
    return hits


def norm_biomes(raws):
    out = []
    for r in raws or []:
        for b in BIOMES:
            if b.lower() in r.lower() and b not in out:
                out.append(b)
    return out


def norm_iucn(raw):
    if not raw:
        return None
    low = raw.lower()
    for cat in IUCN:
        if cat.lower() in low:
            return cat
    return None


records = []
for path in sorted(glob.glob(BASE + u"*.md")):
    slug = os.path.basename(path)[:-3]
    if slug == u"index":
        continue
    with io.open(path, encoding="utf-8") as f:
        txt = f.read()

    name = None
    m = re.search(r"^# Animals -- (.+?)\s*$", txt, re.M)
    if m:
        name = m.group(1)

    hdr = u""
    m = re.search(r"^\*\*(?:Latin|Continent).*$", txt, re.M)
    if m:
        hdr = m.group(0)

    def hdr_field(label):
        mm = re.search(re.escape(label) + r":\*\*\s*([^|]+)", hdr)
        return mm.group(1).strip() if mm else None

    latin = None
    mm = re.search(r"\*\*Latin:\*\*\s*\*(.+?)\*", hdr)
    if mm:
        latin = mm.group(1)

    continent = hdr_field(u"**Continent") or hdr_field(u"**Continent (real-world range)")
    iucn = None
    iucn_ingame = False
    for lab in [u"**IUCN (in-game)", u"**IUCN status", u"**IUCN (real-world, per source)",
                u"**IUCN (real-world)", u"**IUCN (real)", u"**Real IUCN status", u"**IUCN"]:
        iucn = hdr_field(lab)
        if iucn:
            iucn_ingame = (u"in-game" in lab)
            break
    if iucn:
        iucn = re.split(r"\s+--\s+", iucn)[0].strip()
    housing = hdr_field(u"**Housing type")

    dlc = None
    mm = re.search(r"spoiler:\s*dlc:([^_\n]+?)\s*_", txt)
    if mm:
        dlc = mm.group(1).strip()

    conf = None
    mm = re.search(r"confidence:\s*([a-z]+)", txt)
    if mm:
        conf = mm.group(1)

    # Guest tolerance -- the game's relationship-with-humans stat. NOTE: kept
    # under its own key. `confidence` above is SOURCE confidence, a different
    # thing entirely; do not merge them.
    guest = None
    guest_note = field(txt, u"Guest tolerance")
    if guest_note:
        # Drop the trailing `[source date]` marker -- it is corpus provenance,
        # and the artifact renders this string as prose. Leaving it in printed
        # the backticks literally on the page.
        guest_note = re.sub(r"\s*`\[[^\]]*\]`\s*$", u"", guest_note).strip()
        mm = re.match(r"(Shy|Neutral|Confident)\b", guest_note)
        if mm:
            guest = mm.group(1)

    gap = u"## Gap flag" in txt or u"Gap flag --" in txt

    land, per_adult, fam, land_label = parse_land(txt)
    land_raw = field(txt, *[u"Land min / +per adult", u"Land min (individual / family)",
                            u"Land (individual / family)", u"Land +per adult (per-CC scaling)",
                            u"Land base +per adult (per-CC scaling)", u"Land base +per climb-area",
                            u"Land / habitat size", u"Land", u"Total habitat (land+water)",
                            u"Enclosure min (individual / group)"])
    temp_raw = field(txt, u"Temperature range", u"Temperature / Humidity")
    water = first_area(field(txt, u"Water min", u"Water"))
    climb = first_area(field(txt, u"Climb min", u"Climb"))
    tmin, tmax = parse_temp(txt)
    social = field(txt, u"Social type / group", u"Group size", u"Group size / cap",
                   u"Natural social structure")
    gmin, gmax = parse_group(social)
    smale, sfemale = parse_sex_ratio(social)
    if smale is None:
        mm = re.search(r"\*\*Sex-ratio cap:\*\*\s*([0-9]+)\s*males?\s*:\s*([0-9]+)\s*females?", txt, re.I)
        if mm:
            smale, sfemale = int(mm.group(1)), int(mm.group(2))
    biomes = split_list(field(txt, u"Biome(s)", u"Biome"))
    mixing_raw = field(txt, u"Mixing compatibility")
    mixing = [] if (mixing_raw and mixing_raw.lower().startswith(u"none")) else split_list(mixing_raw)
    diet = field(txt, u"Diet", u"Diet/enrichment", u"Real diet")
    enrich = field(txt, u"Enrichment sample")
    terrain = parse_terrain(txt)

    gotcha = None
    mm = re.search(r"## Welfare gotcha\s*\n+(.+?)(?:\n\n|\n_source)", txt, re.S)
    if mm:
        gotcha = re.sub(r"\s+", u" ", mm.group(1)).strip()

    htype = u"Exhibit" if (housing and u"Exhibit" in housing) else u"Habitat"
    walkabout = bool(housing and u"Walkabout" in housing)
    walkthrough = bool(housing and u"Walkthrough" in housing)

    records.append({
        u"slug": slug,
        u"name": name or slug.replace(u"_", u" ").title(),
        u"latin": latin,
        u"continent": continent,
        u"continents": norm_continents(continent),
        u"iucn": iucn,
        u"iucn_cat": norm_iucn(iucn),
        u"iucn_ingame": iucn_ingame,
        u"housing": htype,
        u"housing_raw": housing,
        u"walkabout": walkabout,
        u"walkthrough": walkthrough,
        u"dlc": dlc,
        u"confidence": conf,
        u"guest_confidence": guest,
        u"guest_note": guest_note,
        u"gap": gap,
        u"land": land,
        u"land_per_adult": per_adult,
        u"land_family": fam,
        u"land_label": land_label,
        u"land_raw": land_raw,
        u"temp_raw": temp_raw,
        u"water": water,
        u"climb": climb,
        u"temp_min": tmin,
        u"temp_max": tmax,
        u"social": social,
        u"group_min": gmin,
        u"group_max": gmax,
        u"males_max": smale,
        u"females_max": sfemale,
        u"biomes": norm_biomes(biomes),
        u"biomes_raw": biomes,
        u"mixing": mixing,
        u"diet": diet,
        u"enrichment": enrich,
        u"terrain": terrain,
        u"gotcha": gotcha,
    })

with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write(json.dumps(records, ensure_ascii=False, indent=1, sort_keys=True))

tot = len(records)


def cov(key):
    c = sum(1 for r in records if r.get(key) not in (None, [], u""))
    return u"%3d/%d  %s" % (c, tot, key)


print(u"species: %d" % tot)
for k in [u"latin", u"continent", u"iucn", u"housing_raw", u"dlc", u"land",
          u"land_per_adult", u"water", u"climb", u"temp_min", u"social",
          u"group_max", u"males_max", u"biomes", u"mixing", u"diet",
          u"terrain", u"gotcha", u"guest_confidence"]:
    print(cov(k))
print(u"gap-flagged: %d" % sum(1 for r in records if r[u"gap"]))
print(u"exhibits: %d  habitats: %d" % (
    sum(1 for r in records if r[u"housing"] == u"Exhibit"),
    sum(1 for r in records if r[u"housing"] == u"Habitat")))
