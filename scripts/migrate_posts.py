"""One-time migration of Jekyll _posts into src/content/posts (keeps old URLs via slug)."""
import re, pathlib
src = pathlib.Path('_posts'); dst = pathlib.Path('src/content/posts')
# slug-suffix -> (type, one-line summary for the news feed)
M = {
 'publication-on-local-mutational-processes-in-cancer': ('paper', 'Paper in Genome Biology on local mutational processes in regulatory elements of cancer genomes, with the RM2 method'),
 'preprint-on-mutational-processes': ('preprint', 'Preprint on epigenetic predictors of regional mutagenesis in 2,500 cancer genomes'),
 'new-lab-website': ('update', 'New lab website launched'),
 'system-update': ('update', 'Jüri Reimand promoted to Associate Professor (UofT) and Investigator II (OICR)'),
 'phd-stipends-awarded': ('award', 'Graduate awards to Alec Bahcheli (OGS), Masroor Bayati and Kevin Cheng (MBP Excellence)'),
 'Collaborative-study-on-driver-and-pathway-analysis-in-breast-cancer-published': ('paper', 'Collaborative study on breast cancer drivers and pathways in Nature Communications'),
 'Chistian-Lee-MSc-defence': ('people', 'Christian Lee defended his MSc thesis'),
 'prognostic-cancer-lncRNA-paper-published': ('paper', 'Paper in Cell Reports on the prognostic onco-lncRNA HOXA10-AS in gliomas'),
 'Masroor-qualification-exam': ('people', 'Masroor Bayati passed his PhD qualifying exam'),
 'preprint-published-on-network-rewiring-in-SARS-CoV-2-infection': ('preprint', 'Preprint on genetic rewiring of SARS-CoV-2 phospho-signalling networks'),
 'welcome-to-new-graduate-students': ('people', 'Welcome to new graduate students Zoe Klein, Masoom Mohammad and Michael Slobodyanyuk'),
 'Masroor-OICR-Monday-Talk': ('talk', 'Masroor Bayati spoke at OICR Mondays'),
 'Juri-Seminar-Series-Presentation': ('talk', 'Jüri Reimand seminar at Ryerson University'),
 'publication-on-human-genetics-of-SARS_CoV2-infection': ('paper', 'Paper in Molecular Systems Biology on genetic variants rewiring SARS-CoV-2 signalling networks'),
 'Alec-qualification-exam': ('people', 'Alec Bahcheli passed his PhD qualifying exam'),
 'PPCG-collaboration-on-pathway-based-genetic-biomarkers-of-prostate-cancer': ('paper', 'PPCG collaboration on germline pathway biomarkers of prostate cancer in European Urology'),
 'Kevin-qualification-exam': ('people', 'Kevin Cheng passed his PhD qualifying exam'),
 'Alec-Bahcheli-award-Reimand-Lab-Website': ('award', 'Alec Bahcheli awarded an Ontario Graduate Scholarship'),
 'Mykhaylo-Slobodyanyuk-ISMB-2022-Talk': ('talk', 'Mykhaylo Slobodyanyuk spoke at ISMB 2022'),
 'publication-on-mutational-processes-and-epigenetics-in-cancer': ('paper', 'Paper in PLOS Computational Biology on chromatin accessibility and regional mutational processes'),
 'Juri-Reimand-talk-at-the-EMBO-modularity-meeting': ('talk', 'Jüri Reimand invited talk at the EMBO Modularity meeting'),
 'Reimand-lab-at-the-TFRI-Scientific-Meeting': ('talk', 'Lab at the TFRI Scientific Meeting; flash-talk award to Masroor Bayati'),
 'Collaborative-study-on-RNA-binding-protein-Musashi-1-(MSI1)-published': ('paper', 'Collaborative study on MSI1 in medulloblastoma in Nature Communications'),
 'Diogo-Pellegrina-Congratulations': ('award', 'Diogo Pellegrina awarded a STAGE HostSeq postdoctoral fellowship'),
 'Mykhaylo_CSHL_2023': ('talk', 'Mykhaylo Slobodyanyuk presented a poster at CSHL'),
 'preprint_published_in_biorxiv': ('preprint', 'Preprint on smoking and APOBEC signatures generating stop-gain mutations in cancer'),
 'preprint_published_in_bioRxiv': ('preprint', 'Preprint on the ion permeome in glioblastoma'),
 'research_article_in_frontiers': ('paper', 'Paper in Frontiers in Endocrinology on post-transplant NASH transcriptomes'),
 'GLBIO_poster_2023': ('talk', 'Masroor Bayati and Kevin Cheng presented posters at GLBIO 2023'),
 'research_article_in_nature_communications': ('paper', 'Collaborative study in Nature Communications on CRISPR screens for immunotherapy response in lung cancer'),
 'Alec_Bahcheli_Award': ('award', 'Alec Bahcheli awarded an Ontario Graduate Scholarship'),
 'Masroor_Bayati_Awards': ('award', 'Masroor Bayati awarded the MBP Excellence Award and Caven Fellowship'),
 'Diogo_ICSB_2023': ('talk', 'Diogo Pellegrina spoke at ICSB 2023'),
}
RENAME = {'preprint_published_in_bioRxiv': 'preprint-ion-permeome'}  # avoid case-only clash with ..._biorxiv
IMG = {'/assets/images/research/': '/images/research/', '/assets/images/news_': '/images/news/news_'}
for f in sorted(src.glob('*.md')):
    m = re.match(r'(\d{4}-\d\d-\d\d)-(.*)\.md', f.name); date, slug = m.groups()
    text = f.read_text()
    fm, body = re.match(r'---\n(.*?)\n---\n(.*)', text, re.S).groups()
    title = re.search(r'title:\s*"?(.*?)"?\s*$', fm, re.M).group(1)
    typ, short = M[slug]
    body = re.sub(r'\{:\s*target="_blank"\}', '', body)
    body = re.sub(r'\{:\s*width="\d+px"\}', '', body)
    for a, b in IMG.items(): body = body.replace(a, b)
    body = body.strip() + '\n'
    out = RENAME.get(slug, slug)
    esc = lambda s: s.replace('"', '\\"')
    (dst / f'{out}.md').write_text(
        f'---\ntitle: "{esc(title)}"\ndate: {date}\ntype: {typ}\nshort: "{esc(short)}"\nslug: "{out}"\n---\n\n{body}')
print('migrated', len(list(dst.glob('*.md'))))
