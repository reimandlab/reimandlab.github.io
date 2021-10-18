---
permalink: /research/
title: "Research"
---

Our lab focuses on computational biology and cancer research. We analyze large genomics and other -omics datasets of various cancer types using statistical and machine learning approaches. We alo develop new methods to ask unique questions on the data. We occasionally perform functional experiments in close collaborations with experimental labs to validate our most promising findings. Research in the lab falls under three broad themes.

#### Drivers & passengers of the cancer genome

Cancer is a genetic disease caused by somatic mutations in the genome. Single nucleotide variants (SNVs) and other classes of mutations accumulate in the genome over time and through exposures to DNA-damaging agents. Most mutations have little consequence and are often called passengers, while a small minority of mutations called drivers affect critical genes in cells and cause aberrant activity of oncogenic and tumor suppresive pathways in cells.

Recent research in the lab has focused on both drivers and passengers in large whole-genome sequencing datasets.

**For driver mutations**, we recently performed a systematic analysis of potential non-coding drivers in gene-regulatory regions and three-dimensional interaction hubs of the cancer genome using cancer whole-genome sequencing data. We found dozens of potential novel driver mutations and performed functional experiments with CRISPR genome editing and transcriptome-wide profiling to validate one non-coding region controlling the tumor suppressor gene CCNB1IP1. We developed the computational tool ActiveDriverWGS to enable such discovery. 

[![FMRE_graphical_abstract](/assets/images/research/FMRE_graphical_abstract.png){: width="500px"}](/assets/images/research/FMRE_graphical_abstract.png)

*Candidate cancer driver mutations in distal regulatory elements and long-range chromatin interaction networks.*  
Helen Zhu\*, Liis Uusküla-Reimand\*, Keren Isaev\*, .. , Jüri Reimand.  
*Molecular Cell* 77 (6) 1307-1321. e10 (2020)  
[link](https://www.sciencedirect.com/science/article/pii/S1097276519309578){:target="_blank"}.  

**For passenger mutations**, we recently focused on localized mutational processes acting on thousands of gene-regulatory and chromatin architectural elements of the cancer genome. We characterized the potential functional and genetic determinants of mutational processes at binding sites of the CTCF chromatin architectural factor, gene promoter elements and cancer-specific open-chromatin regions. For example, promoters of highly expressed genes and CTCF binding sites epigenetically conserved across many human tissues display the greatest extent of somatic mutagenesis. We also found that certain driver mutations in cancer genomes significantly increase the apparent activity of these mutational processes.

[![RM2_figure.png](/assets/images/research/RM2_figure.png){: width="500px"}](/assets/images/research/RM2_figure.png)

*Functional and genetic determinants of mutation rate variability in regulatory elements of cancer genomes.*  
Christian A Lee\*, Diala Abd-Rabbo\*, Jüri Reimand.  
*Genome Biology* 22 (1), 133 (2021)  
[link](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-021-02318-x){:target="_blank"}.


#### Multi-omics data integration

High-throughput omics techniques allow researchers to profile all molecules in cell in a single experiments. Next-generation sequencing, proteomics and other technologies enable the profiling of different types of molecules, such as DNA mutations, epigenetic modifications, transcript (RNA) and protein expression levels, post-translational modifications of proteins, etc. Researchers often use a combination of these techniques to profile biological samples or even single cells. However, the analysis of resulting datasets is a complex challenge since the various technologies measure different aspects of cellular logic and the datasets are not directly comparable. 

Our lab develops computational tools for multi-omics data integration. We use statistical techniques such as data fusion to jointly analyze multi-omics datasets and prioritize genes, proteins and other features through these datasets. A central tenet of such multi-omics data integration is that important molecular signals detected in multiple datasets should converge to biological pathways and processes. 

Our recently developed method [ActivePathways](https://github.com/reimandlab/ActivePathways){:target="_blank"} combines multiple omics datasets representing either same omics type (e.g., RNA-seq) or multiple types (e.g., RNA-seq and proteomics). ActivePathways prioritizes genes and/or proteins based on their significance in individual datasets, giving a higher score to those genes/proteins that are standing out in multiple datasets. Pathway enrichment analysis of prioritized genes reveals pathways and processes characteristic of these genes, and also shows which of the input datasets contributes to the discovery of each pathway. These complex analyses are often best visualized as enrichment maps. Enrichment maps are network-based visualizations showing groups of similar pathways as subnetworks that are colored by the type of multi-omics evidence underlying the pathways. 

*Integrative pathway enrichment analysis of multivariate omics data.*  
Marta Paczkowska\*, Jonathan Barenboim\*, Nardnisa Sintupisut, Natalie S Fox, Helen Zhu, Diala Abd-Rabbo, Miles W Mee, Paul C Boutros, PCAWG Drivers and Functional Interpretation Working Group, PCAWG Consortium, Jüri Reimand.  
*Nature Communications* 11 (1), 735 (2021)  
[link](https://www.nature.com/articles/s41467-019-13983-9){:target="_blank"}.

In the example below, we jointly analyzed whole-genome sequencing data of human cancers in the PCAWG project and integrated protein-coding and non-coding mutations in potential driver genes. At the top, the enrichment map shows biological processes and pathways with frequent mutations. Each node is an enriched pathway and these are organized into subnetworks such that pathways with many shared genes are linked by edges. Each node (i.e., pathway) is colored based on the evidence, that is, whether it was mostly identified due to protein-coding mutations or non-coding mutations in respective genes or their regulatory elements (promoters, enhancers). In the middle, a specific subnetwork corresponding to developmental processes is shown in detail. At the bottom, genes of one specific process (kidney development) are shown in the context of omics evidence supporting the pathway enrichment. 

[![APW_example-01.png](/assets/images/research/APW_example-01.png){: width="500px"}](/assets/images/research/APW_example-01.png)

We published a comprehensive protocol paper on pathway enrichment analysis of omics datasets in collaboration with Gary Bader's lab (University of Toronto). The paper includes a literature review of pathway analysis of omics data, best practices and current challenges, as well as step-by-step workflows for pathway enrichment analysis and data visualization. 

*Pathway enrichment analysis and visualization of omics data using g:Profiler, GSEA, Cytoscape and EnrichmentMap.*  
Jüri Reimand\*, Ruth Isserlin\*, Veronique Voisin, Mike Kucera, Christian Tannus-Lopes, Asha Rostamianfar, Lina Wadi, Mona Meyer, Jeff Wong, Changjiang Xu, Daniele Merico & Gary D. Bader.  
*Nature Protocols* 14, 482-517 (2019)  
[link](https://www.nature.com/articles/s41596-018-0103-9){:target="_blank"}.

#### Biomarker & target discovery


















