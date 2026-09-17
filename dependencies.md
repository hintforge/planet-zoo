# Dependencies -- Planet Zoo
<!-- hintforge · stitch pass · last run: 2026-08-22 -->
<!-- Every stitch run re-audits ALL existing edges + adds new ones. The per-edge convergence audit (open each cited source, verify the specific value) applies to every row in this file on every run, not just new candidates. A game patch, DLC, or new ingestion phase can change facts that existing edges cite -- only a full re-audit catches that. See `stitch_and_zipper.md` Phase B "Re-run scope: always full." Inconsistencies (cited source contradicts edge text) land in the `## Corpus inconsistencies` section; the edge row stays in place. -->

## Cross-system edges

| Edge ID | System A | System B | Dependency description | Confidence | Source files |
|---------|----------|----------|------------------------|------------|--------------|
| DEP-001 | Animal Welfare (Social pillar) | Species-specific maturation typing | Western Lowland Gorilla is tagged **solitary** maturation-type despite living in structured family troops, an outlier vs. its own family's usual grouping rules; cited as the practical example of the enrichment-demand ceiling. | high | mechanics.md, animals/western_lowland_gorilla.md |
| DEP-002 | Animal Welfare (Habitat pillar) | Species housing stat block | Hippopotamus water-min requirement (1004 m²) equals its land min, without deep-swimming behavior -- hippos wade/walk on the substrate rather than swim, needing deep water for locomotion/wallowing with a gradual entry/exit slope. | high | mechanics.md, animals/hippopotamus.md |
| DEP-003 | DLC Layer (North America Animal Pack) | Species-specific enrichment roster | North America Animal Pack shipped 5 new enrichment items usable across the pack (Beaver Pool, Restraint Feeder, Piñata Zebra/Pronghorn, Prey-Scented Sack, Underwater Plant Feeder); Beaver Pool is the beaver-specific item. | high | mechanics.md, animals/north_american_beaver.md |
| DEP-004 | DLC Layer (Europe Pack) | Species-specific enrichment/viewing roster | Europe Pack's per-species mechanics: subterranean camera viewing (European Badger), Goat Climbing Mountain enrichment (Alpine Ibex), Rubbing Pad Bark (Eurasian Lynx). | high | mechanics.md, animals/european_badger.md, animals/alpine_ibex.md, animals/eurasian_lynx.md |
| DEP-005 | Genetics & Breeding (species appeal) | Species-specific appeal base stat | Top-tier species-appeal base of 6750 is tied among exactly three species: African Savannah Elephant, West African Lion, Western Lowland Gorilla. | high | mechanics.md, animals/african_savannah_elephant.md, animals/west_african_lion.md, animals/western_lowland_gorilla.md |
| DEP-006 | Conservation Credits (release payout) | Species-specific breeding/gestation timeline | African Savannah Elephant is cited as high as ~1,200 CC per release, but its 22-month gestation + 15-year maturation makes it CC-inefficient per unit time despite the high headline figure. | high | mechanics.md, animals/african_savannah_elephant.md |
| DEP-007 | Conservation Credits (color-morph premium) | Species-specific breeding outcome | Albino/melanistic color-morph lions command a 1,200-1,500 CC premium purely for the rare coat variant, independent of the four bred stats; West African Lion is the community's most commonly cited target species for this (also the "Ghost" achievement's most-cited target). | high | mechanics.md, animals/west_african_lion.md |
| DEP-008 | Achievements (Rebuilding, collection) | Species conservation-status tagging | The "Rebuilding" achievement (release 20 critically-endangered animals) is commonly pursued via fast-breeding critically-endangered exhibit species; the corpus documents at least three such species (Lesser Antillean Iguana, Lehmann's Poison Frog -- both base-game; Axolotl -- Conservation Pack DLC), not a single unique shortcut species. | high | achievements.md, animals/lesser_antillean_iguana.md, animals/lehmanns_poison_frog.md, animals/axolotl.md |

## PoNR / lockout edges

_None found this pass -- Career mode has no hard fail/lockout state (see `sections/missables.md` "Overall finding"); this table is expected to stay empty for a narrative-no-nav management sim unless a future DLC or update introduces a genuine point-of-no-return mechanic._

## Missable / sequencing dependencies

| Edge ID | Action | Window | Consequence | Source files |
|---------|--------|--------|-------------|--------------|
| SEQ-001 | Accept/adopt the retiring group of Indian Elephants offered through Career scenario 7's ("Power Struggle") reward/trading mechanic and house them properly | The scenario 7 offer window (rescue-animal-offer style, time-limited per community reports) | Missing the window blocks the "An Elephant Never Forgets" achievement until a scenario replay offers another chance | achievements.md, sections/power_struggle.md |

## Stitch run log

| Date | Scope | Edges written | Edges proposed (pending) | Inconsistencies surfaced | Model |
|------|-------|---------------|--------------------------|--------------------------|-------|
| 2026-08-22 | full | 9 | 0 | 2 | sonnet-class |

<!-- Inconsistencies surfaced: count from the per-edge convergence audit (stitch_and_zipper.md Phase B). Counts must be derived by reading this file, not recalled. A non-zero count requires an explicit chat call-out and at least one populated row in the Corpus inconsistencies section below. -->

## Corpus inconsistencies

Stitch's per-edge convergence audit (see [`stitch_and_zipper.md`](https://github.com/hintforge/builder/blob/main/stitch_and_zipper.md) Phase B) populates this section when a candidate edge's cited sources contradict each other. Each row records the contradiction; resolving it is the user's call (or a follow-up doctor / ingestion run). Edges blocked on an unresolved entry are NOT written to the tables above until the inconsistency is closed.

| Detected | Files | Conflicting values | Suspected authoritative source | Status |
|----------|-------|--------------------|--------------------------------|--------|
| 2026-08-22 | mechanics.md, animals/european_fallow_deer.md, animals/alpine_ibex.md, animals/red_deer.md | mechanics.md DLC Layer said Scarecrow Feeder is a Europe Pack item "shared, Fallow Deer/Ibex"; Fallow Deer's own file says diet/enrichment "not specified," Ibex's own file lists only Goat Climbing Mountain (no Scarecrow Feeder), and Red Deer (a base-game, non-Europe-Pack species) is the only entity file that actually documents Scarecrow Feeder | animals/red_deer.md (entity file, P3-resolved via 2 independent current-patch sources) | resolved -- mechanics.md's Europe Pack bullet corrected 2026-08-22 to remove the unsupported Fallow Deer/Ibex attribution |
| 2026-08-22 | achievements.md, animals/lesser_antillean_iguana.md, animals/axolotl.md, animals/lehmanns_poison_frog.md | Both achievements.md and lesser_antillean_iguana.md's own text claimed Lesser Antillean Iguana is "the only critically-endangered exhibit species" in the base game; axolotl.md and lehmanns_poison_frog.md are also documented as `Housing type: Exhibit` + `IUCN (in-game): Critically Endangered` | animals/axolotl.md, animals/lehmanns_poison_frog.md (both entity files, independently researched, same confidence class as the iguana file) | resolved -- both achievements.md and lesser_antillean_iguana.md corrected 2026-08-22 to drop the false "only" claim |

<!-- Status vocabulary: open (just surfaced) | resolved (user picked authoritative value + corrected the other file) | accepted (user accepted both -- rare; usually means the claim is genuinely ambiguous in-game). When status flips to resolved, the next stitch run can re-evaluate the edge. -->
