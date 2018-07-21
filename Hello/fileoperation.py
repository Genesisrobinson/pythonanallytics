## Calculating logical conditions in data frame elements
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df1 = pd.read_excel('d:/report/Result_analysis2.xls', na_values=['NA'])


a=[]
index=[]
print("all index")
print(df1.columns)
for x,y in enumerate(df1.columns):
    if "status" in y:
        print(str(x) + " " + str(y))
        a.append(y)
        index.append(x)

print("Final" + str(a))

print(df1.columns[index])


boo=[df1.loc[:,df1.columns[index]] == "passed"]
#print(boo)


print("PRINT PRINT")
abc=df1.loc[:,df1.columns[index]]

#print(abc)

abc['final'] = np.where((abc == "passed").any(axis=1),"passed","")

print("All passed" + str(np.count_nonzero(np.where(abc == "passed").any(axis=1),"passed","")))

print("All passed" + str(np.count_nonzero(np.where((df1.loc[:,df1.columns[index]] == "passed").any(axis=1),"passed",""))))

print(abc)

writer = pd.ExcelWriter('d:/report/pandas_resultfinal.xls', engine=None)
abc.to_excel(writer, sheet_name='Sheet1')
writer.save()
