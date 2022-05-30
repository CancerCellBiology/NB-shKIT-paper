import pandas as pd
import os
import numpy as np
import scipy.stats
from statsmodels.stats.multitest import multipletests

os.chdir('C:\\Lab\\Python\\shKIT')
df= pd.read_excel('NBPAT PAS vs KIT.xlsx')
paths= list(df.drop(['Pathway', 'PRMT1'], axis=1).columns)
x= df['PRMT1']
r_list= list()
p_list= list()
for pw in paths:
    y= df[pw]
    r, p= scipy.stats.pearsonr(x, y)
    #r, p= scipy.stats.spearmanr(x, y)
    r_list.append(r)
    p_list.append(p)
p_adj= multipletests(pvals=p_list, alpha=0.05, method='fdr_tsbky')
result= pd.DataFrame({'Pathway': paths, 'R': r_list, 'p_val': p_list, 'p_adjusted': p_adj[1]})
result.to_excel('NBPAT pathways vs KIT Pearson.xlsx')
    