# Animals -- species bestiary index

**status:** research-integrated
**last_reconciled:** 2026-08-22

This is a **corpus-declared vector extension** (declared in `architecture_manifest.md`). It is the dominant reference surface for Planet Zoo: one file per species, `animals/<species>.md`, holding that animal's welfare requirements and Zoopedia-grade facts.

**Base-game roster: 78 species** (54 Habitat-type incl. Walkabout-flagged + 24 Exhibit-type incl. 1 Walkthrough Exhibit), cross-validated two ways during P1 ingestion: the Fandom `Category:Base_Game_Animals` index lists 78 items, and an independent continent-by-continent count converges on the same total. This is materially smaller than most players assume -- most "iconic" Planet Zoo megafauna (Jaguar, Koala, Red Kangaroo, Polar Bear, Reindeer, American Alligator, Capybara, Llama, Alpaca, Giant Anteater, Eurasian Lynx, European Bison/Wisent) is **DLC-gated**, not base game. DLC species are out of P1 scope -- see `research_briefs/p3.txt`.

## Housing types (four, not three)

- **Habitat** -- standard large enclosure; full Land/Water/Climb Area, Fence Grade, Biome stats.
- **Walkabout** (subcategory of Habitat) -- a Habitat animal flagged calm/safe enough for a guest path to run through its enclosure via guest gates. Mechanically identical to a normal Habitat animal otherwise; a guest-path permission flag, not a separate welfare ruleset. **Walkabout is permission, not a recommendation** -- whether a walkthrough actually works is decided by the separate **Guest tolerance** stat below, not by this flag. 8 of the 26 Walkabout-eligible species are `Shy` and will throw low-welfare warnings in a busy walkthrough: Aardvark, Chinese Pangolin, Nile Lechwe, Nine-Banded Armadillo, Okapi, Pronghorn Antelope, Springbok, White-Faced Saki.
- **Exhibit** -- small glass/terrarium enclosure (~16 m² fixed footprint, community-measured), no customizable land plot, no mixed-species exhibits ever, exhibit-specific enrichment pool.
- **Walkthrough Exhibit** (subcategory of Exhibit) -- a large (12m x 20m, $9,000) walk-in building (added Update 1.11). Legally still an "Exhibit" animal (same no-mixing rule) but housed in the bigger structure. Only base-game qualifier: `animals/malabar_rose_butterfly.md`.

## What each species file carries

Per species, at claim-format granularity: welfare requirements (habitat size, land/water split, terrain composition, temperature/climate band, biome/foliage preference), **guest tolerance**, social group type and size, mixing compatibility, accepted enrichment, diet, housing type, conservation status and continent, and any species-specific welfare gotcha. Numeric housing fields are sourced from a structured community dataset (planetzoohelper.com) and community spreadsheets (single-source, `confidence: medium`); qualitative facts are sourced from Planet Zoo Wiki species pages accessed via search-snippet/Firecrawl workaround this pass (Fandom returned HTTP 402 on all direct-fetch rungs -- see `limitations.md`).

**Guest tolerance (added 2026-09-17).** The game's per-species relationship-with-humans stat -- `Shy`, `Neutral` or `Confident` -- which decides how much guest proximity and crowding an animal absorbs before Stress accrues. Present on all 167 Habitat species (81 Confident / 48 Neutral / 38 Shy); Exhibit species do not carry it, because guests cannot approach them in the same way. Sourced in one pass from the same planetzoohelper.com dataset the numeric housing fields already use (its `relationWithHumans` field, captured 2026-09-17), so it inherits the same single-source `confidence: medium` caveat. The 21 gap-flagged species have it as their only recovered in-game welfare field; their gap notices otherwise stand unchanged. **Why it was added:** a reader building a walkthrough habitat from the Walkabout flag alone hit exactly the low-welfare warnings the flag gave no warning about -- the corpus stated the rule in `mechanics.md` but carried no per-species value to apply it to.

