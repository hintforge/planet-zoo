# Planet Zoo -- Mechanics Reference

**status:** research-integrated
**last_reconciled:** 2026-08-22

The core game-system knowledge surface. Planet Zoo has **high cross-system dependency** -- welfare, economy, staff, guests, genetics, conservation, and building all feed the Zoo Rating and each other. All content below is `spoiler: none`, `enemy-tier: 0`, `puzzle-tier: 0` unless noted -- this is systems content, not narrative.

## Zoo Rating

Primary success metric, computed from five factors per the official Frontier help centre: **Animal Rating** (count, variety, welfare of animals), **Conservation Rating** (conservation activity), **Education Rating** (guest education level leaving the zoo + vets in advanced research + Zoopedia unlock level), **Marketing** (active campaigns), **Guest Happiness Rating** (live rolling average of currently-in-zoo guests' happiness %).

_source: deep-research cascade P1 2026-08-21 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

A widely-circulated Steam Workshop guide instead lists Animals / Conservation / Education / **Scenery** / Guest Happiness -- dropping Marketing and substituting Scenery. Most guides reproduce one list or the other without reconciling; both commonly omit that Marketing has a documented weight below. [Contradicted across sources -- see notes]

**Weighting:** the only hard number found anywhere is **"15% of a zoo's reputation is based on marketing campaigns"** (official Frontier source). No other category's relative weight is documented anywhere -- do not invent numbers for Animal/Conservation/Education/Guest-Happiness weighting. **P3 gap-fill (2026-08-22) re-searched this specifically and confirmed the gap is genuine, not an oversight**: the same official Frontier Beginner's Guide section ("Reputation & Points") that sources the 15% figure lists the other four categories (Animal, Conservation, Education, Guest Happiness Rating) by name with no accompanying weight, and no community source fills the remaining 85%. Treat as a permanent documentation gap unless Frontier publishes a formula.

_source: Frontier official help centre · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

**Star scale:** 1-5 stars, overall and per named sub-rating. Underlying score is continuous/decimal, displayed as stars -- Career objective text quotes exact thresholds: 2.0 (Bronze), 3.0 (Silver), 4.0 (Gold). **"Zoo Points" is a separate metric** (combined animal appeal + education + reputation, diminishing returns for same-species duplicates) -- NOT the internal rating number; conflating the two is a common guide error.

**The periodic "Inspector" event is NOT the same system as the always-on Zoo Rating.** The Inspector samples up to 5 animals + checks guest needs/education and produces its own report, distinct from the persistent reputation display -- a player can have all sampled animals and displayed categories at 5 stars yet the "overall" inspection score reads lower. Most guides use "zoo rating" and "inspection rating" interchangeably, which is an error.

_source: deep-research cascade P1 2026-08-21 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

**Mechanism notes:**
- Education Rating updates on a rolling window of roughly the last 100-150 guests to leave the zoo, not live -- explains persistent player reports of the rating "lagging" recent fixes.
- Individual Animal Rating climbs via an appeal curve: welfare, genetics/longevity, and time-in-zoo raise appeal over time; juveniles reset on maturing; animals parked in the Trade Center pause aging while appeal keeps rising -- a known min-max exploit.
- **Career**: rating directly wired into Bronze/Silver/Gold decimal thresholds (2.0/3.0/4.0); market is scenario-restricted independent of rating. **Franchise**: rating computes/displays but nothing is explicitly gated behind it. Whether Franchise aggregates rating across a player's multiple zoos is unconfirmed by any source -- inferred (not stated) that each zoo's rating calculates independently. **Sandbox**: one data point suggests 5-star Education Rating in Sandbox does NOT trigger the "Nerd" achievement (see `achievements.md`) -- mechanism unclear (Sandbox achievement suppression vs. an actual rating-calc difference).
- No source ties loan eligibility/size/interest to a zoo-rating threshold -- loans are gated by mode/scenario, not reputation stars.

_source: deep-research cascade P1 2026-08-21 · capture: web_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [several sub-claims Single source -- verify]

## Animal Welfare

**Four top-level welfare pillars** shown in the Animal Information Panel, with Stress as a cross-cutting modifier rather than a fifth independent pillar:
- **Nutrition** -- Nourishment (hunger), Last Meal Quality, Hydration (thirst), Last Drink Cleanliness.
- **Social** -- social group satisfaction (group size vs. species preference, sex balance, loneliness/overcrowding).
- **Habitat** -- how well terrain composition, plant/biome suitability, temperature, and cleanliness match species needs.
- **Enrichment** -- mental stimulation from toys/feeders/interactive objects; decays with use.

An older wiki revision instead lists "Nutrition, Social, Space, Stress" as the four majors -- treat Nutrition/Social/Habitat/Enrichment as the current model (in-panel labels).

_source: deep-research cascade P1 2026-08-21 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

**No source produced the exact overall-score weighting formula across the four pillars** -- a confirmed gap in the public community corpus, not merely hard to find. [Hypothesis -- unverified]

**Star rating** (an individual animal's appeal/popularity, distinct from welfare %) rises over time and faster with higher welfare; also influenced by genetics (Longevity gene extends the window to reach 5 stars), food quality, zoo tenure, and general popularity.

_source: deep-research cascade P1 2026-08-21 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

### What triggers welfare LOSS (mechanism, not inventory)

- **Enrichment decay is continuous and real-time-based**: each item's contribution diminishes the longer it sits unused/stale (~10% recovery per in-game month when an item is pulled and replaced [single source]). Decay on one item can't be offset by freshness of another -- 100% Enrichment on demanding species (e.g. Western Lowland Gorilla) requires every possible enrichment object present and freshly placed simultaneously. As habitat animal count rises, enrichment-point demand rises with it; past a point 100% enrichment becomes mathematically unreachable regardless of effort.
- **Stress is guest-visibility- and privacy-driven**: an animal takes a stress penalty when it wants to hide from guests and has no hard-shelter/retreat option; "more confident" species tolerate larger guest crowds before stress accrues than shy species at the same density. **One-way glass zeroes the guest-visibility stress term specifically** -- the animal's AI does not register being observed through it -- a targeted fix, not a general welfare boost.
- **Overcrowding is a Social-pillar mechanism**: space required per animal scales with headcount, worse in mixed-species habitats; walkthrough/guest-accessible habitats compound this by adding guests as a second population inside the enclosed space -- mitigated by a single guest gate capping guest numbers.
- **Illness/disease is an independent welfare-depressing channel**, separate from the four pillars; poor Nutrition accelerates illness onset (Nutrition failure -> Health failure -> further welfare depression). New arrivals must go through quarantine to avoid spreading disease.
- **Barrier failure is a distinct escape trigger, not itself a welfare-score input**: barriers deteriorate continuously (except hedges, electric fences, null barriers, which never degrade) -- once condition drops enough, breach/collapse becomes possible regardless of welfare state.
- **"Dilapidation rate" labels read backwards from intuition** -- a genuine trap. Wood/log walls are labeled "Low" dilapidation and brick "High," implying wood should hold up better. A controlled one-in-game-year test (matched habitats) found the opposite: brick ("High") ended at 69% condition vs. log ("Low") at 59% -- the label describes durability/damage-resistance under stress, not passive decay speed. [Single source -- verify, one controlled test]

_source: deep-research cascade P1 2026-08-21 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

### What triggers welfare RECOVERY

Recovery reverses the specific deficient sub-stat: refreshing enrichment, restocking food/water, cleaning habitats, keeper/mechanic maintenance visits, unlocking better nutrition/enrichment via research. **No source gave an exact recovery rate (%/hour or /day) for any pillar** except the ~10%/month enrichment-rejuvenation figure above -- a documented gap across every source class searched, including datamining. [Hypothesis -- unverified] **P3 gap-fill (2026-08-22) re-searched this specifically (official Frontier guide, community datamining, Frontier forums, Reddit) and found nothing further** -- the official guide describes the four pillars qualitatively only ("declines over time," interspecies social enrichment "can significantly offset" decay) with no numbers. This remains the single largest unresolved gap-fill target from the P1/P3 cascade -- see `limitations.md`.

Difficulty setting materially changes pacing: on Easy, welfare degrades more slowly, animals take longer to reach critical/death states, and enrichment decay may be effectively disabled/floored. Sandbox has a separate toggle to disable enrichment decay entirely.

_source: deep-research cascade P1 2026-08-21 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

### Common new-player mistakes

Enrichment over-saturation (duplicate objects don't help -- one of each type suffices, the bottleneck is decay-cycling not raw count); skipping mechanic/vet research that gates nutrition/enrichment upgrades; treating high welfare as a default state (animals start implicitly high and only degrade through neglect, hiding early warning signs); ignoring species-specific Zoopedia minimums and applying one generic habitat template across species; poor quarantine discipline; only checking the aggregate habitat view and missing an individual outlier animal dragging the average down.

_source: deep-research cascade P1 2026-08-21 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

### Species/group exceptions to general welfare rules

- **Solitary/matrilineal/patrilineal/gregarious social typing** (added Update 1.13) changes how the Social pillar applies per species: solitary species (e.g. Siberian Tiger, Grizzly Bear) have offspring marked "Outsiders" once they exceed population limits or parents remain present, and Outsiders are excluded from mating/play/social interaction entirely -- a solitary species' Social welfare can tank precisely *because* related animals are cohabiting, the opposite of what drives gregarious-species Social welfare. Animals can eventually integrate by spending enough time near the group.
- Western Lowland Gorilla is tagged **solitary** maturation-type despite living in structured family troops -- an outlier vs. its own family's usual grouping rules (see `animals/western_lowland_gorilla.md`).
- Hippopotamus has an enormous water-area requirement (1004 m², equal to its land min) without deep-swimming behavior at all -- hippos don't swim in Planet Zoo, they walk along the substrate, needing deep water for locomotion/wallowing with a gradual entry/exit slope, not for a swim animation. [Single source -- verify]

> **Cross-system dependency** -- see `dependencies.md` DEP-001: Western Lowland Gorilla's solitary maturation-type tag despite family-troop living.
> **Cross-system dependency** -- see `dependencies.md` DEP-002: Hippopotamus water-min requirement equals land-min without deep-swim behavior.

_source: deep-research cascade P1 2026-08-21 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

### Sex-ratio caps within a social group

Separate from the group-size range each species carries, a species also has a **male:female cap** -- a ceiling on how many males a group may hold relative to its females, above which sex-based fighting starts. The cap behaves as a **ratio, not a fixed pair**: divide the male figure by the female figure, multiply by the actual female count, and that is the permitted number of males.

- **Indian Peafowl -- 4:16.** A muster of 20 may hold up to 4 males and 16 females. 4/16 = 0.25, so 2 males alongside 8 females is within the cap; 2 males alongside 7 females is over it.
- **West African Lion -- 1:29.** Males do not tolerate one another whenever a mate is present, without exception. A bachelor-only group may instead hold up to 4 males, or up to 30 females.

**This is a planning constraint the group-size field alone does not express**: a habitat sized correctly for 20 peafowl still fails if the sex split is wrong. Only these two species were recovered at this granularity -- the cap applies game-wide, but per-species figures for the rest of the roster are **not obtained**. Treat an undocumented species' cap as unknown; do not assume a default ratio.

_source: manually-collected community research pass 2026-09-16 (Steam Community guide "Saturn's Comprehensive Guide to Planet Zoo" by leemonshark) · capture: manual-clipping · confidence: low (single-source community guide; only two species documented at this granularity) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Habitats & Enclosures

### Barrier types and the escape mechanic

Barrier categories: fences (wood/log, brick, concrete, hedge), electric fences, glass (standard and one-way), moats/deep water, and the null barrier. Each carries a **strength rating** and a **climb rating** (separate stats), plus an **opacity** flag and an optional **watertight** flag. Height requirement is species-specific per the Zoopedia (e.g. Snow Leopard needs barriers >=3m); a barrier under a species' minimum is treated as climbable/jumpable regardless of material.

**Four distinct escape failure modes** (mainstream guides conflate them into one "barrier too short" explanation):
1. **Climbing/jumping out** -- driven by jump-height stat vs. barrier height, but also by nearby climbable objects (trees, rocks, even scenery) placed within jump range *outside* the barrier, usable as a step-up even when the barrier itself is tall enough. Fix: remove/relocate the external object, not raise the barrier.
2. **Crossing a null barrier where the "real" barrier behind it is insufficient** -- the null barrier is inert scenery-hiding, not containment.
3. **Swimming over a low barrier relative to water level** -- most animals can swim, so water itself is not a barrier; ground must be raised to water level, or a rock-wall barrier in water needs the ground raised first.
4. **A dilapidation hole, or the animal physically knocking the barrier down** (elephants leaning/headbutting through glass, even mid-tier material) -- a strength-rating failure independent of height.

**Empirically tested jump-height data** (one Steam guide author's controlled sandbox test across 90+ species): the overwhelming majority (elephants, rhinos, hippos, giraffes, bears, all primates tested, smaller cats, most birds) cannot clear a 1m vertical barrier. Only five species cleared a 1m drop in testing: Bengal Tiger, Siberian Tiger, Cougar (DLC), Jaguar (DLC), West African Lion -- none cleared 2m+. Two anomalies: red/black-and-white ruffed lemurs appeared to visually clip *through* solid barriers with no climbing path found; burrowing species (prairie dogs/meerkats, DLC) can dig beneath platforms but pop back up rather than actually escaping. [Single source -- verify, one player's systematic test, unreplicated elsewhere]

Digging escape: trench moats must be dug deeper than the barrier-height-equivalent for the species -- not automatically escape-proof by width alone. [Single source -- verify]

**Electric fences: strength 6 when powered, versus strength 1-2 unpowered** -- an unpowered electric fence reverts to one of the weakest barrier types, a documented trap for players who assume "electric" implies inherent extra security even unpowered. [Single source -- verify]

**Diagnostic tool**: Habitat View mode, with an animal selected, visually renders its full traversable area in blue and marks actual escape points in red circles -- the correct workflow for finding an escape rather than guessing at barrier height.

_source: deep-research cascade P1 2026-08-21 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

### Terrain painting

Brush tool selecting from ~8 biome-tied textures (short/long grass, light/heavy soil, smooth/rough rock, fine/coarse sand, snow), applied via mouse-hover with adjustable brush size (bracket keys). **Intensity is speed-sensitive**: moving the cursor quickly applies a light/thin coat, slowly builds denser saturation -- coverage is a function of paint dwell time, not a single on/off application. An auto-paint option randomly selects from biome-appropriate textures.

The welfare-relevant "Terrain Distribution" need is a percentage-range tolerance per species across paintable texture types (documented per species in `animals/`). Community guidance: layer paints, laying the species' most-wanted terrain type first at full intensity, then layering others, rather than precisely tiling discrete zones.

Plants are a related but distinct requirement from painted ground terrain: ideally match both continent/region and biome (a North American temperate-biome animal wants North American plants specifically, not just "temperate" plants generically); the game visually flags wrong-biome plants in red in the planting UI.

_source: deep-research cascade P1 2026-08-21 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

### Climate/temperature control

Animals require a temperature range, not a single target -- good practice is to vary temperature across the habitat within that band rather than force one uniform value everywhere. Heaters/coolers have an adjustable radius (originally capped ~5m, later expanded); cost scales non-linearly -- one large-radius (20) unit costs more than two smaller-radius (14) units combined, making multiple smaller units often more efficient. They require power, can be partially sunk into the ground (hold Shift while placing) or hidden behind scenery without losing function. Full-habitat coverage at the "ideal" temperature is not required for welfare -- animals are satisfied if they can move between shelter/food/water while staying within the acceptable band.

Misters were found only as a general "hot pool" simulation/scenery effect -- no source gave misters a distinct climate-control mechanical role separate from heaters/coolers. [Hypothesis -- unverified, a real gap]

_source: deep-research cascade P1 2026-08-21 · capture: web_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

### One-way glass

Lets guests view an animal while the animal's AI does not register being watched -- specifically zeroes the guest-visibility component of Stress, not a general welfare buff. Requires mechanic research (Barriers track, reported around research level 7, a long unlock) before permanently available; some panels usable earlier as standalone objects. Facing/orientation can be flipped after placement. Primary use case: shy/easily-stressed species and viewing angles where players don't want to pay the Stress cost.

_source: deep-research cascade P1 2026-08-21 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

### Null barrier

An invisible/inert boundary meant to be hidden inside scenery/terrain/construction -- it does not itself stop an animal; it only functions when something else physically blocks the animal at that location (tall/steep terrain, a cliff, rockwork, or a real barrier layered behind it). Because it's inert, an animal that can climb/swim past the *real* physical stop will walk straight through a null barrier -- a common trap where players assume the null barrier itself provides containment. Does not degrade over time (unlike almost all physical barrier types), which is why it's used as a permanent maintenance-free boundary marker.

_source: deep-research cascade P1 2026-08-21 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

### Viewing galleries and the water-physics caveat

Underwater/below-grade viewing galleries combine a below-water-level guest path/tunnel with glass barrier segments; placing underwater feeders near the glass draws animals to the window on cue. Guest satisfaction at a viewing point is multi-factorial, not purely welfare-driven: barrier transparency, physical sightline obstructions, educational signage presence, and habitat cleanliness/water clarity all separately affect the guest's logged experience.

**Important caveat**: Planet Zoo's water is a visual-effects system, not simulated fluid dynamics -- there is no calculated drainage/flow between elevations. Water depth for animal welfare purposes (deep-swim requirement, hippo wading) is a terrain-height/painted-water-surface property, evaluated independently of any decorative waterfall/flow effects layered on top.

_source: deep-research cascade P1 2026-08-21 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Economy & Currencies

### Cash -- earning

**Ticket sales**: guests evaluate price against a qualitative perceived-value signal (too cheap -> fair -> good -> too expensive); pricing too high causes refused entry. **Shops**: restaurants earn ~3-4x the best food-stall profit, drink shops ~5-6x an info/food stand, balloons ~2x an info/food stand; adoption packs sell at ~100% profit (no production cost). **Donation bins**: donation size scales with the guest's satisfaction from the *immediately preceding* animal-viewing experience; bin must be within a short walk of the viewing point, on/adjacent to a path, no power needed. Widely reported as the single largest revenue category -- "1.5-2.5x greater than entry-fee profits" in successful zoos. Selling bred offspring for cash on the Franchise market is a further source (example cited: ~$6,000/sale). [single source]

_source: deep-research cascade P1 2026-08-21 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

### Cash -- spending

Construction, staff wages, power/water infrastructure, cash-tier animal purchase, loan repayment. Research Centre costs $4,000 to build.

### Conservation Credits (CC) -- fully separate currency, never merge with Cash

Earned primarily by **releasing animals to the wild**, scaled by welfare/star rating, genetics/breeding quality, remaining longevity, and real-world IUCN status -- Endangered species pay far more than Least Concern (example: Common Warthog ~10-15 CC vs. well-bred Cheetah >=120 CC; Lions only ~500-1000 CC despite Endangered status because the online market is saturated with lion breeders).

Spot-checked example payouts (approximate, version-sensitive, not exact formula inputs): Common Warthog ~10-15 CC; Nile Monitor up to ~1,000 CC/breeding-pair cycle, ~2,000 CC/5 in-game years with strong longevity/fertility genetics; Red Ruffed Lemur ~45 CC; Cheetah/West African Lion ~500-900+ CC (gold-tier genetics), up to 700-1000+ CC for elite big-cat genetics per one source; African Elephant cited as high as ~1,200 CC per individual but 22-month gestation + 15-year maturation makes it CC-inefficient per unit time; Albino/melanistic color-morph lions 1,200-1,500 CC -- a substantial premium purely for the rare coat variant, independent of the four bred stats.

> **Cross-system dependency** -- see `dependencies.md` DEP-006: African Savannah Elephant's high per-release CC value vs. its 22-month gestation + 15-year maturation making it CC-inefficient per unit time.
> **Cross-system dependency** -- see `dependencies.md` DEP-007: Albino/melanistic color-morph lion 1,200-1,500 CC premium (West African Lion most-cited target).

**[Contradicted across sources]** whether CC payout is strictly tiered by IUCN status category, or whether genetics/age/per-pair breeding efficiency dominate. The more defensible synthesis: conservation status sets a baseline/multiplier, but genetics, age, and per-pair breeding efficiency dominate the realized payout -- status alone does not determine CC value. (Not part of the P3 gap-fill scope -- still open.)

**Resolved at P3 (2026-08-22): cash-purchased animals ARE subject to a birth-origin gate, not a blanket purchase-currency ban.** Supersedes the P1 contradiction. Community consensus (3 independent commenters, r/PlanetZoo): a cash-purchased animal cannot itself be released/sold for CC directly, but once it breeds, its zoo-born offspring can be released to the wild or traded on the market for CC -- *"you can buy animals for cash and then release or trade their offspring for cc once they're adults."* The official Frontier guide corroborates the general release-for-CC mechanic without explicitly stating the cash-origin restriction, and doesn't contradict this finding -- the restriction reads as a Franchise-mode market UI gate (only zoo-bred stock selectable for release/trade, not market-purchased individuals directly).

**Resolved at P3 (2026-08-22): no discrete CC-tier system exists -- confirmed false, not merely unconfirmed.** Supersedes the P1 "[Contradicted / not found]" flag. Multiple sources agree pricing is continuous/per-individual. A 2019 Frontier Forums thread gives a range example: *"a high value tiger could range from 750-1000 conservation credits whereas a high rated peafowl could range from 25-30 conservation credits."* The senginous datamining guide explicitly documents the continuous formula (Appeal x Genetics x Fertility x Longevity x Age/Star-rating all modulate price within a species). No patch notes or help-centre article mention a discrete tier system.

Franchise-exclusive CC extras: daily login bonus (100 CC/24h), greeting 5 visiting players' avatars (+100 CC), selling animals on the online market, weekly community challenges. **Do NOT apply in Challenge mode** (offline/solo market). Research is cash-funded (Research Centre + vet time), NOT a CC source.

**Spending**: buying CC-tier animals on the Franchise market; founding a new zoo within a Franchise costs 100 CC (offset by the daily-login freebie). Market pricing is player-set (not dev-fixed): community convention of roughly +50%/+100%/+150% over baseline for bronze/silver/gold-medal animals. [single source]

_source: deep-research cascade P1 2026-08-21, birth-origin-gate and no-discrete-tier findings resolved by P3 gap-fill 2026-08-22 (items 6-7) · capture: web_fetch · confidence: medium (P1 baseline) / high (P3-resolved sub-claims: birth-origin gate at 3 corroborating sources, no-discrete-tier at 2 corroborating sources incl. official forum) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

### Loans

Loan availability/type is set **per Career scenario**, not universal (examples: 20k/40k/80k starting-cash scenarios; a scenario requiring loan repayment as an explicit objective). Loans can be repaid via a fixed annual installment or paid off early with no penalty, and can be re-taken repeatedly. No source ties loan eligibility/size/interest to a zoo-rating threshold. The "Loaner" achievement requires $50,000 cumulative repayment as a fixed total, unrelated to rating.

**Interest -- resolved at P3 (2026-08-22): no single universal rate; each loan/scenario sets its own fixed percentage.** Official source (one.planetzoogame.com Beginner's Guide, "Finances -> Loans"): *"The number and type of loans available are set per scenario... Each year, the outstanding amount on the loan increases by a fixed percentage as the interest on the debt builds."* This is ground truth and supersedes the P1 "no numeric rate found" gap -- the correct model is per-scenario fixed %, not a single game-wide rate. Concrete observed values corroborated across 4 independent community sources: a $20,000 loan at **5%**, a $50,000 loan at **10%**, and a $5,000 loan at **10%** (1-4yr term) -- illustrative examples of the per-scenario rate, not a universal table.

**Sandbox originally had NO loans** -- added in patch 1.12.3, alongside a full Economy Settings panel (enable/disable cash, disable staff quitting, disable happiness/energy decay, disable barrier decay, infinite power, self-cleaning water).

_source: deep-research cascade P1 2026-08-21, interest-rate mechanism resolved by P3 gap-fill 2026-08-22 (official Frontier Beginner's Guide, ground truth) · capture: web_fetch · confidence: high (mechanism) / medium (illustrative rate examples) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

### Ticket pricing

No mathematical formula found anywhere. Consistently reported: a qualitative guest-perception signal (too cheap->fair->good->too expensive) gates shop/kiosk pricing too, not just entry -- pricing perceived as unfair suppresses downstream shop/donation spending even among guests who do enter. Community heuristic (not dev-confirmed): raise price in ~$5 increments until guests start complaining, then back off to "good" rather than "fair" -- happier guests spend more downstream than the marginal ticket-price gain. Rough guest tolerance ratios cited: ~2x material cost for food/drink, ~4x for souvenirs. [single source]

### Shops and donation bins

Shop counter variety is **patch-gated, not rating-gated**: 8 food/drink counters added update 1.8; 8 more food/drink + 3 souvenir + 1 info counter added update 1.10; full modular Souvenir Shop building added update 1.16. Per-item price customization exists (extras like ice/ketchup raise willingness-to-pay); a "synchronize prices across all shops" toggle exists in Facilities. Donation bins are a single facility type, not tiered -- effectiveness is purely placement + preceding guest-experience quality.

_source: deep-research cascade P1 2026-08-21 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

### Per-item shop pricing -- a worked community example

No dev-published price table exists. One widely-circulated community price set is reproduced below as a **starting point to tune from**, not an optimum -- its author explicitly calls it unoptimised and still in progress.

**Conditions it was derived under** (the numbers do not transfer cleanly outside them): a zoo of 8 exhibits and 6 habitats at ~2,000 guests; entry priced at **$30 adult / $15 child**; several ATMs placed; all condiment extras enabled; ongoing sale of exhibit offspring as a parallel income stream. Shop placement and guest count both move the result.

| Shop | Per-item prices (in listed order) |
|---|---|
| Chief Beef | 12.95 / 10.25 |
| Hotdog Squad | 12.90 / 8.90 |
| Pizza Pen | 7.90 (all items) |
| Cosmic Cow Ice Cream | 8.65 (all items) |
| Street Fox Coffee | 9.50 / 9.50 / 9.50 / 8.50 |
| Pipshot Juice | 6.10 (all items) |
| Pipshot Water | 4.95 / 6.50 |
| Gulpee Soda | 5.95 (all items) |
| Gulpee Slush | 7.60 (all items) |
| Gulpee Energy | 5.95 (all items) |
| Just a Memento | 13.50 / 8.50 / 13.00 / 17.00 / 35.00 / 70.00 |
| Information | 2.80 / 17.00 / 35.00 / 70.00 / 4.00 |
| Toilets | 1.15 |

**Tuning rule the author pairs with the table**: any shop showing little or no queue is overpriced -- drop that shop's prices by 15c at a time and re-test. This is the same feedback loop as the ticket-price heuristic above, run per-shop.

_source: manually-collected community research pass 2026-09-16 (Steam Community discussion "Make $100,000 every 30 minutes (approx)" by MrHappy) · capture: manual-clipping · confidence: low (single-source community heuristic tuned to one specific zoo configuration; author self-describes the set as unoptimised) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

### The finance report -- the six categories the game itself reports

The in-game finance panel breaks the zoo into six lines, and they are the natural unit for any external budgeting: **Purchases** (every animal moved plus all construction, itemised), **Ongoing Expenses** (upkeep and recurring payments -- power, wages and animal food are typically the largest), **Taxes** (scenario-dependent; several types exist and many scenarios have none), **Income** (all earnings by source), **Cash Flow** (income minus expenses), and **Total Profit** (net; the number that should read green).

Profit legitimately oscillates month to month -- an arrow alternating red and green is normal business fluctuation, and only a sustained red run signals a real problem.

### Opening economy playbook -- one experienced player's practice

A community opening sequence for Franchise, recorded as one author's practice rather than an optimal line:

- **Starter species: Indian Peafowl.** Cheap to buy, large litters, a highly flexible temperature band (3-42 degC), low land requirement, and eligible for an interactive (walkabout) habitat which draws more guest attention. Fencing can be **hedges at $0.80**, which need no plant coverage. A single mirror mobile plus a slow feeder covers enrichment at the start. Downside: their habitat is hard to keep clean. Buy for cash rather than Conservation Credits early, prioritising fertility and immunity over a perfect stat line.
- **Butterfly engine (Grasslands Animal Pack only).** A **walkthrough exhibit costs $9,000** up front. Butterflies die fast but breed heavily; buy 2-4 of each sex ignoring stats, set the exhibit to ~25 degC, then use the exhibit's **Management** panel: enable "manage population", set the per-sex maximum to 10 or higher, and set processing to "store in trade center" so surplus flows to sale automatically. Place it near the entrance or the first habitat so guests actually reach it.
- **Education as a paired income and rating lever.** Speakers covering half a path without overlapping raise education across the zoo; a base tour touching at least three habitats priced at **$3-5** attracts guests while earning -- short tours need no break stops. Both require paying an educator, so add them once profit is already stable.

**Cross-mode caution**: this playbook assumes Franchise. See the cross-mode table below before transplanting any of it.

_source: manually-collected community research pass 2026-09-16 (Steam Community guide "Saturn's Comprehensive Guide to Planet Zoo" by leemonshark; finance-report categories from one.planetzoogame.com Beginner's Guide and Steam Community guide "Planet Zoo: The Comprehensive Guide") · capture: manual-clipping · confidence: medium (finance-report categories corroborated by the official help-centre) / low (opening playbook is one author's practice) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

### Cross-mode economy differences (critical -- never merge these)

| Mode | Cash | Conservation Credits | Loans | Market |
|---|---|---|---|---|
| **Career** | Fixed, scenario-specific starting cash (20k/40k/80k examples found) + scenario yearly-profit/loan-repayment objectives | Standard rules, scoped to that single zoo | Loan type/count set per scenario | Single-zoo; market deliberately restricted to what the scenario needs, independent of rating |
| **Franchise** | NOT shared across zoos -- each new zoo starts independently (reported at $40,000); only indirect cash "transfer" is buy-low/sell-high through the shared trade center | Shared across ALL zoos (pooled) -- research is also franchise-wide; new zoo costs 100 CC; 100 CC/24h login bonus | Available; unspecified annual interest %; penalty-free early payoff | Online, player-driven -- prices float on live supply/demand, refresh ~10-15 min/species; only mode with login/greeting CC bonuses |
| **Challenge** | Fixed $40,000 start every time | Fixed 300 Conservation Points start every time | Not separately documented | Fully offline, AI-run -- looks live but isn't |
| **Sandbox** | Unlimited by default (toggleable via Economy Settings panel, patch 1.12.3+) | Unlimited by default (same panel) | Absent until patch 1.12.3, then opt-in | Toggles: no staff quitting, no happiness/energy decay, no barrier decay, infinite power, self-cleaning water; all research pre-completed |

**What guides get wrong**: nearly all beginner guides describe cash-earning tactics without flagging that Franchise cash is per-zoo while CC/research are franchise-wide -- a second zoo starts flat broke regardless of the first zoo's wealth. No guide gives a numeric loan interest rate. Challenge looks live (has a "market") but is actually a fully offline AI-run economy.

_source: deep-research cascade P1 2026-08-21 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Staff

### Cross-cutting mechanics

**Training**: all six roles (Keeper, Vet, Caretaker, Mechanic, Security, Educator) run 1->5 stars (Trainee/Capable/Skilled/Expert/Master); arranged via the staff info panel but only takes effect on the staff member's next staff-room rest, not instantly. Cost ~$40-200/level. Raises happiness, efficiency, resilience, work rate -- and salary expectations. New 1-star hires start ~$1,100/month; no source gave a full $-per-star table for any role.

**Work zones**: created via Zoo Management -> Staff -> Work Zones; drag-select buildings/habitats, assign staff. A habitat's keeper/vet/mechanic must share its zone; unassigned staff free-roam to whatever's been neglected longest. **Vendors and Caretakers cannot be given path-segment zones** -- only whole facilities -- a long-standing community request; workaround is anchoring caretaker routes with toilets/ATMs/food courts. Most guides imply uniform zone granularity across roles when caretakers/vendors functionally lack it.

**Unlock chains**: Mechanic Research (Workshop + working mechanic, one occupant at a time) gates new shop types, scenery/building themes (and their staff-building variants), barrier types, climbing/shelter/habitat blueprints, and solar/wind power. Vet Research (Research Centre + one vet at a time) gates enrichment tiers, "fun facts," food level, education-rating bonus, and breeding-research %.

_source: deep-research cascade P1 2026-08-21 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

### Keepers

Clean habitats, feed/water, report illness/injury, remove carcasses (lower priority than vets). Needs a Keeper Hut in-zone alongside a staff room and habitat(s).

**Staffing ratios [Contradicted across sources]**: figures range from "1 keeper per habitat" up to "6-8 exhibits per keeper," "4-5 enclosures/keeper," "1 keeper per 7 animals." Convergent point despite the spread: animal count, travel distance (hut/staff-room/habitat proximity), and keeper training level drive efficiency far more than any fixed ratio -- distance is repeatedly named the dominant factor.

### Veterinarians

Treat illness/injury, capture escapees, remove carcasses, run Research Centre research, transport animals (lowest priority). **Only one vet can occupy a Research Centre at a time** -- a hard bottleneck; three simultaneous vet-research projects require three separate Research Centres.

**Escaped-animal handling**: free auto-dispatch (tranq -> box -> return) with travel latency, OR a flat **$1,000 "Emergency Capture"** for instant resolution regardless of species -- frequently omitted from beginner guides.

Disease mechanics: welfare/immunity drive self-recovery odds; a shared dirty water source across habitats is a specific cross-habitat outbreak vector; surviving a disease grants permanent immunity to it; vet disease-research reduces catch-chance, recovery time, time-to-death, and zoo-wide outbreak likelihood. Exhibit-animal and habitat-animal research appear to run as separate vet-research tracks (exhibit L1 = +15% breeding research + enrichment L1) -- most casual guides collapse this into one bucket. [single source]

_source: deep-research cascade P1 2026-08-21 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

### Caretakers

Transport boxed animals (highest priority), clean paths, empty bins, maintain toilets. No dedicated hut-equivalent facility. **The clearest work-zone exception**: cannot get path-segment zones, only whole buildings; some experienced players leave them fully unzoned to avoid coverage gaps. Reported bugs: won't enter walk-through habitats to clean; raised walkways cause pathing problems. Litter tip: clusters of 3 bins every ~20m outperforms scattered single bins for coverage-per-caretaker. [single source]

### Mechanics

Repair habitats/barriers/power/water/vandalism; exclusive role for Workshop research. Items need staff-path connectivity or they're never serviced -- a common beginner trap.

**Repairs are schedule-driven, not continuously automatic**: each item has a maintenance-cadence dropdown (monthly/3-month/6-month/annual); too-infrequent scheduling is a frequent cause of "mechanics aren't doing their job" complaints, alongside missing path connectivity and mechanics locked into research-only mode. Reported priority ordering: Habitat > Power > Water > Station > Vandalism.

### Security guards

**Two-part mechanism most guides collapse into one**: cameras are pure detection/deterrence (identify offenders, don't stop them); guards must physically reach the flagged individual to resolve the crime -- full camera coverage with no nearby guard still permits crimes. Higher-trained guards have better stamina/catch-reliability. The dominant crime-reduction lever across all sources is guest happiness itself, with security secondary. Security specifically protects bench/education-board/speaker durability from vandalism -- a broken education board stops contributing to the education economy until repaired, a direct security->education link most guides miss. [single source] Common placement: 2-3 guards at the main entrance (fleeing offenders must pass through it) + full camera coverage. [single source]

### Educators

Run Animal Talks at scheduled talk points, traveling up to 3 months ahead of schedule; sometimes feed the animal during the talk. No dedicated "Educator Hut" found in any source (gap).

**Each guest can only "learn" a given animal once** -- repeat exposure gives no further gain, which is why animal-agnostic general boards (guests can stack multiple) outperform redundant animal-specific content; one well-placed Animal Talk reportedly outperforms many boards. Education output scales with the featured animal's vet-research level, tying Educators directly to vet progress. Educators (added update 1.4.1) need ~3 months rest between talks at the same spot; reported to stress some species even with mitigation; "Do Not Disturb" signs mitigate stress. Educators "don't scale well to large zoos" per community consensus (guests can't reliably reach a talk in time).

_source: deep-research cascade P1 2026-08-21 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Guests & Facilities

### Guest needs -- full list

**Hunger, Thirst, Toilet/Bathroom, Energy, Education, and an aggregate Happiness/Satisfaction bar.** No separate "nausea"/"immersion" need exists in the base game -- confirmed across 4 languages as a complete list, with Happiness as the derivative aggregate rather than a 7th independent input.

Restored by: food shops (hunger), drink shops/coolers (thirst -- depletes faster in heat; some foods like salted fries actively *increase* thirst), toilets (bathroom), benches/rides/some drinks (energy -- also temperature-linked, not just distance-linked), education boards/speakers/educators/research (education). Unmet needs -> "stressed" guests -> fast happiness drop (toilet is called the sharpest single penalty) -> guests leave, spend less, and past a threshold litter/vandalize/spawn protesters. Benches only function when placed directly on a path tile, not adjacent on grass.

_source: deep-research cascade P1 2026-08-21 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

### Education -- a resolved cross-source contradiction

**English/German sources** treat Education as a normal happiness-need input, same tier as hunger/thirst. **French/Spanish wiki pages plus one English forum thread** state Education has no direct effect on the Happiness bar -- instead it scales guest spending/donation willingness, a distinct multiplier.

**Resolution**: patch 1.2 explicitly split Education from Happiness and added a guest-spending multiplier (official 1.2 patch notes: "Education is now split from happiness and now offers a spending bonus multiplier"). Sources describing Education as a happiness sub-component reflect pre-1.2 behavior and are stale against the current 1.20.2 build. **The current correct model is Education -> spending multiplier, NOT direct happiness input** -- likely the single most common oversimplification found across mainstream guides. No source establishes a direct Education -> Conservation Credits pipeline; CC runs through the separate release/conservation-action mechanism.

_source: Frontier official 1.2 patch notes, corroborated by the Zoo Rating research pass · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

Education Boards/Info Signs: cheapest, per-species assigned, 1-2 per habitat typical. Speakers: per-species, adjustable radius; overlapping speaker radii broadcasting different species actively reduces/confuses guest education gain in the overlap zone -- a mechanism most beginner content skips. Conservation Education Boards cover 10 topics; reading all 10 gives a large bonus; board location doesn't matter, only that the guest stops to read. [single source] Vet research on a species raises education value delivered by boards/speakers for that species, and separately feeds the zoo's Education Rating via "vets in advanced research" + Zoopedia unlock level.

### Guest pathing and viewing quality

Food/drink placement actively routes guest traffic toward the less-traveled fork. Congestion fixes reported: paired-boulevard main paths rather than one wide path, viewing areas physically separated from through-traffic, shops in off-path alcoves, oversized entrances (a mandatory 100%-of-guests choke point), and secondary entrances to relieve load.

**Guest AI targets one specific animal at one specific spot, not "the habitat" as a whole** -- a guest can file a "bad view" complaint at an excellent viewing platform if the specific animal it fixated on happens to be behind a hill/shelter, even while conspecifics are in full view nearby -- widely cited as a source of persistent, seemingly-irrational complaints. Viewing-distance thresholds are per-species tiered (good/neutral/bad); one documented example -- common peafowl: good <12m, neutral 12-24m, bad >24m. No comprehensive per-species table was reachable.

Mitigations reported: raised viewing platforms, half-circle two-way-glass bays, lowering interior terrain below path level, "vista points" placed where animals congregate, positioning enrichment/water/feeders to pull animals toward or away from viewing areas, blocking unintended sightline path access, moderate (not excessive) foliage.

_source: deep-research cascade P1 2026-08-21 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

### Shops

Types: food, drink, souvenir, vending machines. Food/drink sell ~2x material cost, souvenirs ~4x, with happy guests paying above baseline. Stock is climate-flagged (ice/cold drinks for hot biomes, coffee/warm food for cold biomes). Vending machines satisfy needs less effectively per use than staffed shops -- a real mechanical trade-off. Souvenir shops require a hidden "modular shop" foundation piece beneath counter/shelving, or a "not connected" error blocks function. [single source] Placement consensus: cluster shops near popular habitats but spread across several small clusters (not one zone) to avoid queue congestion; rough ratio guidance of 2 drink shops per 1 food shop since thirst depletes fastest. Food/drink shops need both power AND an assigned vendor -- no vendor, no sales regardless of stock. No official restroom-per-guest ratio found; community rule of thumb is "add a toilet block around 500 guests." Paid toilets measurably reduce happiness more than the price seems worth. [single/2 sources]

### Transport rides

Research-tree progression (per one synthesized source, unverified against a second): Boat Ride (L1) -> Suspended Gondola (L2) -> Steam Train (L3) -> 4x4 Adventure Tour (L4); Monorail's place in this chain is unconfirmed. Built as contiguous track; Loop mode required for >2 stations; ticket price set **per station-to-station segment**, not flat fare; guests reportedly tolerate $10+/segment in an established large zoo. **Staff cannot ride the transport rides themselves** -- a guest-facing rule that matters for zoo layout, since a staff-only area reachable only by ride triggers zone-disconnection warnings; players build hidden staff tunnels as a workaround. Rides restore guest Energy (alongside benches/drinks) and generate ticket revenue; no evidence of a separate "novelty" happiness bonus beyond energy restoration. [Hypothesis -- unverified]

### Guest happiness -> Zoo Rating

Guest Happiness Rating = live rolling average of currently-in-zoo guests' % happiness, not cumulative/historical -- enables a known min-max exploit: closing the gates to fully empty the zoo, fixing issues, then reopening purges the lower-happiness "old" population and produces a fast rating jump. 5-star Guest Happiness threshold reported at **80% on Easy, 85% on Medium/Hard** (official help centre). Negative modifiers: unmet needs, protesters, litter, vandalism, overcharging, staff-facility "negative radius," stressed/poorly-cared-for animals, long queues. Positive: good views of healthy animals, scenery, souvenir purchases, fair pricing, (contested) education.

**Mode differences**: Sandbox exposes explicit "Maximise guest happiness" (forces ceiling) and "Freeze guest needs" (locks bars) toggles -- bypassing the simulation entirely. Franchise is the only fully-online mode; Sandbox/Career/Challenge are offline. Career runs guest-need mechanics fully live by default, with real scenario objectives tied to guest-happiness thresholds under genuine resource constraints.

_source: deep-research cascade P1 2026-08-21 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Genetics & Breeding

### Trait list

The game tracks **four bred genetic stats**: **Size**, **Longevity**, **Fertility**, **Immunity**. Size and Longevity are additive/continuous (offspring trend between parent values, shift slowly generation to generation, respond predictably to housing/husbandry quality). Fertility and Immunity are volatile -- offspring can land far from either parent's value.

**Appeal/attractiveness is a separate axis, not one of the four bred stats.** Driven by (a) a fixed per-species base "species appeal" number (e.g. African Elephant/West African Lion/Western Lowland Gorilla top the list at 6750; Common Warthog/Greater Flamingo/Indian Peafowl bottom out near 750) and (b) a per-animal star rating driven by welfare/food quality/zoo tenure/popularity. Species appeal is higher in juveniles than adults. **Mainstream guides routinely describe "genetics" as if appeal is a fifth bred trait alongside size/longevity/fertility/immunity -- it isn't.**

> **Cross-system dependency** -- see `dependencies.md` DEP-005: the 6750 top-tier species-appeal base is tied among exactly three species (African Savannah Elephant, West African Lion, Western Lowland Gorilla).

_source: deep-research cascade P1 2026-08-21 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

### Underlying mechanism -- codon system

**[Single source -- verify, corroborated independently twice]**: each animal carries 12 pairs of genetic codons -- 6 governing Fertility, 6 governing Immunity -- one codon per pair inherited from each parent, offspring receiving a random combination per pair. The genetics tab shows each stat as a percentage/range with color-coded (green = favorable) indicators; a genetics comparison tool previews probable offspring ranges before pairing two animals. "Diversity Genes" (heterozygosity rewarded) appeared in one source only; not independently corroborated. [single source]

### Inbreeding mechanics

**Detection**: the game calculates shared-ancestor-DNA percentage between potential mates -- full siblings share 100%, mother/son (or father/daughter) share 75%. **Penalty**: inbred offspring have elevated odds of poor Fertility/Immunity and can be rendered effectively infertile; genetically compromised animals sell/trade/release for less.

**The game's blind spot**: cousins, aunts/uncles, and nieces/nephews are **NOT** flagged by the game's inbreeding warning UI, because the game does not track ancestry beyond one generation back. Two cousins bred together will show no inbreeding warning at all, yet their Fertility/Immunity ranges can still extend deep into negative territory -- a real mechanical gap between "the UI says it's fine" and "the underlying math says it isn't." Most mainstream guides only warn about parent/child and sibling pairings and don't mention the cousin blind spot.

Generations to dissipate: one community estimate states ~5 generations for an inbreeding penalty's effect to fully clear from a lineage. [Hypothesis -- unverified]

_source: deep-research cascade P1 2026-08-21 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

### Contraception

Toggled per-animal via a pill icon/slider on the animal's info panel. Animals on contraception still pair/mate socially but produce no offspring; the age-indicator turns red and the animal is labeled "infertile" while active. Effect is immediate and reversible unless already pregnant. Practical use: apply contraception to all offspring of a breeding pair by default, lifting it only on individuals intended to breed forward -- the primary in-game tool for preventing accidental inbreeding.

### Breeding programs

Requirements: at least one fertile male and one fertile female of the same species, cohabiting, with **overall welfare >= 66%** -- the game reportedly withholds successful mating below that threshold entirely. [single source] Vet research on a species can raise its Fertility stat / breeding-chance multiplier, directly increasing successful conception odds.

### Trading -- distinct from the open Market

Two separate systems: (1) **Animal Market** -- player-to-player, cash- or CC-priced listings, browsable/sortable. Only habitat animals are tradeable -- **exhibit animals cannot be traded**. Deluxe-edition animals only trade to other Deluxe-edition owners. No direct animal gifting -- must go through the market. (2) **Franchise Trade Center** -- internal-only storage shared across a player's own zoos within one Franchise; unlimited storage but reportedly a **30-animal cap on purchases held at once** (storing your own bred/transferred animals isn't subject to this cap). [single source]

_source: deep-research cascade P1 2026-08-21 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Conservation & Research

### Research categories and staff

Three staff roles conduct research, each requiring a **Research Centre** (a powered staff building, path-accessible; a "Large Research Centre" variant exists) with **only one staff member able to use a given Research Centre at a time**.

- **Veterinarians -- Animal Welfare/species research**: researching a species unlocks that species' enrichment toy/food items, better food-quality tiers, a fertility/breeding-chance bump, and a guest-education bonus. Full research to "gold" requires unlocking all of Fun Facts, Diet, Habitat Enrichments, and Food Enrichments for that species.
- **Mechanics -- Habitat & Construction research**: unlocks building materials, barrier types (e.g. Reinforced Glass, Concrete), facility blueprints, utility upgrades.
- **Educators -- Guest Experience research**: unlocks shops, food stalls, educational signage/displays, entertainment items.
- A fourth "Conservation research" role was claimed by exactly one source and not corroborated anywhere else -- treat with real skepticism; every other source describes only the three-role system. [single source]

**Prerequisite**: at least one live individual of a species must be physically present in the zoo before it can be researched. [single source] **Franchise-wide propagation**: research completed in one zoo is shared instantly across every zoo in that Franchise. **Challenge Mode zoos do NOT share this** -- research must be redone independently per Challenge zoo, since Challenge's economy/trading/research runs isolated per-zoo (offline).

_source: deep-research cascade P1 2026-08-21 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

### The release-to-wild CC loop, end to end

1. Breed/raise an animal to non-juvenile, healthy, fertile-eligible, non-elderly status.
2. Push Size/Longevity genetics toward the high end (85-100% cited repeatedly as the practical "good genetics" threshold for high-value species like lions).
3. Release via the zoo management UI; payout = genetics quality + conservation/endangerment status + remaining longevity/age + species-level base value, with a soft cooldown/diminishing-returns penalty on repeated releases of the same species within a short window (existence confirmed by 4 sources; rate/formula given by none -- Hypothesis).
4. CC accrues to a Franchise-wide (not per-zoo) shared pool, usable to buy CC-gated animals in any Franchise zoo or to open a new zoo (100 CC cited).

### Market tiers

The Animal Market has both cash and CC listings, filterable/sortable by currency; the best-stat animals skew toward CC-only listings, with CC cost scaling by stats (one source cites CC prices up to 9,000 CC for top-end animals [single source]). Cash listings exist for a meaningful subset but are scarce/quickly bought up by other players, especially late in the game's community lifecycle. **No discrete numbered CC-tier system exists -- confirmed false at P3 (2026-08-22), not merely unconfirmed** -- every source describes continuous, stats-scaled pricing rather than fixed price bands (see Conservation Credits above for the full resolution).

_source: deep-research cascade P1 2026-08-21 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Unlock Chains (animal & feature acquisition -- general pattern)

**Partially resolved at P3 (2026-08-22).** P1 flagged this as the largest documented gap (Fandom's `List_of_Animals`/`Conservation_Credits` pages, plus a community pricing spreadsheet, not fully opened). P3's gap-fill pass found a live community datamining spreadsheet -- **"PZ Animal Husbandry and Planner" by u/senginous** (linked from Steam Guide id 3048155055, updated for Asia Pack/1.20.1, one patch behind current) -- whose "Details" tab carries **Cash min/max price per species** (e.g. Aardvark $1,186-$5,902; African Leopard $3,317-$15,574; African Savannah Elephant $7,449-$22,763; Bengal Tiger $2,405-$16,653), with an explicit conversion note on the sheet: *"Listed in cash using the (Sandbox) conversion of 1 CC = $13. Lowest observed price in Sandbox mode market after buying the 2 median priced animals until the offer expires for the high or low."* [class:datamining, single source] Pricing is confirmed **not** a fixed per-species number -- it's computed per-individual from Appeal (species+age+star rating), Genetics rating, Fertility, and Age, so any "table" is necessarily a min-max range (consistent with the no-discrete-CC-tier finding above). Villanelle's Data Chest does NOT carry Cash/CC cost columns (habitat/compatibility-focused only); Fandom's `Conservation_Credits` page is a stub with no cost table; Steam guide "Thrall's Planet Zoo Spreadsheet Treasure Trove" (id 3410761755) points to a Patreon-gated sheet, inaccessible. **Still open**: an exact CC-denominated (rather than cash-equivalent) per-species table does not exist anywhere in the public community corpus -- this remains a genuine gap, not an access failure. What follows is the confirmed general pattern.

| Mode | Currency | Trading | Research sharing | Animal availability gate |
|---|---|---|---|---|
| **Sandbox** | N/A -- unlimited money, all research pre-completed | N/A | N/A | **All animals unlocked** from the start -- explicit "All Animals Unlocked" toggle |
| **Franchise** | Cash + CC, both usable on the open Animal Market | Player-to-player Market (cash or CC listings) + internal Trade Center across a player's own Franchise zoos | Shared instantly across all zoos in a Franchise once unlocked in one | Rarer/higher-stat animals gated behind CC-priced listings (cost scales with stats, up to ~9,000 CC for top animals); cash listings exist for a subset but depend on another player currently selling one. No confirmed hard "Franchise level" gate |
| **Career** | Primarily cash; CC appears as an objective/scoring mechanic in later scenarios rather than a market-purchase currency | No player trading (single-player, offline campaign) | Not applicable across scenarios -- each of the 12 scenarios is its own save | Per-scenario animal roster tied to biome/theme/story, not a universal unlock chain (see `sections/`). Completing a scenario to Gold reportedly opens fuller species availability for free-building within that same scenario file afterward. [single source] |
| **Challenge** | Cash + CC, same dual-currency Market as Franchise | Market exists but runs fully offline/isolated per zoo -- listings regenerate on a timer rather than via real player supply | Not shared -- research redone from scratch in each Challenge zoo | Same cash/CC split as Franchise, but supply-gated by the offline market's own regeneration timer |

**Specific confirmed data points:**
- **Exhibit-only animals cannot enter the Trade/Market system at all** -- their unlock chain is purely research/cash-purchase for exhibit placement, with no CC-release or trading path -- a structurally simpler, dead-end chain compared to habitat animals.
- **Color-morph variants (albino, melanistic) are NOT a separate market-tier mechanic** -- same species/same acquisition chain as the standard morph; once bred (a genetic-mutation outcome, not a purchasable trait) they command a large price premium on both cash and CC listings. Several guides write about "getting" albino animals as if separately unlocked -- it's a breeding outcome, not an unlock gate.

_source: deep-research cascade P1 2026-08-21 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_

(Spoiler-classification note: this section describes mode-level unlock mechanics in the abstract, not any specific scenario's content -- a defensible case exists for `spoiler: none`, but tagged `progression`/puzzle-tier 1 per the corpus's err-stricter default since the source brief tagged the whole Unlock Chains chapter `spoiler: progression (mode/scenario gates)`.)

## Building & Construction

### Piece-by-piece building model

Construction is fully piece-by-piece: individual planks, stones, glass panels, and other components are placed and manipulated independently. Objects split into two placement classes: **grid-based** items, which snap to a fixed grid and can't be freely repositioned off it, and **decoration objects** (marked with a white background in the object browser), which allow full free placement. The lower-right interface panel exposes build-time configuration (angle snap, path width, path/barrier length, curvature, window settings) that persists across successive piece placements. Related pieces can be grouped for easier manipulation (shift-click multiple objects, then use the group icon).

### Blueprints -- save/load

A completed multi-piece structure can be saved as a **Blueprint**, collapsing every individual placed component into one placeable object for reuse. Save workflow: select the target structure/habitat's info panel -> "Save as Blueprint" -> "New Blueprint" -> position camera and set time-of-day for the thumbnail -> name it, write a description, tag it -> "Create Blueprint." Mechanic research unlocks additional blueprint types, extra constructible objects, and barrier/habitat-themed construction sets progressively -- the building piece catalogue is partly research-gated, not fully available from the start.

### Steam Workshop integration

A saved blueprint can be uploaded directly from the in-game blueprint browser via "Upload to Steam Workshop." Subscribing to another player's Workshop blueprint auto-downloads it into the local blueprint browser. The Workshop ecosystem ranges from small props/nature dressing to entire pre-built habitats and full zoos.

### Terrain tools

Documented tool set (all modifiable by brush intensity/size): **Push/Pull** (raise/lower elevation), **Flatten to Foundation** (flattens all terrain within the brush circle to the foundation's base height), **Flatten to Terrace** (stepped flattening, preserving verticality -- useful for hillside buildings or large wading-depth water features), **Smooth** (turns stepped/jagged terrain into a continuous ramp), **Roughen** (inverse of Smooth), **Terrain Stamp** (five preset shapes for adding/subtracting terrain volume in one action). Practical technique: low intensity (10-15%) for rough elevation changes near a building footprint, then switch to the leveling tool for the final surface -- avoids overshooting with a single high-intensity pass. [single source]

### Water tools -- the physics caveat

Rivers, lakes, and waterfalls are placeable as scenery/terrain-integrated water bodies. **Important trap**: Planet Zoo's water is a visual-effects system, not a simulated fluid-dynamics system -- there is no calculated water drainage or flow between elevation levels. "Waterfalls" are achieved via water-spray scenery/particle objects layered onto sculpted terrain, not by the engine computing water flowing downhill. This matters directly for welfare mechanics: water depth for animal purposes is a terrain-height/painted-water-surface property, evaluated independently of whatever decorative waterfall/flow effects are layered on top.

### Path system

Two categories: **Guest Paths** (usable by guests and staff) and **Staff Paths** (staff-only) -- Staff Paths route keeper/mechanic traffic without funneling guests through the same route. Path width/length are adjustable at build time; wider paths cost more but support higher throughput. **Path-required-for-access rule**: the Zoo Entrance must connect via guest path to every guest-reachable area, including habitats -- a walk-in habitat is inaccessible unless a continuous guest-path chain runs from the entrance. **Habitat/path adjacency for Walkabout habitats**: guest paths run *through* the barrier via guest gates at entry/exit -- mechanically different from a habitat merely viewed from an adjacent path, which needs no gate, just an unbroken barrier with viewing windows. Capacity-control technique: a single guest gate (rather than multiple entries) caps how many guests are inside a Walkabout habitat at once, since guest crowding inside degrades the contained animals' welfare. Common troubleshooting: "guests won't enter my habitat" usually means either the path chain to the Zoo Entrance is broken somewhere upstream, or the species is flagged too dangerous/undesirable for guests to approach regardless of path correctness.

_source: deep-research cascade P1 2026-08-21 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Game Modes

| Mode | Description | Economy/goals |
|---|---|---|
| **Career** | Story-driven, 12-scenario campaign renovating a series of named zoos (Goodwin House -> Bernie Goodwin Memorial Zoo), teaching systems progressively. Full scenario detail in `sections/` (spoiler-gated). | Fixed per-scenario Bronze/Silver/Gold star objectives; objectives can "uncomplete" if not maintained; loan type/amount and starting cash are scenario-specific; **no hard fail/game-over state exists anywhere in Career** -- bankruptcy does not trigger a game over. |
| **Franchise** | Persistent network of the player's own zoos, played online, with a global player-driven animal market. | Conservation Credits and research are **shared across all of a player's Franchise zoos**; **cash is NOT shared** -- each new zoo starts independently ($40,000 reported). New zoo costs 100 CC; daily login grants 100 CC; weekly Community Challenges available. Only fully online mode. |
| **Challenge** | Single zoo, offline, same full economic simulation as Franchise. | Fixed $40,000 cash + 300 Conservation Credits start every time; animal market is present but AI/computer-run rather than player-driven -- looks live but isn't. No cross-zoo sharing. |
| **Sandbox** | Free-build creative mode. | Unlimited cash/CC by default; individually togglable Economy Settings panel (added patch 1.12.3): enable/disable cash, disable staff quitting, disable happiness/energy decay, disable barrier decay, infinite power, self-cleaning water, loans (absent from Sandbox until 1.12.3). All research pre-completed by default. |

Difficulty (Easy/Medium/Hard) is chosen **per scenario launch, not once for the whole career** -- confirmed by forum posts describing players re-doing individual scenarios "for the hard achievement" one at a time. Hard specifically adds refund availability and enrichment-boredom mechanics not present on Medium/Easy, and affects welfare decay/recovery pacing (see Animal Welfare above) plus guest happiness/refund behavior and staff fatigue.

_source: deep-research cascade P1 2026-08-21 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## DLC Layer

**research-integrated at P3, 2026-08-22.** 20 paid content packs + 1 soundtrack DLC ("You, Me & Other Animals: The Music of Planet Zoo," 17 Sep 2020 -- out of scope, not a content pack). Verified via Steam's official appdetails API + Wikipedia. [Confirmed: 2+ sources, class:official-pr + class:editorial-en]

| # | Title (verbatim) | Release | Type | New species | Achievements beyond base 38 |
|---|---|---|---|---|---|
| 1 | Deluxe Upgrade Pack | 5 Nov 2019 | Deluxe upgrade | 3 | 0 [Confirmed -- Steam stats API] |
| 2 | Arctic Pack | 17 Dec 2019 | Scenery-and-animals | 4 | 0 |
| 3 | South America Pack | 7 Apr 2020 | Scenery-and-animals | 5 | 0 |
| 4 | Australia Pack | 25 Aug 2020 | Scenery-and-animals | 5 | 0 |
| 5 | Aquatic Pack | 8 Dec 2020 | Scenery-and-animals | 5 | 0 |
| 6 | Southeast Asia Animal Pack | 30 Mar 2021 | Animal pack | 8 | 0 [Confirmed -- Fandom Achievements master list] |
| 7 | Africa Pack | 22 Jun 2021 | Scenery-and-animals | 5 | 0 |
| 8 | North America Animal Pack | 4 Oct 2021 | Animal pack | 8 | 0 |
| 9 | Europe Pack | 14 Dec 2021 | Scenery-and-animals | 5 | 0 [Hypothesis -- unverified, not independently checked against the Fandom master list this pass] |
| 10 | Wetlands Animal Pack | 12 Apr 2022 | Animal pack | 8 | 0 [Confirmed -- Steam Community achievements guide] |
| 11 | Conservation Pack | 21 Jun 2022 | Conservation pack | 5 | 0 [Confirmed -- Steam Community achievements guide] |
| 12 | Twilight Pack | 18 Oct 2022 | Animal + scenery | 5 | 0 [Confirmed -- Steam Community achievements guide] |
| 13 | Grasslands Animal Pack | 13 Dec 2022 | Animal pack | 12 (7 habitat + 5 butterflies) | 0 [Confirmed -- Steam Community achievements guide] |
| 14 | Tropical Pack | 4 Apr 2023 | Scenery-and-animals | 5 | 0 [Confirmed -- Fandom Achievements master list] |
| 15 | Arid Animal Pack | 20 Jun 2023 | Animal pack | 8 | 0 [Hypothesis -- unverified] |
| 16 | Oceania Pack | 19 Sep 2023 | Scenery-and-animals | 5 | 0 |
| 17 | Eurasia Animal Pack | 13 Dec 2023 | Animal pack | 8 | 0 [Hypothesis -- unverified, not independently checked against the Fandom master list this pass] |
| 18 | Barnyard Animal Pack | 30 Apr 2024 | Animal pack | 7 | 0 |
| 19 | Zookeepers Animal Pack | 15 Oct 2024 | Animal pack | 7 | 0 [Hypothesis -- unverified -- Fandom access wall hit this pack specifically] |
| 20 | Americas Animal Pack | 15 Apr 2025 | Animal pack | 7 | 0 [Confirmed -- Steam Hunters + base achievement list] |
| 21 | Asia Animal Pack | 25 Jun 2025 | Animal pack | 7 | 0 [Hypothesis -- unverified -- Fandom access wall hit this pack specifically] |

**Zero DLC-specific achievements exist for any pack.** All 38 Steam achievements remain attached to the base app (703080), none to a DLC appid. Confidence varies per pack (see table): 8 packs directly checked against the Fandom Achievements master list or an equivalent per-pack citation; the remaining packs (Arctic, South America, Australia, Aquatic, Africa, North America Animal Pack, Oceania, Barnyard) assert zero with no dedicated per-pack citation surfaced this pass -- treat as medium-confidence, not verified; and 5 packs (Europe, Eurasia, Arid, Zookeepers, Asia Animal Pack) carry the finding as `[Hypothesis - unverified]` because a source-access failure (WebSearch budget exhaustion + Fandom HTTP 402 on every blocked-source-ladder rung) prevented the pass from directly checking those specifically.

**Type-naming pattern** [model observation, not an official Frontier taxonomy]: packs titled plain "___ Pack" bundle new animals **with** a themed scenery/building set (170-350+ pieces) and often a new career scenario. Packs titled "___ Animal Pack" are animal-focused with thinner or no dedicated scenery theme. Conservation Pack is a standalone hybrid. All packs run $9.99/£7.99/€9.99 except the Deluxe Upgrade Pack ($11.99, no scenery, 3 animals only).

**Americas Animal Pack (2025)** is a genuinely distinct SKU independently discovered during the P3 enumeration sweep -- do not confuse with North America Animal Pack (2021) or South America Pack (2020); all three are separate packs with separate rosters.

**Asia Animal Pack (25 Jun 2025) is the final paid DLC pack for Planet Zoo 1.** Confirmed three ways: Wikipedia's DLC table ends here; Steam's DLC appid array assigns monotonically and this pack holds the highest id; Steam's news feed shows a "6 years of Planet Zoo" anniversary post (5 Nov 2025) announcing the team is "hard at work on a sequel," followed by Planet Zoo 2 marketing and a scenery-only Update 1.20.2 (28 May 2026) alongside a "Planet Zoo 2 -- Arriving Oct 13!" announcement. Frontier pivoted directly to the sequel rather than shipping further Planet Zoo 1 packs (a ~14-month content gap explained by the transition). [Confirmed: 3 sources]

**Console/pre-order bonus content mechanism resolved:** Komodo Dragon, Thomson's Gazelle, and Pygmy Hippopotamus are the entire content of the Deluxe Upgrade Pack (Steam appid 1098120) -- confirmed via Steam's own appdetails description. On PC/Steam this is a purchasable paid-upgrade DLC available to anyone regardless of purchase timing, **not** a free unlock. Whether Xbox/PlayStation additionally gate it behind a console-specific pre-order mechanism could not be confirmed (console storefronts unreachable this pass). [Hypothesis -- unverified for console]

**New per-pack mechanics** (species welfare data lives in each species' own `animals/<species>.md` file; this list covers systemic/building additions only):
- **Australia Pack** -- introduced **Challenge Zoo mode** ("Tanami Roadside Zoo"), a franchise-mode objective format layered on an existing zoo.
- **Aquatic Pack** -- formalized underwater/underground guest observation points as a building feature; Underwater Fish Feeder standardized across aquatic species.
- **Europe Pack** -- subterranean camera viewing (European Badger); Goat Climbing Mountain enrichment (Alpine Ibex); Rubbing Pad Bark (Eurasian Lynx). [Corrected 2026-08-22 stitch pass: an earlier draft additionally attributed a "Scarecrow Feeder" item to Fallow Deer/Ibex here -- per-species files show Scarecrow Feeder documented only on Red Deer (base-game, free Anniversary Update addition, not Europe Pack), while `animals/european_fallow_deer.md` and `animals/alpine_ibex.md` do not corroborate it; removed as unsupported by the corpus's own entity data. See `dependencies.md` Corpus inconsistencies.]
- **North America Animal Pack** -- 5 new enrichment items (Beaver Pool, Restraint Feeder, Piñata Zebra/Pronghorn, Prey-Scented Sack, Underwater Plant Feeder).
- **Wetlands Animal Pack** -- shipped alongside free base Update 1.9 (Roaming Educator staff NPCs, first-person "Explore Cam," customizable exhibit water, new bathing behavior for capybaras/macaques) -- these are free-update additions, not DLC-gated; `spoiler: none`.
- **Conservation Pack** -- renewable-energy (solar/wind) power option; "foster plant diversity" biodiversity mechanic tied to the pack's welfare-over-profit scenario framing. [Single source - verify - class:official-pr]
- **Twilight Pack** -- Egyptian Fruit Bat is the game's first flying-creature exhibit animal, in an all-new Walkthrough Exhibit; new red fox coat/color-morph system (silver, black, white, cross, piebald); bouncing pumpkin ball enrichment. **The pack's marketed "red-light night viewing" mechanic was researched and found NOT to exist** -- no source (official description, dedicated review, achievement/community-guide ecosystem) confirms a night-vision mode or day/night visual system; treat as a negative finding, not an under-researched gap. [Confirmed: 2 sources]
- **Grasslands Animal Pack** -- the game's ONLY multispecies exhibit (5 butterfly species cohabit one Walkthrough Exhibit); armadillo hind-leg rearing animation; animated caracal ears.
- **Tropical Pack** -- Brown-Throated Sloth is the game's second Exhibit/Walkthrough-Exhibit mammal (after Twilight's bat) and the first non-flying walkthrough-exhibit mammal.
- **Oceania Pack** -- Spectacled Flying Fox is the second bat species (after Egyptian Fruit Bat); first DLC pack with more than one bird species.
- **Eurasia Animal Pack** -- Hermann's Tortoise is the game's first (and only, per wiki) Grassland-biome exhibit; a 1.17 patch note raised its exhibit population cap from 5 to 20.
- **Barnyard Animal Pack / free Update 1.17 -- Animal Encounters (petting-zoo mechanic).** `spoiler: none` -- shipped as part of the FREE Update 1.17, NOT gated behind the paid Barnyard DLC; works on qualifying species from the base game and other DLC packs too (Frontier's own announcement names Quokka/Oceania Pack, Llama/South America Pack, and Ring-Tailed Lemur/base-game as eligible alongside the 7 new Barnyard species). Mechanically: applied as a toggle on an existing Walkthrough Habitat; requires a guest gate, no dangerous animal present, at least one interactable/suitable species, and at least one Hygiene Station (hand-washing scenery item); guests leave the path to wander/interact, then want a Hygiene Station afterward or happiness drops. The in-game Zoopedia shows a per-species interaction tier (can interact / can walk through without interacting / will flee). **A comprehensive published list of eligible species beyond the 10 named (7 Barnyard + Quokka, Llama, Ring-Tailed Lemur) was not located** -- the in-game Zoopedia tag is authoritative per-animal, but no full roster was found. [Single source - verify - class:official-pr on the roster beyond the 10 named] Same patch: animals with "Domesticated" IUCN status (the 7 Barnyard species + pre-existing Bactrian Camel, Llama, Dromedary Camel) can no longer be released to the wild for CC -- sold for cash via Quick Sell instead. [Confirmed: official patch notes]

> **Cross-system dependency** -- see `dependencies.md` DEP-003: North America Animal Pack's 5 new enrichment items, incl. beaver-specific Beaver Pool.
> **Cross-system dependency** -- see `dependencies.md` DEP-004: Europe Pack's per-species enrichment/viewing mechanics (Badger, Ibex, Lynx).

**New DLC-added career/timed scenarios** (character/location detail only -- no Bronze/Silver/Gold objective breakdown was researched at this pass's granularity; this is a lighter-touch capture than the 12 base Career scenarios in `sections/`): see `sections/dlc_scenarios.md`.

_source: Planet Zoo DLC research pass (P3) 2026-08-22, 7 parallel research passes · capture: web_fetch, several rungs via Firecrawl stealth-proxy after direct WebFetch 402'd (see `limitations.md`) · confidence: medium (pack enumeration/dates high; several individual mechanic claims single-source, flagged inline) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: dlc:<per-pack, see table>_

## Sources

- A Beginner's Guide to Planet Zoo (official): https://one.planetzoogame.com/help-centre/player-guides/the-basics
- Frontier official help centre -- Building Your Zoo: https://one.planetzoogame.com/help-centre/player-guides/building-your-zoo
- Planet Zoo Wiki (Fandom) -- Animal Information Panel, Barrier, Path pages [community-wiki, snippet access this session]
- Steam Community "The Comprehensive Guide" (id 1910776223) [forum]
- int-ent.de welfare/illness article [editorial-non-en, DE, translated]
- Frontier Forums -- multiple threads on barrier height, water depth, loan interest, escaped animals [forum]
- TheGamer, ScreenRant, GameRant, dtgre.com, ludo.guide, steamah.com, gameplay.tips [editorial-en]
- gamersky.com [editorial-non-en, ZH, translated]
- GitHub v-duong/PlanetZoo-Genetics (community offspring-probability tool, confirms codon model is community-reverse-engineered)

Full source list per topic preserved in the P1 result file, archived at `research_inbox/p1/_processed/`.
