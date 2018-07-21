import matplotlib.pyplot as plt
import numpy as np
a=[10,20,30,40,50,60,70,80,90,100]
b=[1.1,1.2,1.3,1.4,1.5,1.1,1.5,1.6,1.7,1.8]

col={
    10:'RED',
    20:'BLUE',
    30:'RED'
    }

np_bool=np.array(bool)
np_a=np.array(a)
np_bool = np_a > 10

plt.scatter(x=a,y=b,s=np_bool*40,alpha = 0.8)
plt.xlabel("Age Group")
plt.ylabel("Rank")
plt.title("Deep Dive Analysis")
plt.show()