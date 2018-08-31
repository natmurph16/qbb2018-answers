#!/usr/bin/env python3

"""
Usage: ./promoter_approx.py <t_data.ctab>

Determine an approximation of the promoter region for each 
of the transcripts present in SRR072893

Outputs a tab separated .bed file

- ctab: t_id chr strand end t_name ...
- bed : chr start end t_name
"""

import sys
import pandas as pd

# df = pd.read_csv(sys.argv[1], sep = "\t")
#
# p_start = df.loc[:,"start"] - 500
# p_end = df.loc[:,"start"] + 500
#
# df2 = df.assign(p_start = p_start, p_end = p_end)
# # if df2.loc[:,"p_start"] <= 0:
# #     df2.loc[:,"p_start"] = 1
#
# #coi  = columns of interest
# coi = ["chr", "p_start", "p_end", "t_name"]
# df2.loc[:,coi].to_csv(sys.stdout, sep = "\t", index = False)



ctab_file = open(sys.argv[1])

for i, line in enumerate(ctab_file):
    if i == 0:
        continue
    fields = line.rstrip("\r\n").split("\t")
    if fields[2] == "+":
        p_start = int(fields[3]) - 500
        if p_start <= 0:
            p_start = 1
        p_end = int(fields[4]) + 500
    elif fields[2] == "-":
        p_start = int(fields[4]) - 500
        if p_start <= 0:
            p_start = 1
        p_end = int(fields[3]) + 500
    
    
    bed_order = [fields[1], str(p_start), str(p_end), fields[5]]

    print("\t".join(bed_order))
    
#Output file called "SRR07893.bed"




