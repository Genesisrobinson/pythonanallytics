

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Folder='/Users/genesisrobinson/Documents/Excel'
F1='DMP-Regression-Build-90'
#F2='DMP Execution suite2'
#F3='DMP Execution suite3'

def fileprocess(File1):
    try:

        df1 = pd.read_excel(str(Folder) + "/" + str(File1) + ".xls", sheet_name ='Sheet1',na_values=['NA'])
        xlist=list((df1['testclass'].unique().tolist()))
        #print(x)
        for lab, i in df1.iterrows():
            for x in xlist:
                if df1.loc[lab, 'testclass']==x:
                    print(df1.loc[lab]['testclass'])

    except ValueError:
       print('Input file types are not proper')

fileprocess(F1)
