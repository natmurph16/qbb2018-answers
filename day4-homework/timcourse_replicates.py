#!/usr/bin/env python3

"""
Usage: ./timecourse_replicates.py <t_name> <samples.csv> <ctab_dir> <replicates.csv>

Create a timecourse of a given transcript (FBtr0331261) for males and females, and their replicates
Output one plot with both timecourses and their functions
"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

def timecourse(gender):
    df = pd.read_csv(sys.argv[2])
    #soi = samples of interest
    soi = df.loc[:, "sex"] == str(gender)
    df = df.loc[soi,:]

    fpkms = []
    for index, sample, sex, stage in df.itertuples():
        filename = os.path.join(sys.argv[3], sample, "t_data.ctab")
        ctab_df = pd.read_table(filename, index_col = "t_name")
        fpkms.append(ctab_df.loc[sys.argv[1], "FPKM"])
    return fpkms
        
m_fpkms = timecourse("male")
f_fpkms = timecourse("female")


def timecourse_rep(gender):
    df = pd.read_csv(sys.argv[4])
    #soi = samples of interest
    soi = df.loc[:, "sex"] == str(gender)
    df = df.loc[soi,:]

    fpkms = []
    for index, sample, sex, stage in df.itertuples():
        filename = os.path.join(sys.argv[3], sample, "t_data.ctab")
        ctab_df = pd.read_table(filename, index_col = "t_name")
        fpkms.append(ctab_df.loc[sys.argv[1], "FPKM"])
    return fpkms
        
rep_m_fpkms = timecourse_rep("male")
rep_f_fpkms = timecourse_rep("female")


my_x = ["9", "10", "11", "12", "13", "14a", "14b", "14c", "14d"]
    
fig, ax = plt.subplots()
ax.plot(m_fpkms, c = "blue")
ax.plot(f_fpkms, c = "red")
ax.plot([4,5,6,7], rep_m_fpkms, c = "green")
ax.plot([4,5,6,7], rep_f_fpkms, c = "orange")
ax.set_title("FBtr0331261", style = 'italic')
ax.set_xlabel("developmental stage")
ax.set_ylabel("mRNA abumdance (FPKM)")
ax.set_xticklabels(labels = my_x)
plt.xticks(rotation=90)
#plt.subplots_adjust(left = 0.1)
plt.legend(["male", "female", "male reps", "female reps"], loc = 'center left', bbox_to_anchor = (1,0.5))
plt.tight_layout()
fig.savefig("all_timecourse_reps.png")
plt.close()