**Contradicted stat blocks -- RESOLVED at P3 (2026-08-22)**: three species (`greater_flamingo.md`, `red_deer.md`, `timber_grey_wolf.md`) received two independently-sourced but numerically different housing stat blocks at P1 (one via planetzoohelper.com, one via direct Fandom access through Firecrawl). P3's gap-fill re-checked current Fandom pages against a current community datamining spreadsheet and found they agree exactly for the 1.20.2 patch -- the P1 contradiction was a stale/cached wiki snapshot at that research pass. All three files rewritten with resolved figures, confidence raised to `high`.

## Roster -- Habitat animals: Africa (29)

Aardvark, African Buffalo, African Savannah Elephant, African Wild Dog, African Leopard, Aldabra Giant Tortoise, Black Wildebeest, Black-and-White Ruffed Lemur, Bongo, Bonobo, Cheetah, Common Ostrich, Common Warthog, Gemsbok, Hippopotamus, Mandrill, Nile Monitor, Nyala, Okapi, Plains Zebra, Red Ruffed Lemur, Reticulated Giraffe, Ring Tailed Lemur, Sable Antelope, Spotted Hyena, Springbok, West African Lion, Western Chimpanzee, Western Lowland Gorilla.

## Roster -- Habitat animals: Asia (16)

Bactrian Camel, Bengal Tiger, Bornean Orangutan, Chinese Pangolin, Formosan Black Bear, Gharial, Giant Panda, Himalayan Brown Bear, Indian Elephant, Indian Peafowl, Indian Rhinoceros, Japanese Macaque, Red Panda, Saltwater Crocodile (secondary continent: Oceania), Siberian/Amur Tiger, Snow Leopard.

## Roster -- Habitat animals: Americas, Europe & cross-continent (9)

American Bison, Grizzly Bear, Pronghorn Antelope, Baird's Tapir, Collared Peccary, Galapagos Giant Tortoise, Greater Flamingo, Red Deer, Timber/Grey Wolf.

## Roster -- Exhibit animals (23) + Walkthrough Exhibit (1) = 24

Lesser Antillean Iguana, Boa Constrictor, Brazilian Wandering Spider, Green Iguana, Lehmann's Poison Frog, Goliath Birdeater, Titan Beetle, Yellow Anaconda, Giant Slippery/Goliath Frog, Giant Forest Scorpion, Golden Poison Frog, Giant Tiger Land Snail, Brazilian Salmon Pink Tarantula, Eastern Brown Snake, Giant Desert Hairy Scorpion, Amazonian Giant Centipede, Gila Monster, Puff Adder, Western Diamondback Rattlesnake, Common Death Adder, Goliath Beetle, Giant Burrowing Cockroach, Mexican Redknee, **Malabar Rose Butterfly (Walkthrough Exhibit)**.

## Keyword -> file map

Common-name lookups differing from the file slug (species whose file uses the full common name or a disambiguating form):

