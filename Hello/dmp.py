import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_excel('d:/report/DMP Execution suite.xlsx', 'DMP', na_values=['NA'])

df2 = pd.read_excel('d:/report/DMP Execution suite1.xlsx', 'DMP', na_values=['NA'])

            # Make sure we order by account number so the comparisons work


print(df2.keys())
values=[]
for name in df1.Name:
  for name1 in df2.Name:
     if name1 == name:
        value=name1
        values.append(value)

df=pd.DataFrame(values)
writer = pd.ExcelWriter('d:/report/pandas_simple.xls', engine=None)
df.to_excel(writer, sheet_name='Sheet1')
writer.save()


