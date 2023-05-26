import base64

from ultralytics import YOLO
from ultralytics.yolo.utils.plotting import save_one_box
from ultralytics.yolo.utils.files import increment_path
from PIL import Image
import os

import grpc
import ocr_pb2
import ocr_pb2_grpc
import cv2
import numpy as np

_HOST = '127.0.0.1'
_PORT = '19999'

def re_prediction(crop2):
    if crop2 is None:
        return None
    maxItem = -1
    maxIndex = 0
    for i, crop in enumerate(crop2):
        if maxItem < max(crop.shape[0], crop.shape[1]):
            maxItem = max(crop.shape[0], crop.shape[1])
            maxIndex = i
    return crop2[maxIndex]


def D0():
    print("d0")
    model2 = YOLO(r'D:\python_project\ultralytics\models\D_best.pt')
    return model2


def D1():
    print("d1")
    model2 = YOLO(r'D:\python_project\ultralytics\models\D1_best.pt')
    return model2


def D2():
    print("D2")
    model2 = YOLO(r'D:\python_project\ultralytics\models\D2_best.pt')
    return model2


def E0():
    print("e0")
    model2 = YOLO(r'D:\python_project\ultralytics\models\E0_best.pt')
    return model2


def E1():
    print("e1")
    model2 = YOLO(r'D:\python_project\ultralytics\models\E1_best.pt')
    return model2


def E2():
    print("E2")
    model2 = YOLO(r'D:\python_project\ultralytics\models\E2_best.pt')
    return model2


def e():
    print("e")
    model2 = YOLO(r'D:\python_project\ultralytics\models\e_best.pt')
    return model2


def b():
    print("b")
    model2 = YOLO(r'D:\python_project\ultralytics\models\b_best.pt')
    return model2


def L():
    print("L")
    model2 = YOLO(r'D:\python_project\ultralytics\models\L_best.pt')
    return model2

def call_ocr(max_crop):
    with grpc.insecure_channel("{0}:{1}".format(_HOST, _PORT)) as channel:
        client = ocr_pb2_grpc.OcrStub(channel=channel)
        response = client.CallOcr(ocr_pb2.OcrRequest(img=max_crop))
    print("received: " + response.result)
    return response.result

pre_dict = {
    "D": D0,
    "D1": D1,
    "D2": D2,
    "E0": E0,
    "E1": E1,
    "E2": E2,
    "e": e,
    "b": b,
    "L": L,
}

# 1.加载模型1
model = YOLO(r'D:\python_project\ultralytics\models\first_train.pt')

# 2.第一次预测
pictures = r"D:\python_project\ultralytics\tests\AD2S1200WSTZ.png"
results = model.predict(pictures)
res = []
dir_path = r"D:\python_project\ultralytics\crop_img"
file_name = "crop.jpg"



for result in results:
    # 获取一张图片识别的所有预测框的个数
    i = result.boxes.cls.shape[0]
    cls_arr = list(result.boxes.cls.int().numpy())
    # 获取每个类别的名字列表
    cls_names = []
    for item in cls_arr:
        cls_names.append(result.names[item])
    # 枚举每一行
    crops2ocr = []
    for t in range(0, i):
        # 根据图片中每一个检测框的上下角标裁剪出检测框
        # crop is bgr
        crop = save_one_box(result.boxes.xyxy[t], result.orig_img, save=False)
        cls_name = str(cls_names[t])
        # 根据不同的预测类别获取不同类型的模型
        func_model2 = pre_dict.get(cls_name)
        model2 = func_model2()

        # 第二次预测 source是rgb的格式，预测方法传的图片是rgb,所以要反转一下
        results2 = model2.predict(crop[..., ::-1])
        # 因为只传了一个图片，所以结果只有一个
        ii = results2[0].boxes.cls.shape[0]

        # 存储单张图片识别预测框
        crop2 = []  # cls -> crop2[]# Crop2是rgb
        for tt in range(0, ii):
            crop2.append(save_one_box(results2[0].boxes.xyxy[tt], crop, BGR=True, save=False)[:, :, ::-1])
        # 对crop2中的切割的图片进行筛选，获取最有可能的预测框
        if len(crop2) == 0:
            crop2.append(crop)
        max_crop = re_prediction(crop2)

        # 保存max_crop
        file_name = os.path.join(dir_path, file_name)
        file_name = str(increment_path(file_name).with_suffix('.jpg'))

        Image.fromarray(max_crop).save(file_name, quality=95, subsampling=0)  # save RGB

        # 将图片用base64编码发给服务器
        # 服务器将接受到的文件解码
        max_crop_str=cv2.imencode('.jpg', max_crop)[1].tobytes()
        str_decode=base64.b64encode(max_crop_str)
        target_number = call_ocr(str_decode)
        crops2ocr.append(target_number)
    # 用zip函数打包
    res.append(list(zip(cls_names, crops2ocr)))
print(res)
