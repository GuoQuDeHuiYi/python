import os
import shutil


def scan_file(path):
    for f in os.listdir(path):
        if f.endswith('.zip'):
            return f


def unzip_it(f, path):
    folder_name = f.split('.')[0]
    target_path = os.path.join(path, folder_name)
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    shutil.unpack_archive(os.path.join(path, f), target_path)


def delete(path, f):
    os.remove(os.path.join(path, f))


path = input("path:")
while True:
    zip_file = scan_file(path)
    if zip_file:
        unzip_it(zip_file, path)
        delete(path, zip_file)
