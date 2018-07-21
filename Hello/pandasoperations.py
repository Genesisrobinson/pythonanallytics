import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_excel('d:/report/DMP Execution suite.xls', na_values=['NA'])

df2 = pd.read_excel('d:/report/DMP Execution suite1.xls', na_values=['NA'])
                # Make sure we order by account number so the comparisons work

dict={}
values=[]
y=0
for i in df1.index:
    for j in df1.keys():
        dict[j]=df1[j][i]
    values.append(dict.copy())
df=pd.DataFrame(values)
print(df['Name'])
writer = pd.ExcelWriter('d:/report/pandas_result.xls', engine=None)
df.to_excel(writer, sheet_name='Sheet1')
writer.save()