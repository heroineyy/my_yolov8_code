from PIL import Image
import os
import numpy as np
# 旋转、水平、垂直、缩放

# 数据集路径
dataset_path = r"E:\new_datasets\to_second\E2"

# 扩充后的数据集路径
augmented_path = r"E:\new_datasets\to_second\E22"

# 扩充后的数据集大小
num_augmented_images = 300

# 加载原始图像
images = []
for filename in os.listdir(dataset_path):
    img = Image.open(os.path.join(dataset_path, filename))
    images.append(img)

# 扩充数据集
for i in range(num_augmented_images - len(images)):
    # 随机选择一个原始图像进行增强
    img = images[i % len(images)]

    # # 随机旋转图像
    # angle = np.random.randint(0, 360)
    # rotated_img = img.rotate(180)
    #
    # # 随机水平翻转图像
    # flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    #
    # # 随机垂直翻转图像
    # flipped_img2 = img.transpose(Image.FLIP_TOP_BOTTOM)

    # 随机缩放图像
    scale_factor = np.random.uniform(0.8, 1.2)
    scaled_img = img.resize((int(img.width * scale_factor), int(img.height * scale_factor)))

    # 保存增强后的图像
    # rotated_img.save(os.path.join(augmented_path, f"{i}_rotated.jpg"))
    # flipped_img.save(os.path.join(augmented_path, f"{i}_flipped.jpg"))
    # flipped_img2.save(os.path.join(augmented_path, f"{i}_flipped2.jpg"))
    scaled_img.save(os.path.join(augmented_path, f"{i}_scaled.jpg"))
