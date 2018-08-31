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

fpkm_log = np.log(fpkm_df + 1)

df_final = pd.concat([fpkm_log, df2, df3, df4, df5, df6], axis = 1, ignore_index = True, sort = True)
df_final.rename(index = str, columns = {0 : "FPKM_log", 1 : "tab1", 2 : "tab2", 3 : "tab3", 4 : "tab4", 5 : "tab5"}, inplace = True)

#print(fpkm_df)
#print(df_final)

log_mod = sm.ols(formula = "FPKM_log ~ tab1 + tab2 + tab3 + tab4 + tab5", data = df_final)
log_res = log_mod.fit()
#print(log_res.summary())
#print(log_res.resid)

fig, ax = plt.subplots()
plt.hist(log_res.resid, bins = 100)
ax.set_title("Histogram of Residuals")
ax.set_xlabel("Bins")
ax.set_ylabel("Number of Transcripts per Residual")
ax.set_xlim(-50, 50)
ax.set_ylim(0, 3000)
fig.savefig("log_residuals.png")
plt.close(fig)







