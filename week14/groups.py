#!/usr/bin/env python

"""
Usage: make plots from data

./groups.py
"""

import sys
import numpy
import scanpy.api as sc
sc.settings.autoshow = False
import matplotlib
matplotlib.use("Agg")

adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
adata.var_names_make_unique()

sc.pp.recipe_zheng17(adata, n_top_genes=1000, log=True, plot=False, copy=False)

sc.pp.neighbors(adata, n_neighbors=15)
sc.tl.louvain(adata, resolution=None)

sc.tl.tsne(adata, n_pcs=None, use_rep=None, perplexity=30, early_exaggeration=12, learning_rate=1000, random_state=0, use_fast_tsne=True, n_jobs=None, copy=False)
sc.pl.tsne(adata, color = "Tubb2b", save = ("tsne_tubb2b"))

sc.tl.umap(adata, min_dist=0.5, spread=1.0, n_components=2, maxiter=None, alpha=1.0, gamma=1.0, negative_sample_rate=5, init_pos='spectral', random_state=0, a=None, b=None, copy=False)
sc.pl.umap(adata, color = "Tubb2b", save = ("umap_tubb2b"))

sc.tl.tsne(adata, n_pcs=None, use_rep=None, perplexity=30, early_exaggeration=12, learning_rate=1000, random_state=0, use_fast_tsne=True, n_jobs=None, copy=False)
sc.pl.tsne(adata, color = "Ackr3", save = ("tsne_ackr3"))

sc.tl.umap(adata, min_dist=0.5, spread=1.0, n_components=2, maxiter=None, alpha=1.0, gamma=1.0, negative_sample_rate=5, init_pos='spectral', random_state=0, a=None, b=None, copy=False)
sc.pl.umap(adata, color = "Ackr3", save = ("umap_ackr3"))

sc.tl.tsne(adata, n_pcs=None, use_rep=None, perplexity=30, early_exaggeration=12, learning_rate=1000, random_state=0, use_fast_tsne=True, n_jobs=None, copy=False)
sc.pl.tsne(adata, color = "Nrxn3", save = ("tsne_nrxn3"))

sc.tl.umap(adata, min_dist=0.5, spread=1.0, n_components=2, maxiter=None, alpha=1.0, gamma=1.0, negative_sample_rate=5, init_pos='spectral', random_state=0, a=None, b=None, copy=False)
sc.pl.umap(adata, color = "Nrxn3", save = ("umap_nrxn3"))

sc.tl.tsne(adata, n_pcs=None, use_rep=None, perplexity=30, early_exaggeration=12, learning_rate=1000, random_state=0, use_fast_tsne=True, n_jobs=None, copy=False)
sc.pl.tsne(adata, color = "Tmsb4x", save = ("tsne_tmsb4x"))

sc.tl.umap(adata, min_dist=0.5, spread=1.0, n_components=2, maxiter=None, alpha=1.0, gamma=1.0, negative_sample_rate=5, init_pos='spectral', random_state=0, a=None, b=None, copy=False)
sc.pl.umap(adata, color = "Tmsb4x", save = ("umap_tmsb4x"))

sc.tl.tsne(adata, n_pcs=None, use_rep=None, perplexity=30, early_exaggeration=12, learning_rate=1000, random_state=0, use_fast_tsne=True, n_jobs=None, copy=False)
sc.pl.tsne(adata, color = "Birc5", save = ("tsne_birc5"))

sc.tl.umap(adata, min_dist=0.5, spread=1.0, n_components=2, maxiter=None, alpha=1.0, gamma=1.0, negative_sample_rate=5, init_pos='spectral', random_state=0, a=None, b=None, copy=False)
sc.pl.umap(adata, color = "Birc5", save = ("umap_birc5"))

sc.tl.tsne(adata, n_pcs=None, use_rep=None, perplexity=30, early_exaggeration=12, learning_rate=1000, random_state=0, use_fast_tsne=True, n_jobs=None, copy=False)
sc.pl.tsne(adata, color = "H3f3a", save = ("tsne_h3f3a"))

sc.tl.umap(adata, min_dist=0.5, spread=1.0, n_components=2, maxiter=None, alpha=1.0, gamma=1.0, negative_sample_rate=5, init_pos='spectral', random_state=0, a=None, b=None, copy=False)
sc.pl.umap(adata, color = "H3f3a", save = ("umap_h3f3a"))


