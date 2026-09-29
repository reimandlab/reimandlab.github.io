# reimandlab.org

Lab website built with [Astro](https://astro.build). All content lives in small
Markdown/YAML files under `src/content/` and `src/data/`; the pages are generated from them.

## Run locally

Requires Node 20+ (`brew install node`).

```sh
npm install      # first time only
npm run dev      # test site at http://localhost:4321, reloads on save
npm run build    # full build into dist/ (catches content errors)
```

## Everyday edits

| To… | Edit |
|---|---|
| Add a news one-liner | `src/data/news.yaml`, one line at the top |
| Add a longer news post | new file in `src/content/posts/` (copy an existing one) |
| Add a paper | new file in `src/content/papers/`, e.g. `2026-smith-nat-commun.md` |
| Add / move a person | `src/content/people/<name>.md`; set `status: alumni` and `now:` when someone leaves |
| Change a tool | `src/content/software/<tool>.md` |
| Intro, contact, join text | `src/data/site.yaml` |
| Photos, figures | `public/images/…` |

### Paper fields

```yaml
---
title: Integrative pathway enrichment analysis of multivariate omics data
authors: ["Marta Paczkowska*", "Jonathan Barenboim*", "Jüri Reimand"]   # * = co-first/co-corresponding
journal: Nature Communications
year: 2020
doi: 10.1038/s41467-019-13983-9
code: https://github.com/reimandlab/ActivePathways   # optional
themes: [multi-omics]        # drivers | multi-omics | biomarkers
featured: true               # shown on the home page and research themes
# lab_led: true              # normally inferred: first or last author is a lab member
---
```

Lab members are bolded automatically by matching surname + first initial against
`src/content/people/` (add other spellings to `author_names:`).

## Deploying

Pushing to `main` builds and publishes via `.github/workflows/deploy.yml`.
Before the first merge of this branch, switch **Settings → Pages → Source** to
**GitHub Actions** (the old site was built by Jekyll from the branch).
Old URLs (`/team/`, `/papers/`, `/news/<post>/`, …) keep working via redirects.
