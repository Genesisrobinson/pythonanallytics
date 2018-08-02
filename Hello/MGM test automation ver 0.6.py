#multiple files
#take files automatically from folder

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os,glob



Folder='d:/report/MGM'
R1='d:/report/MGM/Result/Result2'
GlobalBool=False

def dataextract(File1):

    try:
        print("File:" + File1)
        df1= pd.read_excel(File1,sheet_name ='Sheet1',na_values=['NA'])
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
                        if df1.loc[lab,'is-config'] != 1 or df1.loc[lab,'is-config'] ==None :
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

    except ValueError:
       print('Input file types are not proper')

def fileprocess(File1,Fi1e2,nameofthefile):
    try:
        df1=File1
        df2=Fi1e2

        nameofthefile = nameofthefile.split(Folder, 1)[1]
        nameofthefile=nameofthefile[1:]

        if GlobalBool == False:
            print("inside")
            print(df1.keys())
            df1.columns = ['1tcname',str(nameofthefile) + "2passcount", str(nameofthefile)+ "3failcount",str(nameofthefile) +  '4method','5class','6message','7full-stacktrace']
            print(df1.keys())

        df3 = df1

        for lab,i in df1.iterrows():
            bool1 = False
            for lab1,j in df2.iterrows():
                if df1.loc[lab,'1tcname'] == df2.loc[lab1,'1tcname']:
                          df3.loc[lab,str(nameofthefile) + ":passcount"] =df2.loc[lab1,'2passcount']
                          df3.loc[lab,str(nameofthefile) + ":failcount"]=df2.loc[lab1,'3failcount']
                          df3.loc[lab, str(nameofthefile) + ":failcount"] = df2.loc[lab1, '3failcount']
                          df3.loc[lab, str(nameofthefile) + ":message"] = df2.loc[lab1, '6message']
                          df3.loc[lab, str(nameofthefile) + ":full-stacktrace"] = df2.loc[lab1, '7full-stacktrace']
        for lab,i in df2.iterrows():
            bool1 = False
            for lab1,j in df1.iterrows():
                if df2.loc[lab,'1tcname'] == df1.loc[lab1,'1tcname']:
                           bool1=True
            if bool1 == False:
                        df3.loc[lab1+1, '1tcname'] = df2.loc[lab,'1tcname']
                        df3.loc[lab1+1,str(nameofthefile) + ":passcount"] =df2.loc[lab,'2passcount']
                        df3.loc[lab1+1,str(nameofthefile) + ":failcount"]=df2.loc[lab,'3failcount']
                        df3.loc[lab1 + 1, str(nameofthefile) + ":message"] = df2.loc[lab, '6message']
                        df3.loc[lab1 + 1, str(nameofthefile) + ":full-stacktrace"] = df2.loc[lab, '7full-stacktrace']
        return df3

    except ValueError:
        print('Input file types are not proper')

ret=pd.DataFrame
#ret1=pd.DataFrame
#ret2=pd.DataFrame

#ret=fileprocess(F1,F2,False)
#ret1=fileprocess(ret,F3,True)
#ret2=fileprocess(ret1,F4,True)
fflag=False
sflag=False
for filename in glob.glob(os.path.join(Folder, '*.xls')):
    nameofthefile=filename
    filename = dataextract(filename)
    if fflag == False:
        F1 = filename
        fflag = True
    else:
        if sflag == False:
            F2 = F1
            F1 = filename
            ret=fileprocess(F2,F1,nameofthefile)
            sflag=True
            GlobalBool = True
        else:
            F2 = filename
            F1 = ret
            GlobalBool = True
            ret=fileprocess(F1,F2,nameofthefile)

writer = pd.ExcelWriter(R1 + ".xls", engine=None)
ret.to_excel(writer, sheet_name='Sheet1')
writer.save()



