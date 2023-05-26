from ultralytics import YOLO
model = YOLO(r"D:\python_project\ultralytics\runs\detect\train22\weights\last.pt")
model.train(resume=True)
