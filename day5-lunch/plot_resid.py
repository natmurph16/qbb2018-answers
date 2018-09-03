#!/usr/bin/env python3

"""
Usage: ./plot_resid.py <t_data.ctab> <no1.tab> <no2.tab> <no3.tab> <no4.tab> <no5.tab>

Plot the residuals of your linear regression model and evaluate
Evaluate this assumption with regard to your data
"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm

df = pd.read_csv(sys.argv[1], sep = "\t", index_col = "t_name")
    
df2 = pd.read_csv(sys.argv[2], sep = "\t", index_col = 0).iloc[:,4]
df3 = pd.read_csv(sys.argv[3], sep = "\t", index_col = 0).iloc[:,4]
df4 = pd.read_csv(sys.argv[4], sep = "\t", index_col = 0).iloc[:,4]
df5 = pd.read_csv(sys.argv[5], sep = "\t", index_col = 0).iloc[:,4]
df6 = pd.read_csv(sys.argv[6], sep = "\t", index_col = 0).iloc[:,4]
#print(df6)
coi = ["FPKM"]
fpkm_df = df.loc[:,coi]

df_final = pd.concat([fpkm_df, df2, df3, df4, df5, df6], axis = 1, ignore_index = True, sort = True)
df_final.rename(index = str, columns = {0 : "FPKMs", 1 : "H3K27ac", 2 : "H3K27me3", 3 : "H3K4me1", 4 : "H3K4me3", 5 : "H3K9ac"}, inplace = True)

#print(fpkm_df)
#print(df_final)

mod = sm.ols(formula = "FPKMs ~ H3K27ac + H3K27me3 + H3K4me1 + H3K4me3 + H3K9ac", data = df_final)
res = mod.fit()
#print(res.summary())
#print(res.resid)

fig, ax = plt.subplots()
plt.hist(res.resid, bins = 1000)
ax.set_title("Histogram of Residuals")
ax.set_xlabel("Bins")
ax.set_ylabel("Number of Transcripts per Residual")
ax.set_xlim(left = -100, right = 300)
fig.savefig("residuals.png")
plt.close(fig)







