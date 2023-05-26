import base64

# 读取图片文件
with open(r"D:\python_project\ultralytics\tests\561AV.png", "rb") as image_file:
    # 将图片转换为base64编码
    encoded_string = base64.b64encode(image_file.read())

# 将base64编码的数据写入文件
with open(r"D:\python_project\ultralytics\tests\output.txt", "wb") as output_file:
    output_file.write(encoded_string)