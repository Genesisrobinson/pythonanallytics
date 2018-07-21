## working Code compares two files and write it into third file without any issues
## created on 15th June

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df1 = pd.read_excel('d:/report/DMP Execution suite.xls', na_values=['NA'])

df2 = pd.read_excel('d:/report/DMP Execution suite1.xls', na_values=['NA'])
                # Make sure we order by account number so the comparisons work

dict1={}
values1=[]
count=df1.index
for lab,i in df1.iterrows():
    bool = False
    for lab1,j in df2.iterrows():
        if df1.loc[lab,'Name'] == df2.loc[lab1,'Name']:
                  df1.loc[lab,'Status4'] =df2.loc[lab1,'Status']
                  df1.loc[lab,'Duration4']=df2.loc[lab1,'uration in ms']
for lab,i in df2.iterrows():
    bool = False
    for lab1,j in df1.iterrows():
        if df2.loc[lab,'Name'] == df1.loc[lab1,'Name']:
                   bool=True
    if bool == False:
                df1.loc[lab1+1, 'Name'] = df2.loc[lab,'Name']
                df1.loc[lab1+1,'Status4'] =df2.loc[lab,'Status']
                df1.loc[lab1+1,'Duration4']=df2.loc[lab,'uration in ms']



print("Total tests " + str(np.count_nonzero(df1["Name"])))


writer = pd.ExcelWriter('d:/report/pandas_result1.xls', engine=None)
df1.to_excel(writer, sheet_name='Sheet1')
writer.save()