from ultralytics import YOLO
# import pdb
# pdb.set_trace()
# 加载模型
model = YOLO("yolov8n.yaml")  # 从头开始构建新模型

model = YOLO("yolov8n.pt")  # 加载预训练模型（推荐用于训练）
# pdb.set_trace()
# Use the model
results = model.train(data="../ultralytics/datasets/second_train_e2.0.yaml",epochs=100)

# model = YOLO(r"models/train2/weights/best.pt")
# results = model.val()  # 在验证集上评估模型性能
results = model.predict(source='E:/for_train/second_train_e2.0/images/test', save_crop=True, show=True, conf=0.3, iou=0.8)

# success = model.export(format="onnx")  # 将模型导出为 ONNX 格式

