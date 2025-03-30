import torch
import torchvision.models as models


model = torch.load("best_model.pth")
print(model.keys())


model = models.resnet50()
model.load_state_dict(torch.load("best_model.pth"))
print(model)