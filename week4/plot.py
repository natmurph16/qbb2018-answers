#!/usr/bin/env python3

"""
Usage: make plots from data

./plot.py <file>
"""

import sys
import csv
import numpy as np
import matplotlib.pyplot as plt

var_freq = []

for line in open(sys.argv[1]):
    if line[0] == "#":
        continue
    else:
        fields = line.rstrip("\r\n").split("\t")
        info = fields[7]
        if "AF=" in info:
            freq = info.split("=")
            freq2 = freq[1].split(",")
            var_freq.append(float(freq2[0]))
#print(var_freq)

var_freq.sort()

fig, ax = plt.subplots()

ax.hist(var_freq, bins = 100, color = "green")
ax.set_title("Allele Frequency Spectrum")
ax.set_xlabel("Variant Bins")
ax.set_ylabel("Frequency")

fig.savefig("plot.png")
plt.close(fig)
        