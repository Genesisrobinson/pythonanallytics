import glob,os

path = 'd:/report/MGM'

fflag=False
for filename in glob.glob(os.path.join(path, '*.xls')):
   if fflag == False:
        F1=filename
        fflag=True
   else:
        F2=F1
        F1=filename
        print("File1:" + str(F2) + "File2" + str(F1))

