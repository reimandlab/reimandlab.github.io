---
permalink: /software/
title: "Software"
---

#### ActivePathways

ActivePathways is a method for integrative pathway enrichment analysis of multi-omics datasets. It uses a data fusion approach of P-value merging to prioritize genes and pathways in multiple complementary omics datasets and evaluates the omics evidence supporting each detected pathway and gene. It can be integrated easily with the EnrichmentMap app in Cytoscape to visualize enriched pathways and underlying evidence.  
CRAN: [R package](https://cran.r-project.org/web/packages/ActivePathways/index.html){:target="_blank"}.  
GitHub: [source code](https://github.com/reimandlab/ActivePathways){:target="_blank"}.  
Paper: [Paczkowska, Barenboim et al. Nature Comms 2020](https://www.nature.com/articles/s41467-019-13983-9){:target="_blank"} (with the [PCAWG](https://nature.com/articles/s41586-020-1969-6){:target="_blank"} project).  
[![ActivePathways](/assets/images/research/ActivePathways_overview.png){: width="500px"}](/assets/images/research/ActivePathways_overview.png)


#### ActiveDriverWGS

ActiveDriverWGS is a method for discovering cancer driver mutations in genes and non-coding genomic elements. It uses Poisson regression to identify frequently mutated elements that are potentially positively selected in cancer genomes. The model uses local sequence adjacent to the region of interest to derive expected mutation frequencies and adjusts for trinucleotide sequence and mutation context for improved analysis.  
CRAN: [R package](https://cran.r-project.org/web/packages/ActiveDriverWGS/index.html){:target="_blank"}.  
GitHub: [source code](https://github.com/reimandlab/ActiveDriverWGSR){:target="_blank"}.  
Paper: [Zhu, Uuskula-Reimand, Isaev et al. Molecular Cell 2020](https://www.sciencedirect.com/science/article/pii/S1097276519309578){:target="_blank"}.  
[![ActiveDriverWGS](/assets/images/research/ActiveDriverWGS_overview.png){: width="500px"}](/assets/images/research/ActiveDriverWGS_overview.png)


#### RM2

RM2 is a method to characterize local mutational processes acting on families of genomic elements in cancer genomes. The negative binomial regression model in RM2 evaluates the frequency of somatic mutations in such elements, relative to the background mutation rates in adjacent sequences and also adjusts megabase-scale mutation frequencies as covariates. Optionally, the analysis also considers clinical and genetic properties of the sequencing dataset to find their interactions with localized mutational processes.  
GitHub: [source code](https://github.com/reimandlab/RM2){:target="_blank"}.  
Paper: [Lee, Abd-Rabbo, Reimand. Genome Biol 2021](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-021-02318-x){:target="_blank"}.  
[![RM2](/assets/images/research/RM2.001.png){: width="500px"}](/assets/images/research/RM2.001.png)


#### ActiveDriverDB

ActiveDriverDB is a database for interpreting human genomic variation using cell signalling networks. We analyze missense SNVs (amino acid substitutions) that occur at post-translational modification sites (PTM sites, such as phosphorylation). Somatic cancer mutations, inherited disease mutations, and polymorphic variations in the human genome are included. We evaluate the impact of substitutions on kinase signalling networks by predicting whether the substitutions alter protein sequence motifs bound by kinases and potentially cause rewiring of signalling networks.  
Web server: [www.activeDriverDB.org](https://activedriverdb.org/).  
GitHub: [source code](https://github.com/reimandlab/ActiveDriverDB){:target="_blank"}.  
Original paper: [Krassowski et al. Nucleic Acids Res 2018](https://academic.oup.com/nar/article/46/D1/D901/4566599){:target="_blank"}.  
2021 update paper: [Krassowski et al. Front Cell Dev Biol 2021](https://www.frontiersin.org/articles/10.3389/fcell.2021.626821/full){:target="_blank"}.  
[![ActiveDriverDB](/assets/images/research/ActiveDriverDB_overview.png){: width="500px"}](/assets/images/research/ActiveDriverDB_overview.png)
