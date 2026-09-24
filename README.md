# frederikb96.github.io

Source for https://blog.frederikberg.net/ — whitepapers and worked-through questions, published
so they can be read, cited and checked.

Jekyll on GitHub Pages, no theme gem. `_layouts/default.html` is the only layout and carries every
meta tag, the structured data and the styles. Each document is a directory with an `index.md`;
front matter drives the head (`title`, `description`, `lang`, `locale`, `date_published`,
`meta_line`, and `alt_lang`/`alt_url` for a translated pair).

Two documents are LaTeX papers. Their sources, data and figure scripts sit beside the landing page
in the same directory and build with `make`; the resulting PDF is what the site serves. The build
inputs are excluded from the generated site, not from the repository. `footprints-and-handprints`
needs TeX Live and Python with matplotlib, `complete-food-and-home-cooking` needs TeX Live only —
see each directory's own README.

Text under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) unless a document says
otherwise; the figure tooling is MIT.
