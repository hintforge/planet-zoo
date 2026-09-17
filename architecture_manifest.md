# Planet Zoo -- Architecture manifest

**status:** research-integrated <!-- scaffold | research-integrated | live-observed | reconciled -->
**last_reconciled:** 2026-08-22
**research_run:** P1 (base game, 2026-08-21)

This game is `narrative-no-nav` (a construction-and-management sim), so there is no `nav/` folder and no zone graph -- the player authors their own space; there is nothing to route. This file therefore carries only the **Hintforge manifest** (the machine-readable core the reader discovers at session start) and the **Vector extensions** list. The zone-graph / locks-and-keys structures that a nav-bearing game would put in `nav/architecture.md` are intentionally absent.

## Hintforge manifest

<!-- Read by the reader at session start (see docs/corpus-format.md §3). game-version-* fields describe the game build the corpus was authored against (player-supplied at setup); orthogonal to corpus-core-version (the schema axis). -->

```
corpus-core-version: 6
game-version: "1.20.2"
game-version-platform: "PC / Steam"
game-version-as-of: 2026-09-17
vector-extensions: [animals]
```

## Vector extensions

<!-- One entry per extension folder created at setup. Reader uses this list to route topical questions to the right folder. -->

- `animals/` -- **corpus-declared extension** (not one of the six canonical extensions). Species bestiary: one file per Planet Zoo species with its welfare requirements (habitat size, terrain/climate, social group, enrichment, biome, diet), conservation status, and Zoopedia-grade facts. This is the dominant reference surface for a zoo sim -- the analogue of `items/` in a combat game. Indexed by `animals/index.md`. Per-species files are created at P1 ingestion from the roster; animal facts route here (tag `vector: item` in research, destination `animals/<species>.md`).

## Structural notes (nav-bearing structures -- N/A for this game)

- **Zone graph:** N/A -- `narrative-no-nav`. No navigable zones, no points of no return, no locks-and-keys.
- **Localization-mechanism class:** `none` -- the player builds their own zoo; there are no in-world landmarks to resolve player position against. The `player_position` block is omitted from `CHECKPOINT.md` accordingly.
- **Career scenarios** are self-contained builds with objectives, not navigable zones. Their walkthrough notes live in `sections/`, not in a zone graph.
- **Source-language set:** English (dev: Frontier Developments, UK) + German, French, Russian, Simplified Chinese, Spanish (top player-region languages -- drives the non-English source floor at research time).
