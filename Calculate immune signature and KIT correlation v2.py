import pandas as pd
import numpy as np
import os
import scipy.stats
from statsmodels.stats.multitest import multipletests


def calculate_signatures(df, goi, data_type):
    datasets= {'CCLE': [['Probeset', '#age', '#cas9_activity', '#ccle_name', '#cell_line_name', '#cell_line_nnmd', '#culture_type', '#id', 
              '#lineage', '#lineage_molecular_subtype', '#lineage_sub_subtype',	'#lineage_subtype',	'#primary_disease',	
              'cancer TCGA 2', '#primary_or_metastasis', '#sample_collection_site',	'#sex',	'#source', 
              '#stripped_cell_line_name', '#subtype'], 'cancer TCGA 2'],
              'Cancer_RX': [['Cell_line_name', 'cancer', 'cancer TCGA', 'cancer TCGA 2', 'tissue'], 'cancer TCGA 2'],
              'R2_tumors': [['Patient', 'Dataset_n', 'Dataset', 'Tumor_type'], 'Tumor_type']}
    cwd= os.getcwd()
    out_path=cwd+'\\Immune_signatures'
    if not os.path.exists(out_path):
        os.mkdir(out_path)
    os.chdir(out_path)
    tumors= list(dict.fromkeys(df[datasets[data_type][1]]))
    for gene in df.drop(datasets[data_type][0], axis=1).columns:
        min_exp= df[gene].min()
        df[gene]= df[gene].apply(lambda x: x-min_exp)
    signatures= list(dict.fromkeys(df_sig['Cell type']))
    for signature in signatures:
        genes= list(set(df_sig[df_sig['Cell type']==signature]['Metagene']) & set(df.columns))
        for ind, row in df.iterrows():
            score= 0
            for gene in genes:
                score += (df.at[ind, gene])**2
            score = score/len(genes)
            df.at[ind, signature]= score
    df.to_excel('Immune_merge_scores_'+data_type+'.xlsx')
    df_padj= pd.DataFrame({'Signature': signatures})
    df_r= pd.DataFrame({'Signature': signatures})
    df_p= pd.DataFrame({'Signature': signatures})    
    for tumor in tumors:
        print(tumor)
        df1= df[df[datasets[data_type][1]]==tumor]
        r_list= list()
        p_list= list()
        for sig in signatures:
            r, p= scipy.stats.pearsonr(df1[goi], df1[sig])
            r_list.append(r)
            p_list.append(p)
        p_adj= multipletests(pvals=p_list, alpha=0.01, method='fdr_tsbky')
        df_r[tumor]= r_list
        df_p[tumor]= p_list
        df_padj[tumor]=p_adj[1]
    n_list=list()
    for tumor in tumors:
        n=0
        for ind, row in df_r.iterrows():
            if (df_padj.at[ind, tumor]<=0.05) & (abs(df_r.at[ind, tumor])>=0.25):
                n+=1
        print('Counted')
        n_list.append(n)
    n_list=['Significant']+n_list
    n_series = pd.Series(n_list, index = df_r.columns)
    df_r = df_r.append(n_series, ignore_index=True)
    df_padj = df_padj.append(n_series, ignore_index=True)
    df_r.to_excel('Immune_sig_corr_'+goi+'_'+data_type+'_R-values.xlsx')
    df_p.to_excel('Immune_sig_corr_'+goi+'_'+data_type+'_p-values.xlsx')
    df_padj.to_excel('Immune_sig_corr_'+goi+'_'+data_type+'_p-values_adj.xlsx')
    os.chdir(work_dir)
    return


work_dir='C:\\Lab\\Python\\shKIT\\'
os.chdir(work_dir)
#data = pd.read_excel('R2_SYK_RTK_Immune_merge_v2.xlsx') CCLE_RTK_Immune_genes_SYK
data = pd.read_excel('R2_SYK_RTK_Immune_merge_v2.xlsx')

df_sig = pd.read_excel('C:\\Lab\\Python\\Datasets\\Immune_signatures_Charoentong-et-al.xlsx')
#calculate_signatures_R2(data, 'SYK', 'Tumor_type')
calculate_signatures(data, 'KIT', 'R2_tumors')
"""
goi='KIT'
data_type='R2_tumors'
df_r=pd.read_excel('Immune_signatures\\Immune_sig_corr_'+goi+'_'+data_type+'_tumors_R-values.xlsx')
df_padj=pd.read_excel('Immune_signatures\\Immune_sig_corr_'+goi+'_'+data_type+'_tumors_p-values_adj.xlsx')
df_r.drop('Unnamed: 0', axis=1, inplace=True)
df_padj.drop('Unnamed: 0', axis=1, inplace=True)
datasets= {'CCLE': [['Probeset', '#age', '#cas9_activity', '#ccle_name', '#cell_line_name', '#cell_line_nnmd', '#culture_type', '#id', 
            '#lineage', '#lineage_molecular_subtype', '#lineage_sub_subtype',	'#lineage_subtype',	'#primary_disease',	
            'cancer TCGA 2', '#primary_or_metastasis', '#sample_collection_site',	'#sex',	'#source', 
            '#stripped_cell_line_name', '#subtype'], 'cancer TCGA 2'],
            'Cancer_RX': [['Cell_line_name', 'cancer', 'cancer TCGA', 'cancer TCGA 2', 'tissue'], 'cancer TCGA 2'],
            'R2_tumors': [['Patient', 'Dataset_n', 'Dataset', 'Tumor_type'], 'Tumor_type']}
tumors= list(dict.fromkeys(data[datasets[data_type][1]]))
df_R=df_r.dropna()
n_list=list()
for tumor in tumors:
    n=0
    for ind, row in df_R.iterrows():
        if (df_padj.at[ind, tumor]<=0.05) & (abs(df_R.at[ind, tumor])>=0.2):
            n+=1
    print('Counted')
    n_list.append(n)
n_list=['Significant']+n_list
n_series = pd.Series(n_list, index = df_R.columns)
df_R = df_R.append(n_series, ignore_index=True)
"""
