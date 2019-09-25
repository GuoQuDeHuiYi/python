import shutil
import os

path = input("path:")
files = os.listdir(path)
for f in files:
    folder_name = os.path.join(path, f.split('.')[-1])
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    shutil.move(os.path.join(path, f), folder_name)
