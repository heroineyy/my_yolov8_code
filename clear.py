from PIL import Image, ImageFilter

# 打开图像
im = Image.open(r"D:\python_project\CnOCR-master\crop_img\output_1.png")

# 应用锐化滤镜
im_sharp = im.filter(ImageFilter.SHARPEN)

# 保存图像
im_sharp.save("image_sharpened.jpg")
