import os

def remove_unlabeled_images(image_folder, label_folder):
    for filename in os.listdir(image_folder):
        image_path = os.path.join(image_folder, filename)
        label_path = os.path.join(label_folder, os.path.splitext(filename)[0] + '.txt')
        if os.path.getsize(label_path) == 0:
            print(label_path)
            os.remove(label_path)
            os.remove(image_path)

image_folder = r'E:\chip_datasets4\images\val'
label_folder = r'E:\chip_datasets4\labels\val'

remove_unlabeled_images(image_folder, label_folder)