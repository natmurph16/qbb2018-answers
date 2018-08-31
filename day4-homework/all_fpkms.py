#!/usr/bin/env python3

"""
Usage: ./all_fpkms.py <samples.csv> <ctab_dir>

Create a single file all.csv that contains the FPKMs from all 16 samples in samples.csv
"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(sys.argv[1])

fpkms = {}
for index, sample, sex, stage in df.itertuples():
    filename = os.path.join(sys.argv[2], sample, "t_data.ctab")
    ctab = pd.read_table(filename, index_col = "t_name").loc[:,"FPKM"]
    header = str(sex + "_" + stage)
    fpkms[header] = ctab    
    
ctab_all = pd.DataFrame(fpkms)

#print(ctab_all)
    
