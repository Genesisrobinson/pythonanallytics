import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_excel('d:/report/DMP Execution suite.xlsx', 'DMP', na_values=['NA'])

df2 = pd.read_excel('d:/report/DMP Execution suite1.xlsx', 'DMP', na_values=['NA'])

            # Make sure we order by account number so the comparisons work

values=[]
print(df2.keys())
for i in df1.index:
    bool = False
    for j in df2.index:
        if df2['Name'][j] == df1['Name'][i]:
            bool=True
            dict={
             'Name':df1['Name'][i],
             'Status': df1['Status'][i],
             'Status1':df2['Status'][j],
             }
            values.append(dict)
    if bool == False:
        dict = {
            'Name': df1['Name'][i],
            'Status': df1['Status'][i],
            'Status1': "Null",
        }
        values.append(dict)
for i in df2.index:
    bool = False
    for j in df1.index:
        if df1['Name'][j] == df2['Name'][i]:
            bool=True
    if bool == False:
        dict = {
            'Name': df2['Name'][i],
            'Status':"Null",
            'Status1':df2['Status'][i],
        }
        values.append(dict)
df=pd.DataFrame(values)
writer = pd.ExcelWriter('d:/report/pandas_simple.xls', engine=None)
df.to_excel(writer, sheet_name='Sheet1')
writer.save()