# Render a document's index.md to a PDF beside it.
#
#   make pdf DOC=bahn-zugbindung-alternative
#   make pdf-all
#
# Only for Markdown documents. The two LaTeX papers build with their own
# Makefile in their own directory.

PANDOC ?= pandoc
MD_DOCS := $(shell find . -mindepth 2 -maxdepth 3 -name index.md \
             -not -path './_site/*' \
             -not -path './footprints-and-handprints/*' \
             -not -path './complete-food-and-home-cooking/*' \
             | sed 's|/index.md$$||;s|^\./||')

.PHONY: pdf pdf-all list clean

pdf:
	@test -n "$(DOC)" || { echo "usage: make pdf DOC=<directory>"; exit 1; }
	@test -f "$(DOC)/index.md" || { echo "no $(DOC)/index.md"; exit 1; }
	$(PANDOC) "$(DOC)/index.md" \
	  --from markdown --pdf-engine=pdflatex \
	  --template=_pdf/template.latex \
	  --output "$(DOC)/$(subst /,-,$(DOC)).pdf"
	@echo "wrote $(DOC)/$(subst /,-,$(DOC)).pdf"

pdf-all:
	@for d in $(MD_DOCS); do $(MAKE) --no-print-directory pdf DOC=$$d || exit 1; done

list:
	@for d in $(MD_DOCS); do echo $$d; done

clean:
	@find . -mindepth 2 -maxdepth 3 -name '*.pdf' \
	  -not -path './footprints-and-handprints/*' \
	  -not -path './complete-food-and-home-cooking/*' -delete
