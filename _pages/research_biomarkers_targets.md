---
permalink: /research_biomarkers_targets/
title: "Research: biomarkers and target genes"
---
#### Biomarker & target discovery

Large high-throughput datasets of many cancer types are now available with increasingly detailed clinical and lifestyle information of patients. These datasets enable two major translation challenges of cancer research that have potential to improve patients' journeys with cancer. 

First, we need to identify genes and pathways that are potential therapy targets, that is, genes that encode dependencies for the wellfare of cancer cells and that can be ultimately used to develop drugs to treat cancer. Computational identification of these potential therapy targets is only the first step that needs to be followed by thorough experimental characterization of these targets in cell cultures and animal models. 

Second, we need to identify biomarkers, that is, molecular signals in tumors that represent certain disease subtypes, high-risk cancers, or cancers responding to a particular therapy. These biomarkers are called diagnostic, prognostic and predictive markers, respectively. Reliable biomarkers allow us to predict the characteristics of a given tumor and therefore develop personalized oncological approaches to each individual patient based on the genetic and molecular makeup of their tumor. Biomarker discovery is often a machine learning exercise that uses certain datasets for model training and testing and completely separate datasets for model validation.

In our recent work, we set out to discover potential cancer biomarkers and target genes in the non-coding genome among a class of genes called long non-coding RNAs (lncRNAs). There are thousands of non-coding RNAs in the human genome and many of these are expressed in cancer cells, however the vast majority of these remain uncharacterized. 

[![lncRNA_study_overview](/assets/images/research/lncRNA_CellRep_GA.png){: width="500px"}](/assets/images/research/lncRNA_CellRep_GA.png)

We used a systematic machine learning approach to identify individual non-coding RNA genes whose expression was prognostic (that is, indicative of patient survival time). We studied ~30 cancer types and 10,000 cancer samples of the TCGA PanCanAtlas project using elastic net models. This analysis revealed a catalogue of 166 high-confidence lncRNAs with prognostic biomarker properties in cancers. Interestingly, many of these lncRNAs showed switch-like expression and were often highly expressed in high-risk cancers and completely silent in low-risk cancers. There were numerous associations with molecular subtypes and hallmark cancer pathway activities suggesting that the lncRNAs capture patient risk and tumor heterogeneity. 

We focused on one particular lncRNA HOXA10-AS that showed a strong prognostic signal in brain cancer (low grade glioma) and was associated with the expression of neurodevelopmental genes in patient transcriptomes. Our validation efforts indicated this lncRNA as a potential drug target as well as an informative prognostic biomarker, underlining the potential of this integrative analysis. 

On the one hand, the lncRNA HOXA10-AS appears as a potent onco-lncRNA and a potential drug target since its experimental inhibition using shRNAs reduces cancer cell growth while it over-expression increases cancer cell invasion based on our experiments in cell lines, xenografts and organoids. Thus, advanced brain cancer cells may depend on this lncRNA for growth and survival. 

On the other hand, the lncRNA expression helps identify high-risk tumors that associate with poor patient prognosis, as observed in the cohort of brain cancers from TCGA we used for model training, as well as another patient cohort from our collaborators at the Huashan Hospital that we used for model validation. 

*Pan-cancer analysis of non-coding transcripts reveals the prognostic onco-lncRNA HOXA10-AS in gliomas.*  
Keren Isaev\*, Lingyan Jiang\*, Shuai Wu\*, Christian A. Lee, Valérie Watters, Victoire Fort, Ricky Tsai, Fiona J. Coutinho, Samer M.I. Hussein, Jie Zhang, Jinsong Wu, Peter B. Dirks, Daniel Schramek\*, Jüri Reimand\*.  
*Cell Reports* 37 (3), 109873 (2021).  
[link](https://www.cell.com/cell-reports/fulltext/S2211-1247(21)01340-1){:target="_blank"}.














