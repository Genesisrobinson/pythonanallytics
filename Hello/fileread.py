import glob,os

path = 'd:/report/MGM'

fflag=False
for filename in glob.glob(os.path.join(path, '*.xls')):
     filename=filename.split(path,1)[1]
     filename=filename[1:]
     print(filename)

