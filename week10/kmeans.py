#!/usr/bin/env python3

"""
Usage: make plots from data

./kmeans.py <input_file>
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import ward, dendrogram, linkage, leaves_list, fcluster
from sklearn.cluster import KMeans
import pandas as pd
import seaborn as sns

d = pd.read_csv('hema_data.txt', sep="\t", index_col='gene')
df = pd.DataFrame(data=d)

kmeans = KMeans(n_clusters = 7)
kmeans.fit(df)
y_kmeans = kmeans.predict(df)

plt.figure()
plt.title("KMeans Clustering")
plt.scatter(df["CFU"], df["poly"], c = y_kmeans, s = 5, cmap = "viridis")
plt.ylabel("poly")
plt.xlabel("CFU")
plt.savefig("kmeans.png")
plt.close