import os
import shutil

path = input("path:")
if not os.path.exists(os.path.join(path, 'image')):
    os.makedirs(os.path.join(path, 'image'))
if not os.path.exists(os.path.join(path, 'document')):
    os.makedirs(os.path.join(path, 'document'))

image_suffix = ['jpg', 'png', 'gif']
doc_suffix = ['doc', 'docx', 'ppt', 'md']

for i in image_suffix:
    cur_path = os.path.join(path, i)
    files = os.listdir(cur_path)
    for f in files:
        shutil.move(os.path.join(cur_path, f), os.path.join(path, 'image'))
    os.removedirs(cur_path)
for d in doc_suffix:
    cur_path = os.path.join(path, d)
    files = os.listdir(cur_path)
    for f in files:
        shutil.move(os.path.join(cur_path, f), os.path.join(path, 'document'))
    os.removedirs(cur_path)