- "elephant" (ambiguous, two species) -> `african_savannah_elephant.md` or `indian_elephant.md`
- "tiger" (ambiguous, two species) -> `bengal_tiger.md` or `siberian_amur_tiger.md`
- "lion" -> `west_african_lion.md` (only base-game lion subspecies)
- "zebra" -> `plains_zebra.md` (only base-game zebra species -- Grevy's Zebra does not exist in-game)
- "camel" -> `bactrian_camel.md`
- "wolf" / "grey wolf" / "timber wolf" -> `timber_grey_wolf.md`
- "panda" (ambiguous) -> `giant_panda.md` or `red_panda.md`
- "tortoise" (ambiguous, two species) -> `aldabra_giant_tortoise.md` or `galapagos_giant_tortoise.md`
- "rattlesnake" -> `western_diamondback_rattlesnake.md`
- "tarantula" (ambiguous, two species) -> `brazilian_salmon_pink_tarantula.md` or `mexican_redknee.md`
- "poison dart frog" (ambiguous, two species, NOT color morphs of one) -> `lehmanns_poison_frog.md` or `golden_poison_frog.md`
- "butterfly" -> `malabar_rose_butterfly.md` (the only base-game butterfly / Walkthrough Exhibit species)
- "scorpion" (ambiguous, two species) -> `giant_forest_scorpion.md` or `giant_desert_hairy_scorpion.md`

## DLC roster (added P3, 2026-08-22) -- 132 species across 21 packs

Each DLC species carries `spoiler: dlc:<Pack Title>` on its claim metadata (an independent axis from the enemy/puzzle tier dials -- see `warning_tiers.md`). Full per-pack mechanics/achievements/sources: `mechanics.md` DLC Layer. Full per-pack scenario detail: `sections/dlc_scenarios.md`. **3 packs have real-world biology only, no in-game welfare numbers** (flagged below and in each affected file) -- a genuine research gap, see `limitations.md`.

- **Deluxe Upgrade Pack** (3): Komodo Dragon, Pygmy Hippopotamus, Thomson's Gazelle
- **Arctic Pack** (4): Polar Bear, Reindeer, Arctic Wolf, Dall Sheep
- **South America Pack** (5): Jaguar, Llama, Colombian White-Faced Capuchin Monkey, Giant Anteater, Red-Eyed Tree Frog
- **Australia Pack** (5): Koala, Dingo, Red Kangaroo, Southern Cassowary, Eastern Blue-Tongued Lizard
- **Aquatic Pack** (5): King Penguin, Giant Otter, Grey Seal, Cuvier's Dwarf Caiman, Diamondback Terrapin
- **Southeast Asia Animal Pack** (8): Sun Bear, Clouded Leopard, Malayan Tapir, Proboscis Monkey, North Sulawesi Babirusa, Binturong, Dhole, Giant Malaysian Leaf Insect
- **Africa Pack** (5): Meerkat, Southern White Rhinoceros, African Penguin, Fennec Fox, Sacred Scarab Beetle
- **North America Animal Pack** (8): Moose, Cougar, California Sea Lion, North American Beaver, American Alligator, Black-Tailed Prairie Dog, Arctic Fox, American Bullfrog
- **Europe Pack** (5, **no in-game numeric welfare data recovered this pass**): Alpine Ibex, Eurasian Lynx, European Badger, European Fallow Deer, Fire Salamander
- **Wetlands Animal Pack** (8): Capybara, Platypus, Asian Small-Clawed Otter, Spectacled Caiman, Nile Lechwe, Wild Water Buffalo, Red-Crowned Crane, Danube Crested Newt
- **Conservation Pack** (5): Przewalski's Horse, Amur Leopard, Scimitar-Horned Oryx, Siamang, Axolotl
- **Twilight Pack** (5): Raccoon, Red Fox, Common Wombat, Striped Skunk, Egyptian Fruit Bat
- **Grasslands Animal Pack** (12: 7 habitat + 5 butterflies in the game's only multispecies exhibit): Maned Wolf, Emu, Caracal, Red-Necked Wallaby, Nine-Banded Armadillo, Striped Hyena (do not confuse with base-game Spotted Hyena), Blue Wildebeest, Cloudless Sulphur, European Peacock, Menelaus Blue Morpho, Monarch, Old World Swallowtail
- **Tropical Pack** (5): Fossa, Lar Gibbon, Red River Hog, Asian Water Monitor, Brown-Throated Sloth
- **Arid Animal Pack** (8, **real-world biology only, no in-game welfare numbers**): Dromedary Camel, African Crested Porcupine, Addax, Somali Wild Ass, Black Rhinoceros, Sand Cat, Dama Gazelle, Desert Horned Viper
- **Oceania Pack** (5): North Island Brown Kiwi, Tasmanian Devil, Little Penguin, Quokka, Spectacled Flying Fox
- **Eurasia Animal Pack** (8): Wisent/European Bison, Wild Boar, Mute Swan, Sloth Bear, Wolverine, Saiga, Takin, Hermann's Tortoise
- **Barnyard Animal Pack** (7, all eligible for the free-update Animal Encounters petting mechanic -- see `mechanics.md`): Sussex Chicken, Highland Cattle, Alpine Goat, Alpaca, American Standard Donkey, Hill Radnor Sheep, Tamworth Pig
- **Zookeepers Animal Pack** (7, **real-world biology only, no in-game welfare numbers**): Pallas's Cat, Hamadryas Baboon, Markhor, Spectacled Bear, African Spurred (Sulcata) Tortoise, Kirk's Dik-Dik, Coquerel's Sifaka
- **Americas Animal Pack** (7): Coyote, Ocelot, Bush Dog, Greater Rhea, White-Faced Saki, American Flamingo, Bighorn Sheep
- **Asia Animal Pack** (7, **real-world biology only, no in-game welfare numbers**): Lion-Tailed Macaque, Père David's Deer, Bornean Elephant, Honey Badger, Japanese Raccoon Dog, Blackbuck, Nilgai

**Corpus total: 210 species files (78 base + 132 DLC)** across all housing types.

## Species confirmed NOT IN THE GAME under any pack (checked at P1 and/or P3, do not create files)

Eastern Grey Kangaroo, American Black Bear (only Grizzly Bear, Formosan Black Bear, Himalayan Brown Bear, Giant Panda are Planet Zoo bears), Two-toed Sloth (only Brown-Throated Sloth exists, DLC), Ring-tailed Coati, Plains Bison (not separate -- American Bison covers it), Grevy's Zebra, Nile Crocodile (only Saltwater Crocodile and Gharial exist), Sumatran Orangutan, Chinese Alligator.

**Everything else P1 listed here as "out of scope, DLC" now has its own file** -- see the DLC roster section above. That includes Jaguar, Llama, Giant Anteater, Alpaca, Koala, Red Kangaroo, Emu, European Bison/Wisent, Eurasian Lynx, Reindeer, Polar Bear, American Alligator, Capybara, Fossa, Blackbuck, Père David's Deer, Thomson's Gazelle, Komodo Dragon, Pygmy Hippopotamus, Amur Leopard, Przewalski's Horse, Scimitar-Horned Oryx, Siamang, Malayan Tapir, Sun Bear, Binturong, Dhole, Clouded Leopard, Proboscis Monkey, North Sulawesi Babirusa, Markhor, Pallas's Cat, Takin (Eurasia Pack, not "Sichuan Takin" as P1's brief hedged -- resolved to the same species), and every DLC-gated exhibit species P1 flagged (Diamondback Terrapin, Giant Malaysian Leaf Insect, Sacred Scarab Beetle, American Bullfrog, Fire Salamander, Danube Crested Newt, Axolotl, Egyptian Fruit Bat, the 5 butterflies, Brown-Throated Sloth, Desert Horned Viper, Spectacled Flying Fox, Hermann's Tortoise, Red-Eyed Tree Frog). "Common Bluetongue" (P1's naming) is the Australia Pack's Eastern Blue-Tongued Lizard file.

## Unlock chains -- gap flag

**[unlock-chain incomplete] -- partially resolved at P3 (2026-08-22)**: a per-species acquisition table was not obtainable at P1 (Fandom's `List_of_Animals`/`Conservation_Credits` pages, a community pricing spreadsheet were inaccessible). P3's gap-fill found a live community datamining spreadsheet ("PZ Animal Husbandry and Planner" by u/senginous) with per-species **cash** min/max price data and a documented 1 CC = $13 (Sandbox) conversion. An exact **CC-denominated** per-species table still does not exist anywhere in the public community corpus -- confirmed genuine gap, not an access failure. The confirmed general mode-level pattern plus the new cash-price-range data lives in `mechanics.md` Unlock Chains. See `limitations.md`.

## Sources

- Fandom `Category:Base_Game_Animals`, `List_of_Animals`, `Category:Animals_by_Continent`, `Category:Habitat_Animals`, `Category:Exhibit_Animals`, `Category:Walkthrough_Animals`, `Category:Walkabout_Animals`, `Category:Handleable_Animals` [community-wiki, accessed via search-snippet/Firecrawl workaround this session -- direct fetch, api.php export/parse, BreezeWiki, and archive.ph all 402'd]
- planetzoohelper.com structured dataset [datamining]
- Steam Community "Habitat Husbandry Guide and Planner" (senginous, id 3048155055) [community-wiki/datamining]
- **P3 additions:** Steam DLC appid enumeration + per-pack appdetails [official-pr]; Villanelle's Planet Zoo Data Chest spreadsheet [community-wiki/datamining]; Steam Community "PZ Animal Husbandry and Planner" (senginous, id 3048155055 -- current through Asia Pack/1.20.1) [datamining]; per-pack Fandom wiki pages via Firecrawl stealth-proxy where direct fetch 402'd; Wikipedia species pages for the 3 real-world-only packs (Arid, Zookeepers, Asia Animal Pack).
