#!/usr/bin/env python3

"""
Usage: ./timecourse_gene_general.py <samples.csv> <ctab_dir> <gene_name1> <gene_name2> ... <gene_namen>

Create a timecourse of a mean transcript levels for a list of gene names
"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def timecourse2(gender, name):
    df = pd.read_csv(sys.argv[1])
    soi = df.loc[:, "sex"] == gender
    df = df.loc[soi,:]

    all_fpkms = []
    mean_fpkms = []
    for index, sample, sex, stage in df.itertuples():
        filename = os.path.join(sys.argv[2], sample, "t_data.ctab")
        ctab_df = pd.read_table(filename, index_col = "t_name")
        roi = ctab_df.loc[:, "gene_name"] == name
        all_fpkms.append(ctab_df.loc[roi, "FPKM"])
        mean_fpkms.append(np.mean(all_fpkms))
    return mean_fpkms
      
for input_name in sys.argv[4: len(sys.argv)]:
    mean_m_fpkms = timecourse2("male", input_name)
    mean_f_fpkms = timecourse2("female", input_name)

    fig, ax = plt.subplots()
    ax.plot(mean_m_fpkms, c = "blue")
    ax.plot(mean_f_fpkms, c = "red")
    ax.set_xlabel("developmental stage")
    ax.set_ylabel("mRNA abumdance (FPKM)")
    ax.set_title(str(input_name), style = 'italic')

    my_x = ["9", "10", "11", "12", "13", "14a", "14b", "14c", "14d"]
    ax.set_xticklabels(labels = my_x)
    plt.xticks(rotation=90)
    plt.legend(["male", "female"], loc = 'center left', bbox_to_anchor = (1,0.5))
    plt.tight_layout()
    fig.savefig("all_timecourse_" + str(input_name) + ".png")
    plt.close()
