#!/usr/bin/env python

"""
Usage: make plots from data

./cells.py
"""

import sys
import numpy
import scanpy.api as sc
sc.settings.autoshow = False
import matplotlib
matplotlib.use("Agg")

adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
adata.var_names_make_unique()

#before filtered PCA
# sc.tl.pca(adata, n_comps=50, zero_center=True, svd_solver='auto', random_state=0, return_info=False, use_highly_variable=None, dtype='float32', copy=False, chunked=False, chunk_size=None)
# sc.pl.pca(adata, save = ("unfiltered"))

#after filtered PCA
# sc.pp.recipe_zheng17(adata, n_top_genes=1000, log=True, plot=False, copy=False)
# sc.tl.pca(adata, n_comps=50, zero_center=True, svd_solver='auto', random_state=0, return_info=False, use_highly_variable=None, dtype='float32', copy=False, chunked=False, chunk_size=None)
# sc.pl.pca(adata, save = ("filtered"))

sc.pp.recipe_zheng17(adata, n_top_genes=1000, log=True, plot=False, copy=False)

sc.pp.neighbors(adata, n_neighbors=15)
sc.tl.louvain(adata, resolution=None)
#
# sc.tl.tsne(adata, n_pcs=None, use_rep=None, perplexity=30, early_exaggeration=12, learning_rate=1000, random_state=0, use_fast_tsne=True, n_jobs=None, copy=False)
# sc.pl.tsne(adata, color = "louvain", save = ("tsne"))
#
# sc.tl.umap(adata, min_dist=0.5, spread=1.0, n_components=2, maxiter=None, alpha=1.0, gamma=1.0, negative_sample_rate=5, init_pos='spectral', random_state=0, a=None, b=None, copy=False)
# sc.pl.umap(adata, color = "louvain", save = ("umap"))

# sc.tl.rank_genes_groups(adata, groupby = "louvain",  method="t-test_overestim_var", corr_method="benjamini-hochberg")
# sc.pl.rank_genes_groups(adata, save = ("genes"))

sc.tl.rank_genes_groups(adata, groupby = "louvain", method="logreg")
sc.pl.rank_genes_groups(adata, save = ("genes_log"))









