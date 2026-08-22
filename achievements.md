# Planet Zoo -- Achievements

**status:** research-integrated
**last_reconciled:** 2026-08-22
**stub_source:** Steam
**stub_fetched:** 2026-08-21
**dlc_coverage_checked:** 2026-08-22 (P3)

Single source of truth for "what achievements does this game have, and what do I need to do for each one." Achievement *names* are cited verbatim (lookup keys); trigger conditions are paraphrased in the maintainer's own words -- never the platform's description text (publisher IP).

## Genre vocabulary

- `multiplayer` -- requires Franchise mode (the only online mode) or a live Community Challenge event.
- `meta` -- a fourth-wall / pop-culture-reference achievement rather than a systems-test one.

## Coverage summary (P1 ingestion)

**38/38 achievement stubs resolved.** No DLC-lock evidence found for any of the 38 -- all reference base-game mechanics. Two entries (Silver Award, Gold Award) carry a lower-confidence residual detail: the single-scenario-vs-cumulative scope is inferred from the Bronze Award pattern rather than independently confirmed. Two entries (Tour Guide, Barrier Builder) carry an unresolved cumulative-vs-per-save scope ambiguity, same as Loaner's confirmed cumulative scope but without independent confirmation.

**Precondition-free completeness self-check**: the 38 ids below are `{1..38}`, no gaps, no duplicates -- verified by direct count while writing this file.

## DLC coverage (P3, 2026-08-22)

**Zero DLC-specific achievements exist for any of the 21 shipped DLC packs.** All 38 achievements above remain the complete Steam achievement list -- none are attached to a DLC appid; new DLC species contribute to existing base achievements (e.g. `Zoologist` -- full Zoopedia research; `Rebuilding` -- release threatened/endangered animals) rather than unlocking new ones. Confidence in this finding varies by pack (8 directly confirmed, 8 asserted at medium confidence, 5 carrying `[Hypothesis - unverified]` pending a follow-up pass with working Fandom access) -- see the per-pack confidence table in `mechanics.md` DLC Layer, which is the canonical home for this breakdown (role-split at zipper, 2026-08-22, to avoid maintaining the same 21-pack table twice).

## Progression

### 1. Welcome to Planet Zoo
- **id:** welcome_to_planet_zoo | **hidden:** no | **trigger_type:** progression
- **trigger:** Create your player avatar and place it on the world globe (first-run onboarding).
- **missable:** no | **ponr-window:** n/a | **prereqs:** none
- **vector-binding:** n/a (onboarding, not a corpus content location)
- **enemy-tier:** 0 | **puzzle-tier:** 0 | **spoiler:** none

### 2. Welcome to the Family
- **id:** welcome_to_the_family | **hidden:** no | **trigger_type:** progression
- **trigger:** Adopt your first animal, in any mode.
- **missable:** no | **ponr-window:** n/a | **prereqs:** none
- **vector-binding:** `mechanics.md` Conservation & Research
- **enemy-tier:** 0 | **puzzle-tier:** 0 | **spoiler:** none

### 5. Bronze Award
- **id:** bronze_award | **hidden:** no | **trigger_type:** progression
- **trigger:** Earn a Bronze rating on any one career scenario.
- **missable:** no | **ponr-window:** n/a | **prereqs:** Career mode access
- **vector-binding:** `sections/` (per-scenario Bronze objective)
- **enemy-tier:** 0 | **puzzle-tier:** 1 | **spoiler:** progression

### 7. Silver Award
- **id:** silver_award | **hidden:** no | **trigger_type:** progression
- **trigger:** Earn a Silver rating on any one career scenario.
- **missable:** no | **ponr-window:** n/a | **prereqs:** Career mode access
- **vector-binding:** `sections/`
- **enemy-tier:** 0 | **puzzle-tier:** 1 | **spoiler:** progression
- **notes:** single-scenario (vs. cumulative) scope inferred by naming/description parallel to Bronze/Gold Award, not separately confirmed. [Single source -- verify - class:community-wiki]

### 8. Say Goodbye
- **id:** say_goodbye | **hidden:** no | **trigger_type:** progression
- **trigger:** Release your first animal (to the wild or otherwise removed via the release mechanic).
- **missable:** no | **ponr-window:** n/a | **prereqs:** none
- **vector-binding:** `mechanics.md` Conservation & Research
- **enemy-tier:** 0 | **puzzle-tier:** 0 | **spoiler:** none

