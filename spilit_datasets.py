import os
import random
import shutil

def split_labeled_dataset(image_folder, label_folder, target_folder,train_ratio, test_ratio, val_ratio):
    assert train_ratio + test_ratio + val_ratio == 1.0, '拆分比例之和必须等于1'
    assert 0 <= train_ratio <= 1.0 and 0 <= test_ratio <= 1.0 and 0 <= val_ratio <= 1.0, '拆分比例必须在0和1之间'
    # 获取所有图片路径并打乱
    image_list = os.listdir(image_folder)
    random.shuffle(image_list)
    # 计算划分数据集各个类别数量
    train_size = int(len(image_list) * train_ratio)
    test_size = int(len(image_list) * test_ratio)
    val_size = int(len(image_list) * val_ratio)
    # 划分
    train_images = image_list[:train_size]
    test_images = image_list[train_size:train_size+test_size]
    val_images = image_list[train_size+test_size:train_size+test_size+val_size]

    # 创建train、val、test 文件夹
    for folder_name in ['train', 'test', 'val']:
        image_folder_path = os.path.join(target_folder, "images", folder_name)
        label_folder_path = os.path.join(target_folder, "labels", folder_name)
        if not os.path.exists(image_folder_path):
            os.makedirs(image_folder_path)
        if not os.path.exists(label_folder_path):
            os.makedirs(label_folder_path)
    for filename in train_images:
        image_path = os.path.join(image_folder, filename)
        label_path = os.path.join(label_folder, os.path.splitext(filename)[0] + '.txt')
        shutil.copy(image_path, os.path.join(target_folder, "images", 'train', filename))
        shutil.copy(label_path, os.path.join(target_folder, "labels", 'train', os.path.splitext(filename)[0] + '.txt'))
    for filename in test_images:
        image_path = os.path.join(image_folder, filename)
        label_path = os.path.join(label_folder, os.path.splitext(filename)[0] + '.txt')
        shutil.copy(image_path, os.path.join(target_folder, "images", 'test', filename))
        shutil.copy(label_path, os.path.join(target_folder, "labels", 'test',  os.path.splitext(filename)[0] + '.txt'))
    for filename in val_images:
        image_path = os.path.join(image_folder, filename)
        label_path = os.path.join(label_folder, os.path.splitext(filename)[0] + '.txt')
        shutil.copy(image_path, os.path.join(target_folder, "images", 'val', filename))
        shutil.copy(label_path, os.path.join(target_folder, "labels", 'val', os.path.splitext(filename)[0] + '.txt'))


image_folder = r'E:\labeled\e2.0\PNGImages'
label_folder = r'E:\labeled\e2.0\Annotations'
target_folder = r'E:\for_train\second_train_e2.0'
train_ratio = 0.7
test_ratio = 0.1
val_ratio = 0.2
split_labeled_dataset(image_folder, label_folder, target_folder, train_ratio, test_ratio, val_ratio)