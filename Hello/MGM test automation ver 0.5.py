#multiple files


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



Folder='d:/report/MGM'
F1='DMP-Regression-Build-88'
F2='DMP-Regression-Build-89'
F3='DMP-Regression-Build-90'
F4='DMP-Regression-Build-91'
R1='d:/report/MGM/Result2'


def dataextract(File1):

    try:
        print ("File name is")
        print(File1)
        df1 = pd.read_excel(str(Folder) + "/" + str(File1) + ".xls", sheet_name ='Sheet1',na_values=['NA'])
        xlist=list((df1['testclass'].unique().tolist()))
        #print(x)
        dict1={}
        values=[]

        for x in xlist:
            dictflag=False
            Passcount = 0
            Failcount = 0
            Errorope=False
            for lab, i in df1.iterrows():
                if df1.loc[lab, 'testclass']==x:
                    if dictflag == False:
                        dict1["1tcname"]=x
                        dictflag=True
                    if df1.loc[lab,'status']=="PASS":
                        Passcount=Passcount+1
                    elif df1.loc[lab,'status']=="FAIL":
                        Failcount=Failcount+1
                        #dict1["message"] = df1.loc[lab, 'message']
                        if df1.loc[lab,'is-config'] != 1 :
                             dict1["6message"] = df1.loc[lab,'message']
                             dict1["7full-stacktrace"] = df1.loc[lab,'full-stacktrace']
                             dict1["4method"]= df1.loc[lab,'method']
                             dict1["5class"]= df1.loc[lab,'testclass']
                             Errorope=True

            #print(df1.loc[lab]['testclass'])
            dict1["2passcount"]=Passcount
            dict1["3failcount"]=Failcount
            if Failcount == 0:
                dict1["6message"] = None
                dict1["7full-stacktrace"] = None
                dict1["4method"] = None
                dict1["5class"] = None
            values.append(dict1.copy())

        df3 = pd.DataFrame(values)
        return df3
        #writer = pd.ExcelWriter(str(Folder) + "/" + str(R1) + ".xls", engine=None)
        #df3.to_excel(writer, sheet_name='Sheet1')
        #writer.save()

    except ValueError:
       print('Input file types are not proper')

def fileprocess(File1,Fi1e2,bool):
    try:
        if bool == False:
            df1=dataextract(File1)
            df2=dataextract(Fi1e2)
        else:
            df2 = dataextract(Fi1e2)
            df1 = File1

        df3=pd.DataFrame
        dict1={}
        values1=[]
        count=df2.index
        columns=["testcasename"]
        df3 = pd.DataFrame(index=count,columns=columns)
        df3=df1

        for lab,i in df1.iterrows():
            bool1 = False
            for lab1,j in df2.iterrows():
                if df1.loc[lab,'1tcname'] == df2.loc[lab1,'1tcname']:
                          df3.loc[lab,str(Fi1e2) + "/passcount"] =df2.loc[lab1,'2passcount']
                          df3.loc[lab,str(Fi1e2) + "/failcount"]=df2.loc[lab1,'3failcount']
                          df3.loc[lab, str(Fi1e2) + "/failcount"] = df2.loc[lab1, '3failcount']
                          df3.loc[lab, str(Fi1e2) + "/message"] = df2.loc[lab1, '6message']
                          df3.loc[lab, str(Fi1e2) + "/full-stacktrace"] = df2.loc[lab1, '7full-stacktrace']
        for lab,i in df2.iterrows():
            bool1 = False
            for lab1,j in df1.iterrows():
                if df2.loc[lab,'1tcname'] == df1.loc[lab1,'1tcname']:
                           bool1=True
            if bool1 == False:
                        df3.loc[lab1+1, 'testcasename'] = df2.loc[lab,'1tcname']
                        df3.loc[lab1+1,str(Fi1e2) + "/passcount"] =df2.loc[lab,'2passcount']
                        df3.loc[lab1+1,str(Fi1e2) + "/failcount"]=df2.loc[lab,'3failcount']
                        df3.loc[lab1 + 1, str(Fi1e2) + "/message"] = df2.loc[lab, '6message']
                        df3.loc[lab1 + 1, str(Fi1e2) + "/full-stacktrace"] = df2.loc[lab, '7full-stacktrace']
        return df3

    except ValueError:
        print('Input file types are not proper')

ret=pd.DataFrame
ret1=pd.DataFrame
ret2=pd.DataFrame

ret=fileprocess(F1,F2,False)
ret1=fileprocess(ret,F3,True)
ret2=fileprocess(ret1,F4,True)


writer = pd.ExcelWriter(str(Folder) + "/" + str(R1) + ".xls", engine=None)
ret2.to_excel(writer, sheet_name='Sheet1')
writer.save()






