import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('d:/Book1.xlsx', sheetname='Sheet1')

print("Column headings:")
print(df.columns)

np_Empid=np.array(df['Empid'])

np_Salary=np.array(df['Salary'])

np_grad=np.array(df['Grade'])

np_twodim=np.vstack((np_Empid,np_Salary)).T
np_twodim1=np.vstack((np_grad,np_Salary)).T

print(np_twodim[:,1])
np_twodim[:,1]=np_twodim[:,1] * 1
print(np_twodim.shape)
print(np_twodim1.shape)

np_twodimfinal=np.vstack((np_twodim,np_twodim1)).T

print(np_twodimfinal.shape)
print (np_twodimfinal)

plt.plot(np_grad,np_Salary)
plt.show()

