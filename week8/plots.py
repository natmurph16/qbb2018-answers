#!/usr/bin/env python3

"""
Usage: make plots from data

./plot.py <input_file>
"""

import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
from collections import Counter


raw_file = pd.read_csv(sys.argv[1], delim_whitespace = True, header = None)
df_file = pd.DataFrame(raw_file)
df_file_2 = df_file.iloc[:,2]
start_pos = df_file_2.values.tolist()

df_file_3 = df_file.iloc[:,0]
list_range = df_file_3.values.tolist()
sequence_range = []
for i in range(len(list_range)):
    a = list_range[i].split(":")
    b = a[1].split("-")
    c = int(b[1]) - int(b[0])
    sequence_range.append(str(c))


d = np.array(start_pos, dtype = np.float)
e = np.array(sequence_range, dtype = np.float)
f = np.divide(d,e)
data = []
for i in range(len(f)):
    data.append(round(f[i],2))

x_list = [0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13]
y_list = [1, 5, 3, 2, 5, 6, 14, 11, 14, 4, 8, 8, 5, 2]

fig, ax = plt.subplots()

ax.fill_between(x_list, y_list, color = "lightseagreen")
ax.set_xticks([])
ax.set_xlabel("Relative Start Position Along Sequence")
ax.set_ylabel("Frequency")
ax.set_title("Density Plot of Motif Positions")
fig.savefig("final_plot.png")
plt.close(fig)



