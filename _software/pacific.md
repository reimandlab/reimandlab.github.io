---
title: PACIFIC
tagline: Interactions between multi-omic features that shape cancer patient outcomes.
order: 5
themes: [biomarkers]
image: /images/research/PACIFIC_example.jpg
links:
  github: https://github.com/reimandlab/PACIFIC
paper: https://aacrjournals.org/mcr/article/23/12/971/767272
---
PACIFIC (Predict and Analyze Combinations of Interacting Features In Cancer) finds robust interactions between two sets of features, such as driver mutations and immune cell abundance in tumours, that together explain patient survival. It combines repeated subsampling with elastic net regression to select the most frequently chosen interactions, and reports ANOVA p-values that control for main effects and baseline clinical covariates. PACIFIC is an R package.

The example shows lung squamous cell carcinomas from TCGA: KMT2D mutations combined with high monocyte levels mark poor survival, while neither feature alone is strongly prognostic.
