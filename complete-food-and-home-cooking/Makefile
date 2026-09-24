PDF = complete-food-and-home-cooking.pdf

.PHONY: all clean

all:
	cd src && latexmk -pdf -interaction=nonstopmode -halt-on-error -output-directory=../build main.tex
	cp build/main.pdf $(PDF)

clean:
	rm -rf build
