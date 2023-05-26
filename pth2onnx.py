import torch
from model import Net

model_test = Net()
model_statedict = torch.load("model_figure_classfiy_e500.pth",map_location=lambda storage,loc:storage)   #导入Gpu训练模型，导入为cpu格式
model_test.load_state_dict(model_statedict)  #将参数放入model_test中
model_test.eval()  # 测试，看是否报错
#下面开始转模型，cpu格式下
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
dummy_input = torch.randn(1, 3, 64, 64,device=device)
input_names = ["input"]
output_names = ["output"]
torch.onnx.export(model_test, dummy_input, "model_.onnx", opset_version=9, verbose=False, output_names=["hm"])