### 9. Gold Award
- **id:** gold_award | **hidden:** no | **trigger_type:** progression
- **trigger:** Earn a Gold rating on any one career scenario.
- **missable:** no | **ponr-window:** n/a | **prereqs:** Career mode access
- **vector-binding:** `sections/`
- **enemy-tier:** 0 | **puzzle-tier:** 1 | **spoiler:** progression
- **notes:** same inference basis as Silver Award. [Single source -- verify - class:community-wiki]

### 10. Life finds a way
- **id:** life_finds_a_way | **hidden:** no | **trigger_type:** progression
- **trigger:** First baby animal born in your zoo (natural breeding, not purchased).
- **missable:** no | **ponr-window:** n/a | **prereqs:** none
- **vector-binding:** `mechanics.md` Genetics & Breeding
- **enemy-tier:** 0 | **puzzle-tier:** 0 | **spoiler:** none

### 12. Franchise Zoo
- **id:** franchise_zoo | **hidden:** no | **trigger_type:** progression | **genre:** multiplayer
- **trigger:** Open your first zoo in Franchise mode.
- **missable:** no | **ponr-window:** n/a | **prereqs:** online connection
- **vector-binding:** `mechanics.md` Game Modes
- **enemy-tier:** 0 | **puzzle-tier:** 0 | **spoiler:** none

### 28. An Elephant Never Forgets
- **id:** an_elephant_never_forgets | **hidden:** no | **trigger_type:** progression
- **trigger:** In career scenario 7 ("Power Struggle"), accept/adopt the retiring group of Indian Elephants offered through that scenario's reward/trading mechanic, and house them properly.
- **missable:** yes | **ponr-window:** the scenario 7 offer window; a replay of the scenario may be needed for another chance if missed
- **prereqs:** reaching career scenario 7
- **vector-binding:** `sections/power_struggle.md`
- **enemy-tier:** 0 | **puzzle-tier:** 2 | **spoiler:** story
- **notes:** spoiler-in-name -- moderate. The name + trigger together reveal that scenario 7 involves a group of elephants being retired/rehomed as part of its narrative arc.

> **Cross-system dependency** -- see `dependencies.md` SEQ-001: this achievement's adoption window is tied to Career scenario 7's time-limited rescue-animal offer mechanic.

