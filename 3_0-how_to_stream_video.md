
# ON jetson nano

launch the camera stream using the following command:

```bash
gst-launch-1.0 nvarguscamerasrc ! 'video/x-raw(memory:NVMM), width=1280, height=720, framerate=30/1' ! nvvidconv ! nvv4l2h264enc ! h264parse ! rtph264pay config-interval=1 pt=96 ! udpsink host=you_ip_addres port=5000
```



# ON PC

launch the video stream using the following command:

## On MacOS install gstreamer
```bash
brew install gstreamer gst-plugins-base gst-plugins-good gst-plugins-bad gst-plugins-ugly gst-libav
```

```bash
gst-launch-1.0 udpsrc port=5000 caps="application/x-rtp, media=video, encoding-name=H264, payload=96" ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink
```

## For Windows

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


