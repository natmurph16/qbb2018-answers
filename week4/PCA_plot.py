#!/usr/bin/env python3

"""
Usage: make PCA plot from data

./PCA_plot.py <plink.eigenvec file>
"""

import sys
import csv
import numpy as np
import matplotlib.pyplot as plt

pca1 = []
pca2 = []

for line in open(sys.argv[1]):
    if line.startswith("A"):
        fields = line.rstrip("\r\n").split(" ")
        pca1.append(float(fields[2]))
        pca2.append(float(fields[3]))
        
fig, ax = plt.subplots()
ax.scatter(pca1, pca2)
ax.set_title("SacCer3")
ax.set_xlabel("PCA 1")
ax.set_ylabel("PCA 2")
fig.savefig("PCA_plot.png")
plt.close(fig)