import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_excel('d:/report/pandas_result.xls', na_values=['NA'])

df2 = pd.read_excel('d:/report/DMP Execution suite1.xls', na_values=['NA'])
                # Make sure we order by account number so the comparisons work

dict1={}
values1=[]
count=df1.index
for i in df1.index:
    bool = False
    for j in df2.index:
        if df1['Name'][i] == df2['Name'][j]:
                  df1.loc[i,'Status4'] =df2['Status'][j]
                  df1.loc[i,'Duration4']=df2['uration in ms'][j]
for i in df2.index:
    bool = False
    for j in df1.index:
        if df2['Name'][i] == df1['Name'][j]:
                   bool=True
    if bool == False:
                temp=i+100
                df1.loc[temp, 'Name'] = df2['Name'][i]
                df1.loc[temp,'Status4'] =df2['Status'][i]
                df1.loc[temp,'Duration4']=df2['uration in ms'][i]



boo=np.logical_and(df1["Status"]=="passed",df1["Status4"]=="passed")

print(df1[boo])

writer = pd.ExcelWriter('d:/report/pandas_result.xls', engine=None)
df1[boo].to_excel(writer, sheet_name='Sheet1')
writer.save()