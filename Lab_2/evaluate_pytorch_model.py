import torch
import torchvision
import torchvision.transforms as transforms
import torchvision.datasets as datasets
import os
import time
import numpy as np
from tqdm import tqdm

device = "cuda" if torch.cuda.is_available() else "cpu"
print("using device", device)

# load the model
model = torch.load("cifar10_model.pt", map_location=device)
model = model.to(device)
model.eval()

# load the data
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

batch_size = 4
testset = datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=batch_size,
                                         shuffle=False, num_workers=2)

correct = 0
total = 0
latencies = []

# Inference loop
with torch.no_grad():
    for images, labels in tqdm(testloader):
        images, labels = images.to(device), labels.to(device)

        # measure latency
        start = time.time()
        outputs = model(images)
        torch.cuda.synchronize() if device == "cuda" else None
        end = time.time()

        latencies.append((end - start) * 1000.0)  # ms

        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

# Accuracy
q_acc = correct / total

# Model size (MB)
q_size_mb = os.path.getsize("cifar10_model.pt") / (1024 * 1024)# simulating this since int8 is not avaialble in tensort

# Latency (average ms per batch)
q_latency_ms = np.mean(latencies)

print("\n=== full Results ===")
print(f"Accuracy full : {q_acc*100:.2f}%")
print(f"Size full     : {q_size_mb:.2f} MB")
print(f"Latency full: {q_latency_ms:.2f} ms")

