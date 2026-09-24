---
layout: default
lang: en
locale: en_GB
title: "Footprints and Handprints"
description: >-
  A whitepaper on carbon and ecological accounting: why one country has several different and
  equally correct per-capita footprint figures, how a personal footprint is computed, what falls
  inside a product's system boundary, why the ecological footprint is mostly a carbon number in an
  area unit, and why a handprint can never be netted against a footprint.
date_published: "2026-09-24"
meta_line: "Whitepaper · <a href=\"footprints-and-handprints.pdf\">Read the paper (PDF)</a>"
lede: >-
  A whitepaper on carbon and ecological accounting. It works through why one country has several
  different and equally correct per-capita footprint figures, how a personal footprint is actually
  computed, what falls inside a product's system boundary, why the ecological footprint is mostly
  a carbon number wearing an area unit, and how the handprint differs from the footprint and why
  the two can never be netted against each other.
colophon: >-
  Text and figures under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), the build
  tooling under MIT. Research and drafting were assisted by an AI tool; every cited source was
  checked against the primary document, and responsibility for the content rests with the author.
  Corrections are welcome — [open an
  issue](https://github.com/frederikb96/frederikb96.github.io/issues).
---

**[Read the paper (PDF)](footprints-and-handprints.pdf)** · [source, data and figure scripts](https://github.com/frederikb96/frederikb96.github.io/tree/main/footprints-and-handprints)

## What it covers

Footprint figures are quoted constantly and almost never with the accounting choice that produced them. The paper starts there, because the same country in the same year legitimately carries several per-capita numbers at once depending on whether emissions are counted where they are produced or where they are consumed, and on whether land use is inside the boundary.

From there it works down to the individual: how a personal footprint is actually put together, and what it can and cannot tell someone about a decision they are about to make. Then down again to a single product, and the question of where its system boundary is drawn — the choice that decides most of the answer before any data is collected.

Two further arguments carry the second half. The ecological footprint, expressed in global hectares, turns out to be mostly a carbon number wearing an area unit, which matters for how much independent information it adds over a plain emissions figure. And the handprint — avoided emissions attributed to something you enabled elsewhere — is a different kind of quantity from a footprint, which is why netting one against the other produces a figure that means nothing.

## Data and method

Footprint and biocapacity series by land type for Germany and the world, 1961–2025, come from the Global Footprint Network open data platform, 2026 edition of the National Footprint and Biocapacity Accounts. Territorial CO₂ per capita, consumption-based CO₂ per capita, and greenhouse gases per capita including land use are direct downloads of the Our World in Data grapher endpoints.

Every other number carries a citation to the source it came from, and each source was read directly rather than quoted from a search result. Figures are generated from the primary data by a script in the repository rather than drawn by hand, so each one can be traced back to its input.

Charts use the Okabe-Ito categorical palette, checked for colour-vision separation, and carry direct labels so identity never depends on colour alone.
