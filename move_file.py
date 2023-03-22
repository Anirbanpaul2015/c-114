import os
import shutil
source="C:/Users/ANIRBAN PAUL/Downloads"
distination="C:/Users/ANIRBAN PAUL/OneDrive/drop file here"
listoffiles=os.listdir(source)
for filename in listoffiles:
    name,ext=os.path.splitext(filename)
    print(extention)