PDF = footprints-and-handprints.pdf

.PHONY: all figures clean

all: figures
	latexmk -pdf -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
	cp build/main.pdf $(PDF)

figures:
	python3 scripts/make_figures.py

clean:
	rm -rf build
