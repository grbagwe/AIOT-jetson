# Jetson-Inference

This document provides instructions for performing inference using the Jetson-Inference library on NVIDIA Jetson devices. The Jetson-Inference library supports various deep learning models for tasks such as image classification, object detection, and segmentation.

## Prerequisites
Before you begin, ensure that you have the following prerequisites:
Jetson-inference: should be already installed on your system (Refer to the installation guide if not installed)
A compatible NVIDIA Jetson device (e.g., Jetson Nano, Jetson Xavier NX, Jetson AGX Xavier)

# Image Classification Inference

To perform image classification inference using a pre-trained model, follow these steps:
1. Open a terminal on your Jetson device.
2. Navigate to the Jetson-Inference directory:
   ```bash
   cd ~/jetson-inference/build/aarch64/bin
   ```
3. Run the image classification example with a pre-trained model (e.g., resnet18):
   ```bash
   $ ./imagenet images/orange_0.jpg images/test/output_0.jpg --model=resnet18
   ``` 
4. The output image with the classification result will be saved in the specified output path (e.g., `images/test/output_0.jpg`).

# Object Detection Inference
To perform object detection inference using a pre-trained model, follow these steps:
1. Open a terminal on your Jetson device.
2. Navigate to the Jetson-Inference directory:
   ```bash
   cd ~/jetson-inference/build/aarch64/bin
   ```
3. Run the object detection example with a pre-trained model (e.g., SSD-Mobilenet-v2):
   ```bash
    ./detectnet.py --network=ssd-mobilenet-v2 images/peds_0.jpg images/test/output.jpg
   ```
4. The output image with the detection results will be saved in the specified output path (e.g., `images/test/output.jpg`).

# Segmentation Inference

To perform segmentation inference using a pre-trained model, follow these steps:
1. Open a terminal on your Jetson device.
2. Navigate to the Jetson-Inference directory:
   ```bash
   cd ~/jetson-inference/build/aarch64/bin
   ```
3. Run the segmentation example with a pre-trained model (e.g., fcn-resnet18):
   ```bash
   ./segnet.py --network=fcn-resnet18-cityscapes images/city_0.jpg images/test/output.jpg
   ```
4. The output image with the segmentation results will be saved in the specified output path (e.g., `images/test/output.jpg`).

# Pose Estimation Inference

To perform pose estimation inference using a pre-trained model, follow these steps:
1. Open a terminal on your Jetson device.
2. Navigate to the Jetson-Inference directory:
   ```bash
   cd ~/jetson-inference/build/aarch64/bin
   ```
3. Run the pose estimation example with a pre-trained model (e.g., openpose):
   ```bash
   ./posenet "images/humans_*.jpg" images/test/pose_humans_%i.jpg
   ```
4. The output images with the pose estimation results will be saved in the specified output path (e.g., `images/test/pose_humans_%i.jpg`).


