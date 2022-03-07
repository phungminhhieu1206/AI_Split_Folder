import os
import numpy as np
import shutil
from pathlib import Path

rootdir_images = '/home/hieuphung/hieupm/data/Images'
rootdir_anotations = '/home/hieuphung/hieupm/data/Annotations'

fileNames = '/home/hieuphung/hieupm/data/Filename/val.txt'
with open(fileNames, "r") as fp:
    read_lines = fp.readlines()

file_imgage_paths = []
file_anotation_paths = []
for line in read_lines:

    file_imgage_paths.append(Path(rootdir_images + '/' + line.replace("\n", ".jpg")))
    file_anotation_paths.append(Path(rootdir_anotations + '/' + line.replace("\n", ".xml")))

# for i in file_anotation_paths:
#     print(i)

# print(len(file_anotation_paths))

for image_name in file_imgage_paths:
  shutil.copy(image_name, '/home/hieuphung/hieupm/data/val')

for anotation_name in file_anotation_paths:
  shutil.copy(anotation_name, '/home/hieuphung/hieupm/data/val')

