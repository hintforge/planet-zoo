# Planet Zoo -- Limitations & Blocked Sources

Sources I found that look useful but couldn't fully fetch -- paywalls, Cloudflare, age gates, video-only content, etc. URLs preserved so the player (or another contributor) can open them in a real browser.

## How to read this file
- Each entry: topic, URL, block type, what I could glean, best alternative I did get to.
- Each per-topic file (in `animals/`, `items/`, `sections/`) also lists its own blocked sources at the bottom -- the player rarely needs to come hunting here.
- This file is the catch-all for sources that didn't fit a specific topic.

## Block types
- **paywall** -- content gated behind a subscription or article limit
- **cloudflare** -- Cloudflare bot challenge / 403 / 503 from WebFetch
- **video-only** -- YouTube or other video where the answer is shown visually; no readable text equivalent
- **age-gate** -- content blocked behind age verification
- **cookie-wall** -- popup or consent flow that broke the fetch
- **search-snippet-only** -- search engine returned a snippet but the page itself wasn't reachable
- **dead-link** -- URL was in another source but no longer resolves

## Entries

### Exophase -- achievement list (Stage 0)
- Source: https://www.exophase.com/game/planet-zoo-steam/achievements/
- Block type: cloudflare
- Why I think it has the answer: full achievement list with global unlock %.
- What I could glean before the block: nothing (HTTP 403 at fetch time).
- Best alternative I did get to: the canonical Steam stats page (https://steamcommunity.com/stats/703080/achievements) returned the full 38-achievement list -- captured in `research_briefs/achievement_stubs.md`.

### Planet Zoo Wiki (Fandom) -- nearly all direct access blocked (P1, 2026-08-21)
- Source: `planetzoo.fandom.com` (all pages)
- Block type: cloudflare (returned HTTP 402 specifically -- a bot-paywall variant, not the usual 403)
- Why I think it has the answer: primary wiki for species stats, mechanics detail, the full `List_of_Animals`/`Conservation_Credits` unlock-chain tables, and the Achievements page.
- What I could glean before the block: nothing via direct fetch, `api.php` export/parse, BreezeWiki, or archive.ph -- all four ladder rungs failed across all eight research passes this session.
- Best alternative I did get to: WebSearch snippet exposure and Firecrawl fallback surfaced most qualitative species/mechanics content (captured throughout `animals/`, `mechanics.md`), but at softened confidence (`confidence: medium`, single-source-community-wiki tags throughout) since it's snippet-derived rather than a clean page fetch. The full per-species unlock-chain table specifically was NOT recovered -- see the "[unlock-chain incomplete]" gap below.
- **Recommend for a follow-up pass**: browser-based access (e.g. claude-in-chrome) as a workaround, since Fandom's Cloudflare gate blocks datacenter-IP fetches but not real browser sessions.

### [unlock-chain incomplete] -- per-species acquisition table -- PARTIALLY RESOLVED at P3 (2026-08-22)
- What's missing: an exact CC-denominated per-species price table -- this specific gap remains open; no source anywhere gives a CC-tier table (consistent with the P3 finding that no discrete CC tiers exist at all -- pricing is continuous, see `mechanics.md` Conservation Credits).
- What P3 recovered: a live community datamining spreadsheet, **"PZ Animal Husbandry and Planner" by u/senginous** (Steam Guide id 3048155055, current through Asia Pack/1.20.1), with per-species **Cash** min/max price data and an explicit 1 CC = $13 (Sandbox) conversion note. Steam guide id 3410761755 ("Thrall's Planet Zoo Spreadsheet Treasure Trove") was reached this time but points to a Patreon-gated sheet -- still inaccessible.
- Current state: captured in `mechanics.md` Unlock Chains. A cash-equivalent min/max range exists per species; an exact CC-denominated table does not exist anywhere in the public community corpus -- treat as a genuine, permanent gap rather than an access failure to retry.

### Russian-language sourcing -- attempted at P3, no new precision found
- P1 flagged this as not reached at all. P3's gap-fill pass (2026-08-22) prioritized it per the brief and searched VK ("Planet Zoo RU" group), Russian Reddit posts, and guidesgame.ru. Found: a VK Tips topic pointing to an existing English-language calculator tool (no distinct Russian dataset); a Russian r/PlanetZoo thread on market-price frustration with no extractable numbers; guidesgame.ru's guide page 404'd. **No Russian source added precision or corroboration beyond the English-language findings** -- this gap-fill target could not be closed even with a dedicated attempt. Not recommended as a priority for a further follow-up pass unless a specific new Russian source surfaces.

### Video transcription -- not performed
- No YouTube video was directly transcribed in any P1 or P3 research pass. Video-tutorial content was referenced by title/description only (e.g. German building tutorials, a Chinese 100-tip Steam guide's tip numbers). Attributable to WebSearch/WebFetch budget exhaustion across multiple passes, not an oversight.

### Reddit (r/PlanetZoo) -- mostly unreachable direct access
- Direct Reddit access failed nearly every attempt across every P1 research pass (the "reddit tool access forbidden" note appears in the Achievement Coverage source list). A handful of Reddit-sourced facts made it in via forum-thread snippets surfaced through WebSearch (e.g. the Bison "neutral to humans" trait, the Zoo Rating Franchise-sharing silence). P3's passes had mixed Reddit access -- some got old.reddit.com/.json working (used for gap-fill items 4 and 7), others hit 403s and a falsely-flagged "private/quarantined" MCP-tool error on r/PlanetZoo. The framework's `reddit_sweep.md` autonomous module remains the recommended path for systematic community-knowledge coverage of this subreddit -- see the P1 recap in `CHECKPOINT.md`.

### Contradicted stat blocks -- three species -- RESOLVED at P3 (2026-08-22)
- `animals/greater_flamingo.md`, `animals/red_deer.md`, `animals/timber_grey_wolf.md` each carried two numerically different P1 housing stat blocks. P3's gap-fill re-checked current Fandom pages against the senginous/Villanelle "Details" tab and found they **agree exactly** for patch-current (1.20.2) data -- the P1 contradiction stemmed from a stale/cached wiki snapshot at that research pass. All three files rewritten with the resolved figures; confidence raised to `high`.

### DLC source-access failures (P3, 2026-08-22)
- **planetzoo.fandom.com returned HTTP 402 to direct WebFetch across every P3 research pass** -- an apparent anti-scraping paywall change since P1 (P1 also hit 402s, so this is a persistent, not new, condition). The full blocked-source ladder was exhausted on every rung by at least one pass; some passes found working alternates (Firecrawl stealth-proxy, a live browser session, or a pre-warmed connection) and got full data through; others did not. **Real welfare-data gap, not just qualitative softening**: 3 packs (Arid Animal Pack, Zookeepers Animal Pack, Asia Animal Pack) have NO in-game welfare numbers at all -- only real-world IUCN/range/diet/social-structure data from Wikipedia. Europe Pack also has thin numeric coverage (qualitative only, no habitat-size figures). See each affected species' `animals/<species>.md` file and `mechanics.md` DLC Layer for the per-pack achievement-confidence knock-on effect.
- **WebSearch hit its session budget cap partway through the P3 research effort**, forcing several passes onto Firecrawl web search, Steam's own APIs, and direct Google Sheets CSV-export endpoints as substitutes.
- **archive.ph/archive.today was refused outright by the fetch tool** in multiple P3 passes ("unable to fetch from archive.ph/archive.is") -- a tool-level restriction, not a source-side block.
- **Console storefronts (Xbox Store, PlayStation Store) were unreachable**, leaving whether the Deluxe Upgrade Pack's console pre-order mechanism is distinct from its PC/Steam DLC form open. See `mechanics.md` DLC Layer.
- **No German or Simplified-Chinese community welfare spreadsheet was reached in any P3 pass**, despite the brief's preference for non-English precision sourcing -- a real, acknowledged shortfall against the source-diversity floor, same pattern as P1.
- **Recommend for a follow-up pass**: browser-based access (e.g. claude-in-chrome) as a workaround for Fandom's persistent 402, to fill Arid/Zookeepers/Asia Animal Pack's in-game welfare numbers and confirm DLC-achievement-zero for the 5 currently-`[Hypothesis - unverified]` packs (see `achievements.md` DLC coverage).

### Documented mechanical formula gaps (not source-access failures -- genuine absence in the public community corpus)
- **Exact welfare loss/recovery rates** (percent-per-hour or per-day, per pillar) beyond the single ~10%/month enrichment-rejuvenation figure -- UNRESOLVED, re-attempted at P3 with no new data found (official guide, community datamining, Frontier forums, Reddit all searched specifically). See `mechanics.md` Animal Welfare. This is now the single largest confirmed-genuine (not access-blocked) gap in the corpus.
- ~~Exact loan interest rate (numeric)~~ -- **RESOLVED at P3**: no single universal rate exists; each loan/scenario sets its own fixed % (official source). See `mechanics.md` Economy & Currencies.
- Exact Zoo Rating category weighting beyond the confirmed 15%-marketing figure -- UNRESOLVED, re-attempted at P3 against the same official source that gives the 15% figure; the other four categories are named with no accompanying weight anywhere. See `mechanics.md` Zoo Rating.
- ~~Whether a discrete Conservation-Credit price-tier system exists in the live UI~~ -- **RESOLVED at P3**: confirmed false, not just unconfirmed -- pricing is continuous/per-individual everywhere checked. See `mechanics.md` Conservation Credits.
- ~~Whether cash-purchased animals can ever generate CC on release, vs. a birth-origin gate~~ -- **RESOLVED at P3**: birth-origin gate confirmed (3 corroborating community sources; doesn't contradict the official guide). See `mechanics.md` Conservation Credits.
- Whether Franchise mode aggregates/averages Zoo Rating across a player's multiple zoos -- inferred from source silence, not a stated fact. Not part of the P3 gap-fill scope; still open.

## Always-blocked categories

- **Developer achievement descriptions** -- Steam/PSN/Xbox achievement description text is publisher IP and is intentionally NOT captured. Achievement *names* are captured verbatim (lookup keys); trigger conditions are researched and paraphrased in P1, not lifted from the platform.
- **Dormant vectors** -- Planet Zoo has no enemies, no combat, and no traditional puzzles, so the `boss` / `enemy` / `puzzle` research vectors have no content to fill. This is expected, not a gap.
