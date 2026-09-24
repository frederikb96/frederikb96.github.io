# Footprints and Handprints

**[Read the paper (PDF)](footprints-and-handprints.pdf)**

A white paper on carbon and ecological accounting. It works through why one country
has several different and equally correct per-capita footprint figures, how a personal
footprint is actually computed, what falls inside a product's system boundary, why the
ecological footprint is mostly a carbon number wearing an area unit, and how the
handprint differs from the footprint and why the two can never be netted against each
other.

## Build

```
make          # figures + PDF
make figures  # regenerate figures only
make clean
```

Requires TeX Live (`latexmk`, `pdflatex`) and Python with matplotlib.

## Layout

```
main.tex                 the paper
scripts/make_figures.py  generates every figure in figures/ from data/
data/                    primary-source data files
figures/                 generated PDFs, do not edit by hand
```

## Data

`data/gfn_series.csv` was extracted from the Global Footprint Network open data
platform (`data.footprintnetwork.org`, country trends view, 2026 edition of the
National Footprint and Biocapacity Accounts). It holds per-capita footprint and
biocapacity by land type for Germany and the world, 1961–2025.

The `data/owid-*.csv` files are direct downloads of the Our World in Data grapher CSV
endpoints for territorial CO₂ per capita, consumption-based CO₂ per capita, and
greenhouse gases per capita including land use.

Every other number in the paper carries a citation to the source it came from, and
each source was read directly rather than quoted from a search result.

Charts use the Okabe-Ito categorical palette, checked for colour-vision separation,
and carry direct labels so identity never depends on colour alone.

## Licence

Text and figures under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/),
the build tooling under MIT. See `LICENSE`.
