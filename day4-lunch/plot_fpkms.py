#!/usr/bin/env python3

"""
Usage: ./compare_fpkms.py <ctab_file1> <ctab_file2>
"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

name1 = sys.argv[1].split(os.sep)[-2]
fpkm1 = pd.read_csv(sys.argv[1], sep = "\t", index_col = "t_name").loc[:,"FPKM"]

name2 = sys.argv[2].split(os.sep)[-2]
fpkm2 = pd.read_csv(sys.argv[2], sep = "\t", index_col = "t_name").loc[:,"FPKM"]

z = np.polyfit(fpkm1,fpkm2,1)
p = np.poly1d(z)
x = np.linspace(0,10000)

fig, ax= plt.subplots()
ax.scatter(fpkm1, fpkm2, alpha = 0.2, s = 2)
fig.suptitle("FPKM Comparison")
ax.set_xlabel("FPKM1")
ax.set_ylabel("FPKM2")
ax.set_yscale('log')
ax.set_xscale('log')
plt.axis([0.0001, 10000, 0.0001, 10000])
plt.plot(x,p(x), c = "black")
fig.savefig("compare_plot2.png")
plt.close(fig)

#Output file to "compare_plot2.png"