### 29. Career Complete
- **id:** career_complete | **hidden:** no | **trigger_type:** progression
- **trigger:** Bring every scored career scenario to at least Bronze (per one source, the 9 non-tutorial scenarios #4-12, not the 3 tutorials).
- **missable:** no (ratings can lapse if objectives aren't maintained, but likely only needs Bronze hit once per scenario)
- **ponr-window:** n/a | **prereqs:** all 9 (or 12) career scenarios played to at least Bronze
- **vector-binding:** `sections/`
- **enemy-tier:** 0 | **puzzle-tier:** 1 | **spoiler:** progression

### 31. Silver Career
- **id:** silver_career | **hidden:** no | **trigger_type:** progression
- **trigger:** Bring every scored career scenario to at least Silver (same "9 non-tutorial" caveat as Career Complete).
- **missable:** no | **ponr-window:** n/a | **prereqs:** Career Complete generally precedes this in normal play, not a hard prerequisite
- **vector-binding:** `sections/`
- **enemy-tier:** 0 | **puzzle-tier:** 1 | **spoiler:** progression

### 32. Gold Career
- **id:** gold_career | **hidden:** no | **trigger_type:** progression
- **trigger:** Bring every scored career scenario to Gold. "The Last Leg" is the natural completion point most guides reference.
- **missable:** no | **ponr-window:** n/a | **prereqs:** same as above
- **vector-binding:** `sections/the_last_leg.md`
- **enemy-tier:** 0 | **puzzle-tier:** 1 | **spoiler:** progression

## Mastery

### 3. Trainer
- **id:** trainer | **hidden:** no | **trigger_type:** mastery
- **trigger:** Train one staff member through all 5 tiers (Trainee -> Capable -> Skilled -> Expert -> Master).
- **missable:** no (repeatable, costs time/money per tier) | **ponr-window:** n/a | **prereqs:** at least one staff member
- **vector-binding:** `mechanics.md` Staff
- **enemy-tier:** 0 | **puzzle-tier:** 0 | **spoiler:** none

### 14. Animal Research
- **id:** animal_research | **hidden:** no | **trigger_type:** mastery | **genre:** multiplayer
- **trigger:** Bring one animal's Zoopedia research to 100% (gold medal) specifically while playing Franchise mode.
- **missable:** no | **ponr-window:** n/a | **prereqs:** Franchise mode; trained vet speeds this
- **vector-binding:** `mechanics.md` Conservation & Research
- **enemy-tier:** 0 | **puzzle-tier:** 0 | **spoiler:** none
- **notes:** boundary call vs. `collection` -- classified as mastery (deliberate full-investment completion of one entity's research profile, parallel to Trainer) rather than collection (which is reserved for finite named sets spanning many entities, e.g. Zoologist). The same research in Career/Sandbox does not trigger it per forum reports -- Franchise-specific.

### 17. Wow, that's a lot!
- **id:** wow_thats_a_lot | **hidden:** no | **trigger_type:** mastery
- **trigger:** Build a single habitat holding 30 animals, all simultaneously above 75% welfare.
- **missable:** no | **ponr-window:** n/a | **prereqs:** large, well-designed habitat
- **vector-binding:** `mechanics.md` Animal Welfare
- **enemy-tier:** 0 | **puzzle-tier:** 0 | **spoiler:** none
- **notes:** boundary call vs. `threshold` -- classified as mastery because the achievement requires a compound condition (count AND sustained welfare quality simultaneously), and the source explicitly frames the difficulty as sustaining 75%+ welfare at that density, not merely accumulating count.

### 27. Natural Selection
- **id:** natural_selection | **hidden:** no | **trigger_type:** mastery
- **trigger:** A single animal (bred or purchased) whose genetics exceed 90% in all four tracked categories (Size, Longevity, Fertility, Immunity) simultaneously.
- **missable:** no (rare organically -- most players buy/breed toward it deliberately) | **ponr-window:** n/a
- **prereqs:** access to strong breeding stock or Franchise market
- **vector-binding:** `mechanics.md` Genetics & Breeding
- **enemy-tier:** 0 | **puzzle-tier:** 0 | **spoiler:** none
- **notes:** boundary call vs. `threshold` -- a compound simultaneous-quality condition on one entity's four stats, not a cumulative count, so mastery fits better than threshold.

### 36. Hard - Career Complete
- **id:** hard_career_complete | **hidden:** no | **trigger_type:** mastery
- **trigger:** Same as Career Complete (all scored scenarios to Bronze), but every scenario must specifically have Hard difficulty selected.
- **missable:** no, but a real trap: difficulty is set **per scenario at launch**, not once for the whole career -- forgetting to pick Hard on any individual scenario launch means that scenario won't count even if otherwise cleared. [Single source -- verify - class:forum]
- **ponr-window:** each scenario's launch screen | **prereqs:** same career-completion path as Career Complete, replayed with Hard selected each time
- **vector-binding:** `mechanics.md` Game Modes (difficulty note)
- **enemy-tier:** 0 | **puzzle-tier:** 0 | **spoiler:** none

### 37. Hard - Silver Career
- **id:** hard_silver_career | **hidden:** no | **trigger_type:** mastery
- **trigger:** Same as Silver Career, entirely on Hard difficulty (same per-scenario selection trap as #36).
- **missable:** no (same trap as #36) | **ponr-window:** n/a | **prereqs:** same as #36
- **vector-binding:** `mechanics.md` Game Modes
- **enemy-tier:** 0 | **puzzle-tier:** 0 | **spoiler:** none

### 38. Hard - Gold Career
- **id:** hard_gold_career | **hidden:** no | **trigger_type:** mastery
- **trigger:** Same as Gold Career, entirely on Hard difficulty (same per-scenario selection trap as #36).
- **missable:** no (same trap as #36); forum threads describe this as very rarely earned (sub-1% unlock rates cited anecdotally)
- **ponr-window:** n/a | **prereqs:** same as #36
- **vector-binding:** `mechanics.md` Game Modes
- **enemy-tier:** 0 | **puzzle-tier:** 0 | **spoiler:** none

## Collection

### 11. Enriched
- **id:** enriched | **hidden:** no | **trigger_type:** collection
- **trigger:** Place 25 different (distinct) enrichment item types across your zoo -- not 25 copies of one item.
- **missable:** no (cumulative, easy in normal career play) | **ponr-window:** n/a | **prereqs:** none
- **vector-binding:** `mechanics.md` Animal Welfare
- **enemy-tier:** 0 | **puzzle-tier:** 0 | **spoiler:** none

### 15. Redecorating
- **id:** redecorating | **hidden:** no | **trigger_type:** collection
- **trigger:** In an exhibit (not a habitat), unlock and activate every enrichment slot/level available for that exhibit animal.
- **missable:** no (must be an exhibit specifically -- habitats don't count) | **ponr-window:** n/a
- **prereqs:** exhibit animal fully researched
- **vector-binding:** `animals/index.md` (Exhibit housing type)
- **enemy-tier:** 0 | **puzzle-tier:** 0 | **spoiler:** none

### 19. Zoologist
- **id:** zoologist | **hidden:** no | **trigger_type:** collection
- **trigger:** Fully complete the Zoopedia -- max research ("fun facts") on every base-game animal (habitat and exhibit).
- **missable:** no; research progress is shared across Career/Franchise/Challenge zoos, but NOT achievable via Sandbox research alone per forum reports
- **ponr-window:** n/a | **prereqs:** non-Sandbox research mode; trained vets speed research
- **vector-binding:** `animals/index.md`
- **enemy-tier:** 0 | **puzzle-tier:** 0 | **spoiler:** none
- **notes:** owning any DLC before finishing this adds those animals to the required list too -- this guide's base-game scope means the base 78-species roster alone should suffice for a base-game-only playthrough.

### 33. Diversity
- **id:** diversity | **hidden:** no | **trigger_type:** collection | **genre:** multiplayer
- **trigger:** Open a Franchise-mode zoo in each of the 6 biomes (Taiga, Tundra, Desert, Grassland, Temperate, Tropical).
- **missable:** no | **ponr-window:** n/a | **prereqs:** Franchise mode, enough CC to open zoos in new biome slots
- **vector-binding:** `mechanics.md` Game Modes / Economy & Currencies
- **enemy-tier:** 0 | **puzzle-tier:** 0 | **spoiler:** none
- **notes:** confirmed via forum discussion that this does not trigger from Career or Sandbox zoos even covering different biomes.

### 35. Planet Zoo
- **id:** planet_zoo | **hidden:** no | **trigger_type:** collection | **genre:** multiplayer
- **trigger:** Open a Franchise-mode zoo on each of the 7 continents (any biome combination -- just continent coverage).
- **missable:** no | **ponr-window:** n/a | **prereqs:** Franchise mode, Conservation Credits
- **vector-binding:** `mechanics.md` Game Modes / Economy & Currencies
- **enemy-tier:** 0 | **puzzle-tier:** 0 | **spoiler:** none

## Threshold

### 4. A superstar comes along
- **id:** a_superstar_comes_along | **hidden:** no | **trigger_type:** threshold
- **trigger:** Get any single animal's individual Animal Rating to 5 stars.
- **missable:** no (can be chased indefinitely) | **ponr-window:** n/a | **prereqs:** none
- **vector-binding:** `mechanics.md` Zoo Rating
- **enemy-tier:** 0 | **puzzle-tier:** 0 | **spoiler:** none

### 13. Baby Boom
- **id:** baby_boom | **hidden:** no | **trigger_type:** threshold
- **trigger:** Cumulative total of 73 baby animals born across your play.
- **missable:** no | **ponr-window:** n/a | **prereqs:** none
- **vector-binding:** `mechanics.md` Genetics & Breeding
- **enemy-tier:** 0 | **puzzle-tier:** 0 | **spoiler:** none
- **notes:** the reason for the specific number "73" is undocumented anywhere found.

### 16. This one's a Keeper
- **id:** this_ones_a_keeper | **hidden:** no | **trigger_type:** threshold
- **trigger:** Employ >=3 keepers, each in a separate work zone, simultaneously. Explicitly only counts in Sandbox, Franchise, or Challenge mode -- Career mode does not trigger it.
- **missable:** no | **ponr-window:** n/a | **prereqs:** 3 keepers, 3 distinct work zones, non-Career save
- **vector-binding:** `mechanics.md` Staff
- **enemy-tier:** 0 | **puzzle-tier:** 0 | **spoiler:** none

### 20. Loaner
- **id:** loaner | **hidden:** no | **trigger_type:** threshold
- **trigger:** Repay a cumulative $50,000 in zoo loans -- cumulative across ALL saves/zoos, confirmed explicitly (unlike most other achievements, which are presumed per-save).
- **missable:** no (can grind small loan/repay cycles across many zoos) | **ponr-window:** n/a | **prereqs:** none
- **vector-binding:** `mechanics.md` Economy & Currencies
- **enemy-tier:** 0 | **puzzle-tier:** 0 | **spoiler:** none

### 21. Tour Guide
- **id:** tour_guide | **hidden:** no | **trigger_type:** threshold
- **trigger:** Build a cumulative 1 kilometer of tracked ride path.
- **missable:** no | **ponr-window:** n/a | **prereqs:** none
- **vector-binding:** `mechanics.md` Guests & Facilities
- **enemy-tier:** 0 | **puzzle-tier:** 0 | **spoiler:** none
- **notes:** unclear whether cumulative across saves (like Loaner) or must be built within a single zoo/save -- no source explicitly states which. [Single source -- verify - class:community-wiki]

### 22. Barrier Builder
- **id:** barrier_builder | **hidden:** no | **trigger_type:** threshold
- **trigger:** Build a cumulative 10 kilometers of barrier/fencing.
- **missable:** no | **ponr-window:** n/a | **prereqs:** none
- **vector-binding:** `mechanics.md` Habitats & Enclosures
- **enemy-tier:** 0 | **puzzle-tier:** 0 | **spoiler:** none
- **notes:** same cumulative-vs-per-save scope ambiguity as Tour Guide. [Single source -- verify]

### 23. Nerd
- **id:** nerd | **hidden:** no | **trigger_type:** threshold | **genre:** multiplayer
- **trigger:** Reach a 5-star Education Rating specifically in a Franchise-mode zoo.
- **missable:** no | **ponr-window:** n/a | **prereqs:** Franchise mode
- **vector-binding:** `mechanics.md` Zoo Rating / Guests & Facilities
- **enemy-tier:** 0 | **puzzle-tier:** 0 | **spoiler:** none
- **notes:** a Sandbox zoo hitting 5-star education does not trigger it per forum reports -- Franchise-specific, same pattern as Animal Research.

### 25. Rebuilding
- **id:** rebuilding | **hidden:** no | **trigger_type:** threshold
- **trigger:** Release a cumulative 20 critically-endangered animals to the wild. Only adults either bought with conservation points or bred in your own zoo qualify (species must carry the game's "critically endangered" conservation-status tag).
- **missable:** no, but slow with big critically-endangered species (gorillas, chimps, lions)
- **ponr-window:** n/a | **prereqs:** conservation-status-tagged critically endangered animals
- **vector-binding:** `mechanics.md` Conservation & Research
- **enemy-tier:** 0 | **puzzle-tier:** 0 | **spoiler:** none
- **notes:** `animals/lesser_antillean_iguana.md` is a commonly used fast-breeding shortcut among the base game's critically-endangered exhibit species -- not the only such species (also `animals/lehmanns_poison_frog.md`, base-game, and `animals/axolotl.md`, Conservation Pack DLC; corrected 2026-08-22 stitch pass, see `dependencies.md` Corpus inconsistencies).

> **Cross-system dependency** -- see `dependencies.md` DEP-008: the "Rebuilding" achievement's fast-breeding shortcut depends on species conservation-status tagging; at least three critically-endangered exhibit species exist in the corpus.

### 34. Global Zoo
- **id:** global_zoo | **hidden:** no | **trigger_type:** threshold | **genre:** multiplayer
- **trigger:** Open a cumulative 25 zoos in Franchise mode (not all concurrent -- only 10 Franchise zoos can be active at once, so this requires cycling zoo slots over time). Each new zoo costs ~100 CC; Franchise grants ~100 CC/day for logging in, so ~2,500 CC total is the rough budget.
- **missable:** no; time-gated by CC accrual rate if not supplemented via Community Challenges
- **ponr-window:** n/a | **prereqs:** Franchise mode, Conservation Credits
- **vector-binding:** `mechanics.md` Game Modes / Economy & Currencies
- **enemy-tier:** 0 | **puzzle-tier:** 0 | **spoiler:** none

## Discovery

### 6. Oh My!
- **id:** oh_my | **hidden:** no | **trigger_type:** discovery | **genre:** meta
- **trigger:** Have a lion, a tiger, and a bear simultaneously present in the same zoo (any species/subspecies of each).
- **missable:** no; achievable in one sitting in Franchise/Sandbox | **ponr-window:** n/a | **prereqs:** none
- **vector-binding:** `animals/index.md` (species roster)
- **enemy-tier:** 0 | **puzzle-tier:** 0 | **spoiler:** none
- **notes:** pop-culture reference to "Lions and tigers and bears, oh my!" (The Wizard of Oz).

### 18. Ghost
- **id:** ghost | **hidden:** no | **trigger_type:** discovery
- **trigger:** Produce an albino animal through breeding (most reliably forced via inbreeding related animals, e.g. cousin pairings) or otherwise obtain one (e.g. Franchise market purchase).
- **missable:** no; RNG-gated if bred naturally | **ponr-window:** n/a | **prereqs:** breeding stock or market access
- **vector-binding:** `mechanics.md` Genetics & Breeding (inbreeding / cousin blind spot)
- **enemy-tier:** 0 | **puzzle-tier:** 0 | **spoiler:** none
- **notes:** the community's most reliable route deliberately exploits the cousin/aunt/uncle inbreeding blind spot documented in `mechanics.md`.

### 24. Circle of Life
- **id:** circle_of_life | **hidden:** no | **trigger_type:** discovery
- **trigger:** A juvenile lion is born into a zoo that already contains 10+ different species (any mix).
- **missable:** no; commonly falls out naturally partway through the first tutorial scenario
- **ponr-window:** n/a | **prereqs:** 10+ species already present, lion breeding pair
- **vector-binding:** `animals/west_african_lion.md`
- **enemy-tier:** 0 | **puzzle-tier:** 0 | **spoiler:** none
- **notes:** boundary call vs. `threshold` -- classified as discovery because the compound condition (species-count + lion birth) is non-obvious and typically stumbled into rather than deliberately pursued, per the source's own framing.

### 26. Community
- **id:** community | **hidden:** no | **trigger_type:** discovery | **genre:** multiplayer, social
- **trigger:** Participate in and submit a Community Challenge -- a Franchise-mode-only, rotating ~4-day event running roughly biweekly, requiring play/breeding toward that cycle's animal goal, then manually submitting progress via an in-game trophy-icon button.
- **missable:** yes-ish -- time-gated to whenever a Community Challenge event is live
- **ponr-window:** the live event window | **prereqs:** Franchise mode, an active Community Challenge window
- **vector-binding:** `mechanics.md` Economy & Currencies (Franchise-exclusive CC extras)
- **enemy-tier:** 0 | **puzzle-tier:** 0 | **spoiler:** none
- **notes:** boundary call -- doesn't map cleanly to any of the six values; classified as discovery (the residual bucket) since it's participation-shaped rather than a count/collection/skill test.

### 30. The Elephant in the Room
- **id:** the_elephant_in_the_room | **hidden:** no | **trigger_type:** discovery
- **trigger:** Have two different elephant species (African and Indian) born via breeding in the same zoo. Confirmed to work in Sandbox mode (not mode-restricted like several others).
- **missable:** no | **ponr-window:** n/a | **prereqs:** breeding pairs of two elephant species
- **vector-binding:** `animals/african_savannah_elephant.md`, `animals/indian_elephant.md`
- **enemy-tier:** 0 | **puzzle-tier:** 0 | **spoiler:** none
- **notes:** mild pun at most, no narrative reveal despite the elephant theme overlapping career scenario 7.

## Sources

- Canonical Steam achievement list: https://steamcommunity.com/stats/703080/achievements (fetched 2026-08-21, primary, all 38 verbatim trigger texts)
- Exophase and GamesXtreme per-achievement pages
- TrueSteamAchievements -- Rebuilding, Zoologist, Community
- Frontier Forums thread on "This one's a Keeper"
- Steam Discussions on Sandbox achievement restrictions, Medium vs. Hard career difficulty
- steamah.com Career Mode Guide [editorial-en]
- us.gamesplanet.com achievements list [cross-check of all 38 names/descriptions]

Inaccessible this session (documented, not silently skipped): Fandom Achievements page (all fallback rungs failed), a rate-limited Steam 100%-guide (id 2707585690), PSNProfiles/xboxachievements/gamefaqs/truesteamachievements game-list page/steamhunters (all 403s), direct r/PlanetZoo access. See `limitations.md`.
