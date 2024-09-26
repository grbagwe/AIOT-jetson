# Steaming Video

# Jetson nano

Gstreamer is allready installed on Jetson nano. 
```bash
gst-launch-1.0 nvarguscamerasrc ! 'video/x-raw(memory:NVMM),width=1280,height=720,framerate=30/1' ! nvv4l2h264enc bitrate=4000000 ! rtph264pay config-interval=1 ! udpsink host=<PC-ip-address> port=1234
```




# PC

## 1. Install Gstreamer
### macOS
```bash 
brew install gstreamer gst-plugins-base gst-plugins-good gst-plugins-bad gst-plugins-ugly
``` 
### linux
```bash
sudo apt-get install gstreamer1.0-tools gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav
```

Run 
```bash
gst-launch-1.0 -v udpsrc port=1234 caps="application/x-rtp,media=(string)video,clock-rate=(int)90000,encoding-name=(string)H264,payload=(int)96" ! rtph264depay ! decodebin ! autovideosink
```

# For Windows
## install
```
https://gstreamer.freedesktop.org/data/pkg/windows/1.18.4/gstreamer-1.0-x86_64-1.18.4.msi
```
Run
```bash
gst-launch-1.0 -v udpsrc port=1234 caps="application/x-rtp,media=(string)video,clock-rate=(int)90000,encoding-name=(string)H264,payload=(int)96" ! rtph264depay ! decodebin ! autovideosin
```

