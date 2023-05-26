import os
import shutil

folder_name= r'E:\demo'

for root, dirs, files in os.walk(folder_name):
    for file in files:
        path = os.path.join(root, file)
        output_path = os.path.join(root, root.split("\\")[-1:].pop()+"-"+file)
        print(path)
        print(output_path)
        shutil.copy(path, output_path)
        os.remove(os.path.join(root, file))