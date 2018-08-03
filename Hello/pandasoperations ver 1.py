import pandas as pd
import numpy as np
import xlrd


import matplotlib.pyplot as plt

#df1=xlrd.open_workbook("DMP Execution suite1.xls")
#df1=xlrd.open_workbook("DMP Execution suite1.xls")

df1 = pd.read_excel('DMP Execution suite1.xls', na_values=['NA'])

df2 = pd.read_excel('DMP Execution suite2.xls', na_values=['NA'])
                # Make sure we order by account number so the comparisons work

dict={}
values=[]
y=0
for i in df1.index:
    for j in df1.keys():
        dict[j]=df1[j][i]
    values.append(dict.copy())
df=pd.DataFrame(values)
dict1={}
values1=[]
for i in df.index:
    bool = False
    for j in df2.index:
        if df['Name'][i] == df2['Name'][j]:
                  df.loc[i,'Status1'] =df2['Status'][j]
                  df.loc[i,'Duration1']=df2['uration in ms'][j]

print(df)
writer = pd.ExcelWriter('pandas_result.xls', engine=None)
df.to_excel(writer, sheet_name='Sheet1')
writer.save()