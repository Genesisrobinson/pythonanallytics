

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Folder='/Users/genesisrobinson/Documents/Excel'
F1='DMP-Regression-Build-90'
#F2='DMP Execution suite2'
#F3='DMP Execution suite3'
R1='Result'
<<<<<<< HEAD
=======

>>>>>>> 420c95fb6c3f0fcdd0e49aaee315a24c0a08af1a

def fileprocess(File1):
    global Passcount
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
            Errorope=False
            for lab, i in df1.iterrows():
                if df1.loc[lab, 'testclass']==x:
                    if dictflag == False:
                        dict1["1tcname"]=x
                        dictflag=True
                    if df1.loc[lab,'status']=="PASS":
                        Passcount=Passcount+1
                    elif df1.loc[lab,'status']=="FAIL":
                        Failcount=Failcount+1
                        #dict1["message"] = df1.loc[lab, 'message']
                        if df1.loc[lab,'is-config'] != 1 :
                             dict1["6message"] = df1.loc[lab,'message']
                             dict1["7full-stacktrace"] = df1.loc[lab,'full-stacktrace']
                             dict1["4method"]= df1.loc[lab,'method']
                             dict1["5class"]= df1.loc[lab,'testclass']
                             Errorope=True

            #print(df1.loc[lab]['testclass'])
<<<<<<< HEAD
            dict1["Passcount"]=Passcount
            dict1["Failcount"]=Failcount
=======
            dict1["2passcount"]=Passcount
            dict1["3failcount"]=Failcount
            if Failcount == 0:
                dict1["6message"] = None
                dict1["7full-stacktrace"] = None
                dict1["4method"] = None
                dict1["5class"] = None
            values.append(dict1.copy())
>>>>>>> 420c95fb6c3f0fcdd0e49aaee315a24c0a08af1a

            values.append(dict1.copy())
        #print(values)
        df3 = pd.DataFrame(values)
<<<<<<< HEAD
        print(df3)
        writer = pd.ExcelWriter(str(Folder) + "/" + str(R1) + ".xls", engine=None)
        df3.to_excel(writer, sheet_name='Sheet1')
        writer.save()
=======
        return df3
        #writer = pd.ExcelWriter(str(Folder) + "/" + str(R1) + ".xls", engine=None)
        #df3.to_excel(writer, sheet_name='Sheet1')
        #writer.save()
>>>>>>> 420c95fb6c3f0fcdd0e49aaee315a24c0a08af1a

    except ValueError:
       print('Input file types are not proper')

abc=fileprocess(F1)
print(abc)
writer = pd.ExcelWriter(str(Folder) + "/" + str(R1) + ".xls", engine=None)
abc.to_excel(writer, sheet_name='Sheet1')
writer.save()