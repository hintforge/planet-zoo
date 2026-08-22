# Planet Zoo — Hintforge Companion

![Planet Zoo companion status — coverage, how current it is, and spoiler control](assets/readme-status-card.svg)

A spoiler-controlled hint companion for **Planet Zoo**, Frontier's wildlife management sim where you design habitats, breed species, and build the zoo of your dreams across career scenarios and sandbox. Built in the [Hintforge](https://github.com/hintforge/builder) format: a loyal sidekick that answers only from these guide files — never from guesswork — at the spoiler level you set.

## Use it

You need a Hintforge reader running in Claude Code, Codex, or OpenClaw. Point it at this repo:

> Load the Planet Zoo guide from github.com/hintforge/planet-zoo

Then just ask — *"what habitat does a snow leopard need," "how do I breed red pandas," "what are the career scenario goals."* Runtime setup lives in [`hintforge/reader`](https://github.com/hintforge/reader).

## Spoilers

**You** set two independent dials — enemy warnings (Tier 0–5) and puzzle/decision warnings (Tier 0–3) — both **silent by default**; the guide volunteers nothing until you raise one. Planet Zoo is a sandbox sim, so these dials are near-dormant — the real spoiler surface is career-scenario objectives and outcomes, gated by the puzzle dial. There's no save-state reader, so every answer comes from this guide's files.

## What's inside

A structured Markdown corpus — core mechanics (welfare, conservation, economics, breeding, staff, guests), a 210-species bestiary covering habitat requirements and welfare needs across the base game and 21 DLC packs, career scenarios, controls, settings, and achievements. Interactive tools (a habitat planner is the natural fit) aren't built yet. The companion reads and writes only the files you control.
