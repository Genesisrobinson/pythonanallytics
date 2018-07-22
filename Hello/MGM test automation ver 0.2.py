

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Folder='d:/report/MGM'
F1='DMP-Regression-Build-90'
#F2='DMP Execution suite2'
#F3='DMP Execution suite3'

def fileprocess(File1):
    try:

        df1 = pd.read_excel(str(Folder) + "/" + str(File1) + ".xls", sheet_name ='Sheet1',na_values=['NA'])
        xlist=list((df1['testclass'].unique().tolist()))
        #print(x)
        dict1={}
        values=[]

        for x in xlist:
            dictflag=False
            Passcount = 0
            Failcount = 0
            for lab, i in df1.iterrows():
                if df1.loc[lab, 'testclass']==x:
                    if dictflag == False:
                        dict1["tcname"]=x
                        dictflag=True
                    if df1.loc[lab,'status']=="PASS":
                        Passcount=Passcount+1
                    elif df1.loc[lab,'status']=="FAIL":
                        Failcount=Failcount+1
            #print(df1.loc[lab]['testclass'])
            dict1["Passcount"]=Passcount
            dict1["Failcount"]=Failcount
            values.append(dict1.copy())

        df3 = pd.DataFrame(values)
        print(df3)

    except ValueError:
       print('Input file types are not proper')

fileprocess(F1)