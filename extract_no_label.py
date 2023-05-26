import os
import shutil

def extract_unlabeled_images(image_folder, label_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for filename in os.listdir(image_folder):
        image_path = os.path.join(image_folder, filename)
        label_path = os.path.join(label_folder, os.path.splitext(filename)[0] + '.txt')
        # if not os.path.exists(label_path) or os.path.getsize(label_path) == 0:
        if not os.path.exists(label_path):
            output_path = os.path.join(output_folder, filename)
            shutil.copy(image_path, output_path)
            os.remove(image_path)


image_folder = r'E:\labeled\L\PNGImages'
label_folder = r'E:\labeled\L\Annotations'
output_folder = r'E:\labeled\L\no_label'
extract_unlabeled_images(image_folder, label_folder, output_folder)