import pandas as pd
import numpy as np

df = pd.read_excel('d:/Book1.xlsx', sheetname='Sheet1')

print("Column headings:")
print(df)

np_bool=np.array(bool)

np_salery=np.array(df['Salary'])
np_Empid=np.array(df['Empid'])
np_Empid=array(df['Name1'])

np_bool= np_salery < 1005

print(np_Empid[np_bool])
