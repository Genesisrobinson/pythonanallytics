## Calculating logical conditions in data frame elements
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

name="name"
df1 = pd.read_excel('d:/report/DMP Execution suite.xls', na_values=['NA'])


print(df1.keys())


df1.columns = ['Name1', 'Status1','uration']
print(df1.keys())

