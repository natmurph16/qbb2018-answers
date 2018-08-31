#!/usr/bin/env python3

"""
Usage: ./ma-plot.py <ctab_file1> <ctab_file2>

Create an ma-plot comparing the FPKMs two samples of your choice
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

m = np.log2((fpkm1+1)/(fpkm2+1))
a = np.log2((fpkm1+1)*(fpkm2+1))*0.5

#print(m)
#print(a)

fig, ax= plt.subplots()
ax.scatter(a, m, alpha = 0.2, s = 2)
fig.suptitle("MA-Plot")
ax.set_xlabel("Mean Expression")
ax.set_ylabel("Log Fold Change")
plt.axhline(y=0, c = "black", lw = 1, alpha = 0.5)
fig.savefig("ma_plot.png")
plt.close(fig)




