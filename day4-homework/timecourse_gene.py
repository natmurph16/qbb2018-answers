#!/usr/bin/env python3

"""
Usage: ./timecourse_gene.py <gene_name> <samples.csv> <ctab_dir>

Create a timecourse of a mean transcript levels for a given gene
"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def timecourse2(gender):
    df = pd.read_csv(sys.argv[2])
    soi = df.loc[:, "sex"] == gender
    df = df.loc[soi,:]

    all_fpkms = []
    mean_fpkms = []
    for index, sample, sex, stage in df.itertuples():
        filename = os.path.join(sys.argv[3], sample, "t_data.ctab")
        ctab_df = pd.read_table(filename, index_col = "t_name")
        roi = ctab_df.loc[:, "gene_name"] == sys.argv[1]
        all_fpkms.append(ctab_df.loc[roi, "FPKM"])
        mean_fpkms.append(np.mean(all_fpkms))
    return mean_fpkms
      
mean_m_fpkms = timecourse2("male")
mean_f_fpkms = timecourse2("female")


fig, ax = plt.subplots()
ax.plot(mean_m_fpkms, c = "blue")
ax.plot(mean_f_fpkms, c = "red")
ax.set_xlabel("developmental stage")
ax.set_ylabel("mRNA abumdance (FPKM)")
ax.set_title("Sxl", style = 'italic')

my_x = ["9", "10", "11", "12", "13", "14a", "14b", "14c", "14d"]
ax.set_xticklabels(labels = my_x)
plt.xticks(rotation=90)
plt.legend(["male", "female"], loc = 'center left', bbox_to_anchor = (1,0.5))
plt.tight_layout()
fig.savefig("all_timecourse_Sxl.png")
plt.close()




















