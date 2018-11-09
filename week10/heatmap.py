#!/usr/bin/env python3

"""
Usage: make plots from data

./heatmap.py <input_file>
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import ward, dendrogram, linkage, leaves_list
import seaborn as sns
import pandas as pd

# data = []
#
# for line in open(sys.argv[1]):
#     fields = line.rstrip("\r\n").split()
#     poly = fields[2]
#     cfu = fields[1]
#
#     data.append([cfu, poly])
#print(data)




d = pd.read_csv('hema_data.txt', sep="\t", index_col='gene')
df = pd.DataFrame(data=d)
# df_array = np.array(df)
# data.columns = ["CFU", "poly", "unk", "int", "mys", ""]
# print(df["CFU"])
# print(df.iloc[[0]])
cmap = sns.diverging_palette(220, 20, sep=20, as_cmap=True)

ax = sns.clustermap(df, cmap=cmap)
plt.show()
ax.savefig("heatmap.png")
plt.close(ax)