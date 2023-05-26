import os
import re


def remove_chinese_chars(filename):
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    return re.sub(pattern, '', filename)


def rename_files(path):
    for filename in os.listdir(path):
        new_filename = remove_chinese_chars(filename)
        os.rename(os.path.join(path, filename), os.path.join(path, new_filename))


if __name__ == '__main__':
    path = r'E:\dataset3\Annotations'
    rename_files(path)
