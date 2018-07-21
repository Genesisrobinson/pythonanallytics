## working Code compares two files and write it into third file without any issues
## created on 15th June

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Folder='d:/report'
File1='DMP Execution suite1'
File2='DMP Execution suite2'
File3='DMP Execution suite3'
ResultFile='Result_analysis4'

f1 = pd.read_excel(str(Folder) + "/" + str(File1) + ".xls", na_values=['NA'])

f2 = pd.read_excel(str(Folder) + "/" + str(File2) + ".xls", na_values=['NA'])

f3 = pd.read_excel(str(Folder) + "/" + str(File3) + ".xls", na_values=['NA'])

# Make sure we order by account number so the comparisons work

def fileprocess(df1,df2):


    dict1={}
    values1=[]
    count=df1.index
    for lab,i in df1.iterrows():
        bool = False
        for lab1,j in df2.iterrows():
            if df1.loc[lab,'Name'] == df2.loc[lab1,'Name']:
                      df1.loc[lab,str(df1) + "/status"] =df2.loc[lab1,'Status']
                      df1.loc[lab,str(df2) + "/Duration"]=df2.loc[lab1,'uration in ms']
    for lab,i in df2.iterrows():
        bool = False
        for lab1,j in df1.iterrows():
            if df2.loc[lab,'Name'] == df1.loc[lab1,'Name']:
                       bool=True
        if bool == False:
                    df1.loc[lab1+1, 'Name'] = df2.loc[lab,'Name']
                    df1.loc[lab1+1,str(df2) + "/status"] =df2.loc[lab,'Status']
                    df1.loc[lab1+1,str(df2) + "/Duration"]=df2.loc[lab,'uration in ms']

    a=[]
    index=[]
    # ienditying the column index which contains the word "status"
    for x,y in enumerate(df1.columns):
        if "status" in y:
            #print(str(x) + " " + str(y))
            a.append(y)
            index.append(x)


    df1['final'] = np.where((df1.loc[:,df1.columns[index]] == "passed").all(axis=1),"passed","failed")

    print("Total Test Cases" +str(np.count_nonzero(df1['final'])))


    print("Total passed tests " + str(np.count_nonzero(df1["final"]=="passed")))

    print("Total failed tests " + str(np.count_nonzero(df1["final"]=="failed")))

    #extract the df1 dataframe with only selective columns based on index and contan all for passed" if yess assign passed finally do count


    #abc['final'] = np.where((abc == "passed").any(axis=1),"passed","")
    #print("All passed " + str(np.count_nonzero(np.where((df1.loc[:,df1.columns[index]] == "passed").any(axis=1),"passed",""))))

    return df1


result=fileprocess(f1,f2)
result1=fileprocess(result,f3)

writer = pd.ExcelWriter(str(Folder) + "/" + str(ResultFile) + ".xls", engine=None)
result1.to_excel(writer, sheet_name='Sheet1')
writer.save()