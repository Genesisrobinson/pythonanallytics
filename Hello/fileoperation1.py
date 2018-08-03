## Calculating logical conditions in data frame elements
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df1 = pd.read_excel('d:/report/MGM/DMP-Regression-Build-87.xls',sheet_name ='Sheet1', na_values=['NA'])

#print(df1.keys())
#print(df1.module)

#df1.module=df1.module.str.slice(0,9)
#df1['module'] = df1['module'].str.extract("\((.*)\)")
#print(df1['module'].str.extract(r'(.*)',expand=False))
#found = re.search('AAA(.+?)ZZZ', text).group(1)
#print(df1['module'].str.extract('(.+?)\('))
print(df1['module'].str.extract('(.+?)\('))
#print(df1.module1)