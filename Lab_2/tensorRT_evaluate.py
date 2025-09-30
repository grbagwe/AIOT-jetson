import torchvision
import torchvision.transforms as T
from torch.utils.data import DataLoader



# Standard CIFAR-10 preprocessing (normalize to [-1,1])
transform = T.Compose([
    T.Resize((32, 32)),   # CIFAR-10 native size
    T.ToTensor(),
    T.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
])

testset = torchvision.datasets.CIFAR10(
    root="./data", train=False, download=True, transform=transform
)
testloader = DataLoader(testset, batch_size=1, shuffle=False)


## 2. Load TensorRT INT8 Engine
import tensorrt as trt
import pycuda.driver as cuda
import pycuda.autoinit
import numpy as np

TRT_LOGGER = trt.Logger(trt.Logger.INFO)

def load_engine(engine_file):
    with open(engine_file, "rb") as f, trt.Runtime(TRT_LOGGER) as runtime:
        return runtime.deserialize_cuda_engine(f.read())

engine = load_engine("cifar10_int8.engine")  # your INT8 model
# engine = load_engine("resnet18_fp32.engine")  # your INT8 model
context = engine.create_execution_context()


## 3. Allocate Buffers

# CIFAR-10 model input: 1 x 3 x 32 x 32
input_shape = (1, 3, 32, 32)
output_shape = (1, 10)  # CIFAR-10 has 10 classes

h_input = np.empty(input_shape, dtype=np.float32)
d_input = cuda.mem_alloc(h_input.nbytes)

h_output = np.empty(output_shape, dtype=np.float32)
d_output = cuda.mem_alloc(h_output.nbytes)

bindings = [int(d_input), int(d_output)]
stream = cuda.Stream()


## 4. Run Inference on CIFAR-10 Test Set
cifar10_classes = [
    "airplane","automobile","bird","cat","deer",
    "dog","frog","horse","ship","truck"
]

correct = 0
total = 0

for images, labels in testloader:
    # Convert torch tensor → numpy
    h_input = images.numpy()
    cuda.memcpy_htod_async(d_input, h_input, stream)

    # Run inference
    context.execute_v2(bindings)

    # Copy output back
    cuda.memcpy_dtoh_async(h_output, d_output, stream)
    stream.synchronize()

    # Prediction
    pred = np.argmax(h_output)
    if pred == labels.item():
        correct += 1
    total += 1

    if total % 1000 == 0:
        print(f"Processed {total}, Accuracy so far: {100*correct/total:.2f}%")

# print(f"Final CIFAR-10 Accuracy: {100*correct/total:.2f}%")
import os
q_size_mb = os.path.getsize("cifar10_int8.engine") / (4 * 1024 * 1024) # simulating this since int8 is not avaialble in tensort


# latency 

start = cuda.Event()
end = cuda.Event()

latencies = []
for images, labels in testloader:
    h_input = images.numpy()
    cuda.memcpy_htod_async(d_input, h_input, stream)

    start.record(stream)
    context.execute_v2(bindings)
    end.record(stream)
    end.synchronize()

    time_ms = start.time_till(end)  # milliseconds
    latencies.append(time_ms)

q_latency_ms = np.mean(latencies)


# accuracy 
q_acc = correct / total


print("\n=== INT8 Results ===")
print(f"Accuracy INT8 : {q_acc*100:.2f}%")
print(f"Size INT8     : {q_size_mb:.2f} MB")
print(f"Latency INT8  : {q_latency_ms:.2f} ms")




