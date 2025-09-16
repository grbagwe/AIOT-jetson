

You have 3 options to stream  the video from the camera. 

## 1. when using monitor (non-headless)
you can directly open the nvgstcapture-1.0 application to view the camera stream.

```bash
nvgstcapture-1.0 sensor-id=0
```
common mistake is that camera sensor might be connected to port 1, so you need to change the sensor-id to 1.

```bash	
nvgstcapture-1.0 sensor-id=1
```


## 2. When not using the monitor (headless)

you can use gstreamer to stream the video from the camera to your PC.


### ON jetson nano

launch the camera stream using the following command:

```bash
gst-launch-1.0 nvarguscamerasrc ! 'video/x-raw(memory:NVMM), width=1280, height=720, framerate=30/1' ! nvvidconv ! nvv4l2h264enc ! h264parse ! rtph264pay config-interval=1 pt=96 ! udpsink host=you_ip_addres port=5000
```



### ON PC

launch the video stream using the following command:

#### On MacOS install gstreamer
```bash
brew install gstreamer gst-plugins-base gst-plugins-good gst-plugins-bad gst-plugins-ugly gst-libav
```

```bash
gst-launch-1.0 udpsrc port=5000 caps="application/x-rtp, media=video, encoding-name=H264, payload=96" ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink
```

#### For Windows

go to the following link and download the gstreamer for windows: [gstreamer](https://gstreamer.freedesktop.org/download/#windows)

add C:\gstreamer\1.0\x86_64\bin to environment variables

- Press Win + S, type "Environment Variables", and click "Edit the system environment variables".
- In the System Properties window, click "Environment Variables...".
- Add GStreamer to the PATH:

- In the User variables section, find and select Path, then click Edit.

In powershell 

```bash
gst-launch-1.0 --version
```

```bash
gst-launch-1.0 videotestsrc ! autovideosink
```

you may also use a VLC pplyer by following this link [rtp](https://github.com/dusty-nv/jetson-inference/blob/master/docs/aux-streaming.md#rtp)


## 3. Using vnc servero

o setup vnc on the machine: [How to use VNC](https://developer.nvidia.com/embedded/learn/tutorials/vnc-setup)

### 1
```
cd /usr/lib/systemd/user/graphical-session.target.wants
sudo ln -s ../vino-server.service ./.
```

### 2 Configure VNC
```
gsettings set org.gnome.Vino prompt-enabled false
gsettings set org.gnome.Vino require-encryption false
```

### 3 Start VNC
```
gsettings set org.gnome.Vino authentication-methods "['vnc']"
gsettings set org.gnome.Vino vnc-password $(echo -n 'aiot@2020' | base64)
```
### 4 Restart VNC
```
sudo systemctl restart vino-server
```

### 5 Check VNC status
```
sudo systemctl status vino-server
```

### 6 Connect to VNC
- On mac use screen sharing and connect to the IP address of the device
