import os

file_name = input('name:')
suffix = input('suffix:')
path = input('输入文件夹路径：')
files = os.listdir(path)
for f in files:
    if f.endswith(suffix) and file_name in f:
        print('found:' + f)
