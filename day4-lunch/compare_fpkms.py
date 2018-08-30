#!/usr/bin/env python3

"""
Usage: ./compare_fpkms.py <threshold> <ctab_file1> <ctab_file2> ... <ctab_filen>
"""

import sys
import os
import pandas as pd
import numpy as np

t = sys.argv[1]
fpkms = {}

for file in range(2,len(sys.argv)):
    name = sys.argv[file].split(os.sep)[-2]
    fpkm = pd.read_csv(sys.argv[file], sep = "\t", index_col = "t_name").loc[:,"FPKM"]
    fpkms[name] = fpkm
    
fpkms_df = pd.DataFrame(fpkms)
#fpkms_df.to_csv(sys.stdout)

fpkms_df["Sum"] = fpkms_df[list(fpkms_df)].sum(axis = 1)
#print(fpkms_df)

roi = fpkms_df.loc[:,"Sum"] > float(t)
fpkms_df.loc[roi, fpkms_df.columns != "Sum"].to_csv(sys.stdout, sep = "\t")

#Output file to "compare_output"



