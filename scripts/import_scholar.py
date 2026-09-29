"""Convert a Google Scholar BibTeX export into paper files in _papers/.

Usage:  python3 scripts/import_scholar.py scripts/import/scholar.bib
Existing paper files (matched by title) are never overwritten. Writes a review
list to scripts/import/REVIEW.md for entries that need a human check.
"""
import re, sys, pathlib, unicodedata

SRC = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else 'scripts/import/scholar.bib')
OUT = pathlib.Path('_papers')

LATEX = {r'\"u': 'ü', r'\"o': 'ö', r'\"a': 'ä', r'\"U': 'Ü', r'\"O': 'Ö', r'\"A': 'Ä', r'\"e': 'ë', r'\"i': 'ï',
         r"\'e": 'é', r"\'a": 'á', r"\'o": 'ó', r"\'u": 'ú', r"\'i": 'í', r"\'\i": 'í', r"\'E": 'É', r"\'c": 'ć',
         r'\`e': 'è', r'\`a': 'à', r'\^e': 'ê', r'\^o': 'ô', r'\~n': 'ñ', r'\~a': 'ã', r'\~o': 'õ',
         r'\o': 'ø', r'\O': 'Ø', r'\aa': 'å', r'\AA': 'Å', r'\ss': 'ß', r'\c{c}': 'ç', r'\c c': 'ç',
         r'\v{s}': 'š', r'\v{c}': 'č', r'\v{z}': 'ž', r'\v s': 'š', r'\v c': 'č', r'\l': 'ł', r'\&': '&'}

def delatex(s: str) -> str:
    for k in sorted(LATEX, key=len, reverse=True):
        s = s.replace('{' + k + '}', LATEX[k]).replace(k, LATEX[k])
    s = re.sub(r'[{}]', '', s)
    return re.sub(r'\s+', ' ', s).strip()

SMALL = {'of', 'and', 'in', 'the', 'for', 'on', 'at', 'to', 'a', 'an', '&'}
FIX = {'plos': 'PLOS', 'arxiv': 'arXiv', 'embo': 'EMBO', 'febs': 'FEBS'}

def journal_case(j: str) -> str:
    out = []
    for i, w in enumerate(j.split()):
        lw = w.lower()
        if lw in FIX: out.append(FIX[lw])
        elif i > 0 and lw in SMALL: out.append(lw)
        elif any(c.isupper() for c in w[1:]): out.append(w)      # bioRxiv, TheScienceBreaker
        else: out.append(w[0].upper() + w[1:])
    return ' '.join(out)

def person(a: str) -> str:
    a = delatex(a)
    if ',' in a:
        last, first = [x.strip() for x in a.split(',', 1)]
        return f'{first} {last}'.strip()
    return a

def norm_title(t: str) -> str:
    t = unicodedata.normalize('NFD', t).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]', '', t)[:60]

def field(body: str, k: str) -> str:
    m = re.search(r'\b' + k + r'\s*=\s*\{(.*?)\},?\s*\n', body, re.S)
    return m.group(1).strip() if m else ''

THEMES = {
    'drivers': r'mutat|driver|non-?coding|whole genome|somatic|passenger|chromatin|ctcf|genome sequenc|mutagen',
    'multi-omics': r'pathway|enrichment|network|omics|phospho|signal|profiler|integrat|kinase|interactom|functional interpretation',
    'biomarkers': r'prognos|biomarker|survival|therap|immun|target|outcome|diagnos|drug',
}
PREPRINT = re.compile(r'biorxiv|medrxiv|arxiv|research square|ssrn', re.I)

def main():
    text = SRC.read_text()
    entries = re.findall(r'@(\w+)\{([^,]+),(.*?)\n\}', text, re.S)
    existing = {norm_title(re.search(r'^title:\s*"?(.*?)"?\s*$', p.read_text(), re.M).group(1)): p.name
                for p in OUT.glob('*.md')}
    used = {p.stem for p in OUT.glob('*.md')}
    review, written, skipped = [], 0, 0
    for _, key, body in entries:
        title = delatex(field(body, 'title')).replace('g: Profiler', 'g:Profiler')
        if norm_title(title) in existing:
            skipped += 1; continue
        raw = [x.strip() for x in re.split(r'\s+and\s+', field(body, 'author').replace('\n', ' ')) if x.strip()]
        if not raw:
            raw = ['International Cancer Genome Consortium'] if key.startswith('international') else ['Unknown']
        truncated = raw and raw[-1].lower() == 'others'
        authors = [person(a) for a in raw if a.lower() != 'others']
        journal = journal_case(delatex(field(body, 'journal') or field(body, 'booktitle') or field(body, 'publisher')))
        year = field(body, 'year') or (re.search(r'(19|20)\d\d', key) or [''])[0]
        notes = []
        if not field(body, 'year'): notes.append(f'year guessed from key ({year})')
        preprint = bool(PREPRINT.search(journal))
        themes = [t for t, rx in THEMES.items() if re.search(rx, title, re.I)]
        surname = re.sub(r'[^a-z]', '', unicodedata.normalize('NFD', authors[0].split()[-1]).encode('ascii', 'ignore').decode().lower()) if authors else 'anon'
        jslug = '-'.join([w for w in re.sub(r'[^a-z ]', '', journal.lower()).split() if w not in SMALL][:3]) or 'paper'
        stem = base = f'{year}-{surname}-{jslug}'
        n = 2
        while stem in used: stem = f'{base}-{n}'; n += 1
        used.add(stem)
        q = lambda s: '"' + s.replace('\\', '').replace('"', '\\"') + '"'
        lines = ['---', f'title: {q(title)}', 'authors: [' + ', '.join(q(a) for a in authors) + ']']
        if truncated: lines.append('authors_truncated: true   # Scholar export cut the list; paste the full list and remove this line')
        lines += [f'journal: {q(journal)}', f'year: {year}']
        if preprint: lines.append('type: preprint')
        lines.append(f'themes: [{", ".join(themes)}]')
        lines += ['---', '']
        (OUT / f'{stem}.md').write_text('\n'.join(lines))
        written += 1
        if truncated: notes.append('author list truncated; lab-led guessed from first author only')
        if not themes: notes.append('no theme guessed')
        if not field(body, 'author'): notes.append('no authors in export (group author?)')
        if notes: review.append(f'- `{stem}.md`: {title[:90]} — ' + '; '.join(notes))
    pathlib.Path('scripts/import/REVIEW.md').write_text(
        '# Scholar import: entries to check\n\nNo DOIs in the Scholar export: add `doi:` where you want a link.\n\n' + '\n'.join(review) + '\n')
    print(f'wrote {written}, skipped {skipped} already present, {len(review)} flagged for review')

if __name__ == '__main__':
    main()
