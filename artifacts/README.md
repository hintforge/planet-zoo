# Planet Zoo -- interactive tools

Self-contained HTML tools that read this guide's corpus data. Open the file in any browser;
nothing is installed, nothing phones home, and everything you type stays in your own browser.

## Zoo Planner -- `zoo_planner.html`

A working surface to keep open beside the game.

- **Roster.** All 210 species in one sortable, filterable table -- land and water area,
  climbing area, temperature band, social group size, sex-ratio cap, biome, diet, mixing
  compatibility, IUCN status and pack. Filter by continent, biome, housing type, pack,
  conservation status or data completeness. Click any row for the full record, including its
  terrain composition and welfare gotcha.
- **Plan.** Add species with the male/female split you intend to keep. It totals the land,
  water and climbing area the game will require, and flags sex-ratio breaches, group sizes
  outside the documented range, and any species whose data is incomplete.
- **Budget.** Pick your game mode -- the four economies work differently and the tool keeps
  them apart. Enter your cash and your real figures from the in-game finance report, enter
  animal prices from the purchase panel, and it works out what the plan costs and how long
  your cash lasts.
- **Reference.** Sex-ratio caps, a worked shop-pricing example, an opening playbook, and the
  Career scenario medal objectives.

### What it will not do

**It does not predict your income.** Planet Zoo publishes no ticket-price or guest-spend
formula, and no community source has reverse-engineered one -- revenue is documented only as
ratios tied to a zoo you have not built yet. Rather than dress a guess up as a projection,
the budget tab asks for the figures your own finance report already shows and does the
arithmetic on those.

**It does not invent missing data.** Where the corpus has no figure, the cell reads "not
recorded" rather than zero, and the totals say how many species were left out. Habitat sizes
exist for 142 of 210 species; 68 do not have one, and 22 species are flagged because the
research pass could not reach their in-game data at all. You will see exactly which.

**Prices are yours to enter.** No source publishes animal or building prices and they shift
between patches, so the tool ships with empty price fields instead of stale numbers. What
you enter is remembered in your browser.

## Where the numbers come from

Everything is extracted from this repository -- `animals/*.md` for species data,
`mechanics.md` for the economy rules and reference tables, `sections/*.md` for the Career
scenarios. Every figure traces back to a `_source:` line in those files, which records its
origin and a confidence level. Community-sourced material (the shop prices, the opening
playbook) is marked as such on the page rather than presented as authoritative.

## Caveat

The tool has not been validated against a running game. The maths follows the corpus, and
the corpus follows its sources, but no one has yet sat with the game open and confirmed that
a habitat sized here satisfies the game. Treat totals as a floor to clear, not a guarantee --
and they cover the animals only, not paths, barriers, viewing areas or the space between
habitats.
