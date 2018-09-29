#!/usr/bin/env python3

"""
Usage: make manhattan plot from data

./manhattan.py <qassoc file> <condition>
"""

import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
        
p = []
pos = []
ch = []
x = []
y = []
c = []

count = 0

for line in open(sys.argv[1]):
    if "SNP" in line or "NA" in line:
        continue
    else:
        fields = line.rstrip("\r\n").split()
        p = -np.log(float(fields[8]))
        pos = float(fields[2])
        ch = fields[0]
        count += 1
        x.append(count)
        y.append(p)
        c.append(ch)
        
fig, ax = plt.subplots()
ax.scatter(x, y, s = 3, alpha = 0.5, color = "black")
plt.axhline(y=-np.log(10e-5), lw = 1, color = "red")
ax.set_ylabel('-log10(p-value)')
ax.set_xlabel('SNP')
ax.set_title(sys.argv[2])
fig.savefig(sys.argv[2] + '.png')
plt.close()

