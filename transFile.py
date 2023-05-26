# #1. 将当前目录下的文件重命名为当前目录的名字+原始文件名
# import os
#
# # 获取当前目录名
# dir_name = os.path.basename(os.getcwd())
#
# # 遍历当前目录下的所有文件
# for filename in os.listdir('.'):
#     # 如果文件名不是当前目录名
#     if filename != dir_name:
#         # 构造新的文件名
#         new_filename = filename.replace(filename, dir_name + '_' + filename)
#         # 重命名文件
#         os.rename(filename, new_filename)



# #2.将原目录中只有两个文件的文件夹移动到指定目录下
# import os
# import shutil
#
# # 获取当前目录和目标目录
#
# #current_dir = os.getcwd()
# source_dir = "E:/QFP"
# target_dir = "E:/chips"
#
# # 列出当前目录下只有两个文件的文件夹
# dirs_with_two_files = [dir for dir in os.listdir(source_dir) if os.path.isdir(os.path.join(source_dir, dir)) and len(os.listdir(os.path.join(source_dir, dir))) == 2]
#
# # 将这些文件夹移动到目标目录下
# for dir in dirs_with_two_files:
#     shutil.move(os.path.join(source_dir, dir), os.path.join(target_dir, dir))
#
# # 输出结果
# print("已将以下文件夹移动到目标目录：")
# for dir in dirs_with_two_files:
#     print(dir)


# #3. 指定目录下遍历所有png图片，将它们重命名为对应文件夹的名字
# import os
# import glob
#
# # 指定目录
# directory = "E:/QFP"
#
# # 遍历指定目录下的所有文件夹
# for folder in os.listdir(directory):
#     # 判断是否为文件夹
#     if os.path.isdir(os.path.join(directory, folder)):
#         # 获取当前文件夹下的所有png图片
#         png_files = glob.glob(os.path.join(directory, folder, "footprint.png"))
#         # 遍历所有png图片，将它们重命名为对应文件夹的名字
#         for png_file in png_files:
#             new_name = os.path.join(directory, folder, folder + ".png")
#             os.rename(png_file, new_name)
#             print(f"已将 {png_file} 重命名为 {new_name}")

## 4.在指定目录下遍历所有footprint.png图片，将它们重命名为对应文件夹的名字
# import os
# import glob
#
# # 指定目录
# directory = "E:/QFP"
#
# # 遍历指定目录下的所有文件夹
# for folder in os.listdir(directory):
#     # 判断是否为文件夹
#     if os.path.isdir(os.path.join(directory, folder)):
#         # 获取当前文件夹下的所有footprint.png图片
#         png_files = glob.glob(os.path.join(directory, folder, "footprint.*"))
#         # 遍历所有footprint.png图片，将它们重命名为对应文件夹的名字
#         for png_file in png_files:
#             new_name = os.path.join(directory, folder, folder + ".png")
#             # 判断新文件名是否已存在，如果已存在则跳过
#             if os.path.exists(new_name):
#                 continue
#             # 重命名文件
#             os.rename(png_file, new_name)
#             print(f"已将 {png_file} 重命名为 {new_name}")

# 5. 将当前文件夹下的所有图片，拷贝到目标目录下
import os
import shutil

# 指定目录和目标目录
directory = "E:/chips"
target_directory = "E:/final_chips"

# 遍历指定目录下的所有文件夹
for folder in os.listdir(directory):
    # 判断是否为文件夹
    if os.path.isdir(os.path.join(directory, folder)):
        # 获取当前文件夹下的所有图片
        image_files = [f for f in os.listdir(os.path.join(directory, folder)) if os.path.isfile(os.path.join(directory, folder, f)) and f == folder + ".png"]
        # 拷贝所有图片到目标目录下
        for image_file in image_files:
            shutil.copy(os.path.join(directory, folder, image_file), os.path.join(target_directory, image_file))
            print(f"已将 {os.path.join(directory, folder, image_file)} 拷贝到 {os.path.join(target_directory, image_file)}")




