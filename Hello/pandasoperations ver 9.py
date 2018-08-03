## working Code compares two files and write it into third file without any issues
## created on 15th June
## updated for multiple files in functtion
## Exception Handling
<<<<<<< HEAD
=======
## single write to File
>>>>>>> 420c95fb6c3f0fcdd0e49aaee315a24c0a08af1a

import pandas as pd
import numpy as np


<<<<<<< HEAD
Folder='/Users/genesisrobinson/Documents/Excel'
=======
Folder='d:/report'
>>>>>>> 420c95fb6c3f0fcdd0e49aaee315a24c0a08af1a
F1='DMP Execution suite1'
F2='DMP Execution suite2'
F3='DMP Execution suite3'
F4='DMP Execution suite4'
R1='Result_analysis1'

def fileread(File1):
    df1 = pd.read_excel(str(Folder) + "/" + str(File1) + ".xls", na_values=['NA'])
    return df1

def fileprocess(File1,File2,bool):
    try:
        if bool==False:
            df1=fileread(File1)
            df2=fileread(File2)
        else:
            df2=fileread(File2)
            df1=File1

        dict1={}
        values1=[]
        count=df2.index
        columns=["testcasename"]
        df3=pd.DataFrame(index=count,columns=columns)
        df3=df1
<<<<<<< HEAD




=======
>>>>>>> 420c95fb6c3f0fcdd0e49aaee315a24c0a08af1a
        for lab,i in df1.iterrows():
            bool = False
            for lab1,j in df2.iterrows():
                if df1.loc[lab,'Name'] == df2.loc[lab1,'Name']:
                          df3.loc[lab, "Name"] = df1.loc[lab1, 'Name']
                          df3.loc[lab,str(File2) + "/status"] =df2.loc[lab1,'status']
                          df3.loc[lab,str(File2) + "/Duration"]=df2.loc[lab1,'uration in ms']
        for lab,i in df2.iterrows():
            bool = False
            for lab1,j in df1.iterrows():
                if df1.loc[lab,'Name'] == df1.loc[lab1,'Name']:
                           bool=True
            if bool == False:
                        df3.loc[lab1+1, 'Name'] = df2.loc[lab,'Name']
                        df3.loc[lab1+1,str(File2) + "/status"] =df2.loc[lab,'status']
                        df3.loc[lab1+1,str(File2) + "/Duration"]=df2.loc[lab,'uration in ms']

        a=[]
        index=[]
        # ienditying the column index which contains the word "status"
        for x,y in enumerate(df3.columns):
            if "status" in y:
                #print(str(x) + " " + str(y))
                a.append(y)
                index.append(x)


        df3['final'] = np.where((df3.loc[:,df3.columns[index]] == "passed").all(axis=1),"passed","failed")

        print("Total Test Cases" +str(np.count_nonzero(df3['final'])))


        print("Total passed tests " + str(np.count_nonzero(df3["final"]=="passed")))

        print("Total failed tests " + str(np.count_nonzero(df3["final"]=="failed")))

        #extract the df1 dataframe with only selective columns based on index and contan all for passed" if yess assign passed finally do count


        #abc['final'] = np.where((abc == "passed").any(axis=1),"passed","")
        #print("All passed " + str(np.count_nonzero(np.where((df1.loc[:,df1.columns[index]] == "passed").any(axis=1),"passed",""))))

        return df3
    except ValueError:
        print('Input file types are not proper')

ret1=fileprocess(F2,F1,False)
<<<<<<< HEAD

ret2=fileprocess(ret1,F3,True)


=======
ret2=fileprocess(ret1,F3,True)
>>>>>>> 420c95fb6c3f0fcdd0e49aaee315a24c0a08af1a
ret3=fileprocess(ret2,F4,True)


writer = pd.ExcelWriter(str(Folder) + "/" + str(R1) + ".xls", engine=None)
ret3.to_excel(writer, sheet_name='Sheet1')
writer.save()
<<<<<<< HEAD

=======
>>>>>>> 420c95fb6c3f0fcdd0e49aaee315a24c0a08af1a
