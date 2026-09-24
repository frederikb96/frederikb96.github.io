PDF = footprints-and-handprints.pdf
PYTHON ?= uv run --quiet --with matplotlib python3

.PHONY: all figures clean

all: figures
	latexmk -pdf -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
	cp build/main.pdf $(PDF)

# matplotlib is not a system package. uv fetches it for the run, so nothing is
# installed globally and no virtualenv is kept in the tree. Override with
# PYTHON=python3 where matplotlib is already available.
figures:
	$(PYTHON) scripts/make_figures.py

clean:
	rm -rf build
