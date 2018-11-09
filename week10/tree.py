#!/usr/bin/env python3

"""
Usage: make plots from data

./tree.py <input_file>
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import ward, dendrogram, linkage, leaves_list

data = []

for line in open(sys.argv[1]):
    fields = line.rstrip("\r\n").split()
    poly = fields[2]
    cfu = fields[1]
    data.append([cfu, poly])
#print(data)

distance = ward(pdist(data))

leaves_list(distance)

fig = plt.figure(figsize = (25, 10))
dn = dendrogram(distance)
fig.savefig("tree.png")
plt.close(fig)