# Lab 2: Post-Training Quantization on CIFAR-10

This lab demonstrates post-training quantization of a PyTorch model trained on the CIFAR-10 dataset, converting it to a TensorRT INT8 engine, and evaluating its performance.

---

## 1. Train the Model
Train a CIFAR-10 classifier in Google Colab. Save the PyTorch checkpoint:

```python
torch.save(model.state_dict(), "cifar10_model.pt")
```


## 2. Start Docker Container

Launch the Jetson Inference container and mount the local downloads directory:

```
cd jetson-inference
./docker/run.sh -v ~/Downloads/:/Downloads
cd /Downloads
```

## 3. Convert PyTorch to ONNX
```
python3 -m pip install tqdm
python3 get_onnx.py
```
 
## 4. Convert ONNX to TensorRT INT8
```
/usr/src/tensorrt/bin/trtexec \
  --onnx=cifar10_model.onnx \
  --saveEngine=cifar10_model.engine
```

## 5. Evaluate TensorRT Model

```
python3 tensorRT_evaluate.py
```

## 6. Evaluate PyTorch Model
```
python evaluate_pytorch_model.py
```





