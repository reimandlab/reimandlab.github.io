---
title: CAMM
tagline: Deep learning of regional mutation rates in metastases from chromatin accessibility.
order: 6
themes: [drivers]
links:
  github: https://github.com/reimandlab/CAMM
paper: 10.64898/2026.05.24.727503
---
CAMM (Chromatin Accessibility to Metastatic Mutagenesis) is a hierarchical, multi-scale, multi-task neural network that predicts the density of single-nucleotide variants and indels at 1 Mb, 100 kb and 10 kb resolution from chromatin accessibility and replication timing. It is trained on metastatic whole genomes from the Hartwig Medical Foundation and validated on primary tumours from PCAWG.

Genomic windows with more mutations than CAMM expects from the epigenome point to candidate cancer genes. The repository includes the code, trained models for six cancer types, and the public input data. CAMM is written in Python with PyTorch.
