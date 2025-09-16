# Jetson-Inference with Streaming Inference

This guide demonstrates how to set up and use streaming inference with the Jetson-Inference library. Streaming inference allows for real-time processing of video streams, making it ideal for applications such as object detection, image classification, and segmentation.

## Prerequisites
Before you begin, ensure you have the following:
1. Jetson-inference : should be installed  


2. A pi cam (csi camera) or USB camera connected to your Jetson device.


## Image Classification with Streaming Inference
To perform image classification using streaming inference, follow these steps:
1. Open a terminal on your Jetson device.
2. Run the following command to start the image classification demo with streaming inference:
   ```bash
   ./imagenet --network=resnet-18  webrtc://@:8554/output
   ``` 
3. Open a web browser and navigate to `http://<your-jetson-ip>:8554/output` to view the live video stream with classification results.

## Do the same for other models

You can use the same approach for other models such as object detection and segmentation. 

## To know the ip address of your jetson device, run the following command in the terminal:
```bash
 ip addr show
```


