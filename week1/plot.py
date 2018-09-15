#!/usr/bin/env python3

"""
Usage: Plot dS and dN

./plot.py <mut_type input file> <plot output file>
"""

import sys
import numpy as np
import pandas as pd
import scipy.stats as sp
import matplotlib.pyplot as plt


data = pd.read_csv(sys.argv[1], sep = "\t", header = None, names = ["codon", "dS/dN", "dN-dS"])

p_val = 0.005

x = range(len(data))
y = data["dS/dN"]

#Z-value for Z test using scipy.stats > z value is measure of stddev
z_vals = sp.zscore(data["dN-dS"])
#using z val, get p val > probabilty that value occures randomly
p_vals = 2 * sp.norm.cdf(-1*np.abs(z_vals))

#input the significance to data points
significant_x = [i for i in range(len(p_vals)) if p_vals[i] < p_val]
significant_y = [y[i] for i in significant_x]
nonsig_x = [i for i in range(len(x)) if not i in significant_x]
nonsig_y = [y[i] for i in nonsig_x]


plt.figure()

plt.scatter(nonsig_x, nonsig_y, s=1)
plt.scatter(significant_x, significant_y, s=1, color='black')
plt.xlabel("codons")                 
plt.ylabel("dS/dN")

plt.savefig(sys.argv[2] + ".png")
plt.close()


