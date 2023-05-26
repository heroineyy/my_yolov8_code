from PIL import Image
import os

# 指定图片路径
img_path = r'D:\python_project\crnn_seq2seq_ocr_pytorch-master\image'
trarget_img_path=r'D:\python_project\crnn_seq2seq_ocr_pytorch-master\resize_image'

# 获取图片列表
img_list = os.listdir(img_path)
# 循环resize图片
for img_name in img_list:
    # 判断是否为图片文件
    if img_name.endswith('.jpg') or img_name.endswith('.png'):
        # 打开图片
        with Image.open(os.path.join(img_path, img_name)) as img:
            # resize图片
            img_resized = img.resize((280, 32))
            # 保存resize后的图片
            img_resized.save(os.path.join(trarget_img_path, 'resized_' + img_name))
