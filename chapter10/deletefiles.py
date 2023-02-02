import os

for folderName, subfolders, filenames in os.walk('/home/nikhil/pictures'):
    for filename in filenames:
        path = folderName+"/"+filename
        if int(os.path.getsize(path)) >= 100000000:
            print('Path: '+path+"   "+"Size:"+str(os.path.getsize(path)))