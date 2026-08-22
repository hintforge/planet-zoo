# Planet Zoo -- Settings Reference

**status:** research-integrated
**last_reconciled:** 2026-08-22

Settings that affect performance, difficulty perception, and quality of life. All content `spoiler: none`, `enemy-tier: 0`, `puzzle-tier: 0`.

**Confirmed menu tabs**: the official Frontier guide explicitly names a **"Controls" tab**; a PCGamingWiki fix note independently references a **"Video settings page"** (used to force exclusive-fullscreen for higher refresh rates). Only **Video** and **Controls** are confirmed by name; a difficulty toggle is also settings-menu-accessible mid-game. **[Gap]** -- the full tab list (whether "Audio," "Gameplay," "Accessibility" exist as separately named tabs) is not independently confirmed. The section headers below are organized by topic, not confirmed exact tab names -- treat any specific tab-name claim as unverified until checked against the live menu.

## Video / Graphics -- performance impact in large zoos

Best-sourced settings topic in the P1 pass, from a 118-rating Steam Community "Performance Improvement" guide plus a second FPS-tips discussion, corroborated in German and Chinese:

| Setting | Impact | Recommendation |
|---|---|---|
| Resolution | High | Native 1080p ideal; scale down from 2K/4K if struggling |
| Anti-aliasing | Moderate | TAA (heaviest) > FXAA > None; game is more CPU-bound than GPU-bound |
| Shadow quality | Noticeable, not immediately visible | Medium-or-lower |
| Water reflections | Real hit | Disable if not noticed |
| Screen-space reflections | Similar to water reflections | Disable if perf-constrained |
| Terrain geometry detail | Minor visible impact | Scale down |
| **Guest limiter (max guest count)** | **Largest single lever** -- every guest's needs/pathing recalculated continuously | ~3000 guests recommended ceiling; independently corroborated in Chinese (tip #23: "checking the guest-limit box... effectively solves performance problems") and German ("Limiting the number of guests can help to reduce lag") |
| Path congestion / narrow paths | Guest bunching measurably hits performance | Widen chokepoint paths |
| Guest/animal/staff "needs" simulation | Sandbox-only toggles; each disabled need removes a recurring calculation | Use in Sandbox for big builds |
| Animal count / habitat size | More animals = more calculation | Fewer, smaller habitats where possible |
| Foliage/climbing flags | Disabling the "climbable" flag on trees/scenery objects that don't need it removes a background calculation | Disable climbing on non-essential foliage/structures |
| Pause while building | Full calculation freeze | Always pause mid-build |
| DirectX / engine note | DX11 on the custom Cobra engine, described as "much more CPU heavy than GPU intensive" -- a 1080->3080 GPU upgrade reportedly produced "not much improvement" for one reporting user | Prioritize CPU headroom over GPU spend when zoo-building is the bottleneck |

_source: Tomboeg "Performance Improvement" Steam guide + CombatShawn "FPS improvement tips for large zoo" Steam discussion + Chinese 100-tip Steam guide + German-language Steam discussion "Big zoo is lagging" + Reddit "LAG ADVICE"/"impossible to build large zoo" threads 2026-08-21 · capture: web_fetch · confidence: high (5 sources, 3 languages) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Accessibility

- **UI scale is coarse and cuts off menus for low-vision players.** A 2019-era Steam Community thread (still active as of a 2025 reply) documents the in-game scaling option jumping directly from 100% to 160% with no intermediate steps, causing menu text/window clipping at 160%. Community workaround: edit the config file directly (`Saved Games\Frontier Developments\Planet Zoo\<id>\Config`) to set an intermediate value like 120% by hand. Apparently unresolved as of the most recent visible reply (2025). [single long-running thread spanning 2019-2025, class:forum]
- **No native colorblind mode.** PCGamingWiki's structured "Color blind mode" field is marked unsupported. **[Contradicted across sources]** -- a Reddit snippet states "Planet Zoo 1 does come with some accessibility features, especially for people who are colour blind"; full thread content could not be retrieved to resolve this discrepancy. Flagging rather than asserting either claim as settled.
- **Closed captions exist but are hardcoded on** whenever characters speak (not a togglable subtitle option in the traditional sense) per PCGamingWiki's structured Audio table. Separate volume controls and subtitle support are listed as present. [single source]
- A Frontier-forums thread requesting phobia-related accessibility options implies none exist as of that thread -- consistent with Planet Zoo's accessibility surface being comparatively thin versus later Frontier titles (Jurassic World Evolution 2 later added a dedicated colorblind Dinosaur Highlight option that Planet Zoo does not appear to have received). [single source]

_source: deep-research cascade P1 2026-08-21 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Gameplay / difficulty (settings-adjacent)

Difficulty (Easy/Medium/Hard) is changeable **per scenario launch**, through the settings menu, and affects welfare decay rate, guest happiness/refund behavior, and staff fatigue -- not performance-relevant, but the one other settings-menu behavior independently confirmed by the official Frontier guide alongside Controls/Video. See `mechanics.md` Game Modes for how difficulty interacts with the Hard-difficulty achievement trap.

## Sources

- Tomboeg "Performance Improvement" Steam guide [forum]
- CombatShawn FPS discussion [forum]
- Chinese 100-tip Steam guide [forum, translated from: Chinese]
- German-language Steam discussion [forum, translated from: German]
- PCGamingWiki [community-wiki]
- Official Frontier help centre: https://one.planetzoogame.com/help-centre/player-guides/the-basics
- Reddit accessibility/performance threads [forum, snippet-level]
