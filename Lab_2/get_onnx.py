import torch
import torchvision.models as models

# Load model (example: ResNet18)
# model = models.resnet18(pretrained=True).eval()
model = torch.load("cifar10_model.pt")
model.eval()

dummy = torch.randn(1, 3, 32, 32)
torch.onnx.export(
    model, dummy, "cifar10_model.onnx",
    input_names=["input"], output_names=["output"],
    opset_version=11,
    dynamic_axes={"input": {0: "batch_size"}, "output": {0: "batch_size"}}
)
