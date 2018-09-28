#!/usr/bin/env python3

"""
Usage: make plots from data

./plot.py <file>
"""

import sys
import csv
import numpy as np
import matplotlib.pyplot as plt

var_depth = []
var_qual = []
var_freq = []

for line in open(sys.argv[1]):
    if line[0] == "#":
        continue
    else:
        fields = line.rstrip("\r\n").split("\t")
        info = fields[7].split(";")
        info2 = fields[9].split(":")
        for var in info:
            if "DP=" in var:
                depth = var.split("=")
                depth2 = depth[1].split(",")
                var_depth.append(float(depth2[0]))
            if "AF=" in var:
                freq = var.split("=")
                freq2 = freq[1].split(",")
                var_freq.append(float(freq2[0]))     
        for val in info2:
            var_qual.append(float(info2[1]))

var_depth.sort()
var_freq.sort()
var_qual.sort()

x, y = np.loadtxt("summary.txt", delimiter = "\t", unpack = True)

labels = ["0", "DOWNSTREAM", "EXON", "INTERGENIC", "INTRON", "SPLICE_SITE_REGION", "UPSTREAM"]

fig, axes = plt.subplots(nrows = 2, ncols = 2, figsize = (20,10))
axes = axes.flatten()

plt.tight_layout(pad = 10)

axes[0].hist(var_depth, bins = 900)
axes[0].set_xlim(0, 250)
axes[0].set_ylim(0, 3500)
axes[0].set_title("Read Depth Distribution")
axes[0].set_xlabel("Variant Bins")
axes[0].set_ylabel("Read Depth")

axes[1].hist(var_freq, bins = 800, color = "green")
axes[1].set_xlim(0, 150)
axes[1].set_ylim(0, 20000)
axes[1].set_title("Allele Frequency Spectrum")
axes[1].set_xlabel("Variant Bins")
axes[1].set_ylabel("Frequency")

axes[2].hist(var_qual, bins = 100, color = "orange")
axes[2].set_xlim(0, 120)
axes[2].set_ylim(0, 35000)
axes[2].set_title("Genotype Quality Distribution")
axes[2].set_xlabel("Variant Bins")
axes[2].set_ylabel("PHRED")

axes[3].bar(x, y, color = "purple")
axes[3].set_xticklabels(labels)
axes[3].set_xlabel("Variant Type")
axes[3].set_ylabel("Percent")

fig.savefig("final_plot.png")
plt.close(fig)
        