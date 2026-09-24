# Complete Food and Home Cooking

**[Read the paper (PDF)](complete-food-and-home-cooking.pdf)**

A white paper comparing the environmental footprint and health evidence of vegan
complete foods — powders formulated to be a whole diet, such as Huel, Jimmy Joy and
Mana — against a regional, seasonal, whole-food vegan diet in Germany. Both sides are
vegan, which holds the largest dietary variable constant and leaves a narrower
question: given that someone eats plants, does the form those plants arrive in change
anything?

## Build

```
make
make clean
```

Requires TeX Live (`latexmk`, `pdflatex`).

## What's in it

- A reconstructed bottom-up cradle-to-gate estimate for a complete food, since no
  independent product assessment exists for any brand in the category
- Two 2000 kcal day models for the whole-food comparator, one optimised for regional
  and seasonal produce, one with imported and greenhouse items
- An ingredient-level refinement penalty traced through bean → meal → protein isolate
- The health evidence: the ultra-processed food literature and its subgroup
  heterogeneity, and the vegan micronutrient and fracture data

## Data

- Agribalyse 3.1 via the ADEME data API — whole foods, cradle-to-shelf, split by
  life-cycle stage, with seasonal and off-season entries listed separately
- CarbonCloud ClimateHub verified product reports — industrial ingredients at factory
  gate, split into agriculture, processing and transport
- Scarborough et al. 2023 in Nature Food — measured diet-group footprints
- Manufacturer sustainability pages, read directly
- Primary publications for every effect size and confidence interval

Every number was verified against its primary source rather than a search summary.

## Headline result

Both options land in roughly 1–3 kg CO₂e per 2000 kcal, against about 10 kg for a
meat-heavy diet. The spread within each option is larger than the gap between them.
What drives a complete food's footprint is ingredient refinement rather than
manufacturing: dry blending accounts for 0.2 % of the total, while soy protein isolate
costs about six times its parent bean with 84 % of that coming from processing.

## Licence

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). See `LICENSE`.
