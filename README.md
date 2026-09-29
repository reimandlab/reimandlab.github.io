# reimandlab.org

Lab website built with [Jekyll](https://jekyllrb.com) and published by GitHub Pages
from the `main` branch. Everything is Markdown/YAML; pages are generated from these files.

## Everyday edits

| To… | Edit |
|---|---|
| Add news | new file in `_posts/`, named `YYYY-MM-DD-short-name.md` (see below) |
| Add a paper | new file in `_papers/`, e.g. `2026-smith-nature-communications.md` |
| Add / update a person | `_people/<name>.md`; when someone leaves set `status: alumni` and `now:` |
| Change a tool | `_software/<tool>.md` |
| Research themes | `_research/*.md` |
| Intro, contact, join text, links | `_data/site.yml` |
| Photos, figures | `images/…` |

### News item

A one-liner needs only the header; add text below it for a longer post with its own page.

```markdown
---
title: "Paper on ion channel genes in glioblastoma"
type: paper          # paper | preprint | award | talk | people | update
short: "Paper in Nature Communications on ion channel genes in glioblastoma"
link: https://doi.org/10.1038/...    # optional: where the one-liner points
---
```

### Paper

```yaml
---
title: Integrative pathway enrichment analysis of multivariate omics data
authors: ["Marta Paczkowska*", "Jonathan Barenboim*", "Jüri Reimand"]   # add * for co-first, # for co-corresponding
journal: Nature Communications
year: 2020
doi: 10.1038/s41467-019-13983-9
code: https://github.com/reimandlab/ActivePathways   # optional
themes: [multi-omics]        # drivers | multi-omics | biomarkers
featured: true               # shown on the home page and research themes
# lab_led: true              # normally inferred: first or last author is a lab member
# authors_truncated: true    # list is incomplete, shown with "et al."
# unbold: ["Mona Meyer"]     # lab member who wasn't in the lab yet for this paper
---
```

### Adding new papers from Google Scholar

1. On your Scholar profile, tick the select-all box → **Export** → **BibTeX**, save the file.
2. From the repo folder run `python3 scripts/import_scholar.py ~/Downloads/citations.bib`
3. Only papers not already on the site are added (listed on screen). Open the new
   files in `_papers/` to add `featured: true`, fix themes, or paste a full author list.

Lab members are bolded automatically by matching surname + first initial against
`_people/` (add other spellings to `author_names:`).

## Preview locally (optional)

GitHub builds the live site itself; a local preview needs Ruby:

```sh
brew install ruby        # then follow brew's note to put it on your PATH
bundle install           # first time only
bundle exec jekyll serve # http://localhost:4000, rebuilds on save
```

Old URLs (`/team/`, `/papers/`, `/news/<post>/`, `/feed.xml`) keep working.
