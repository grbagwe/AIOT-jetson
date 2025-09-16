# Demo For pose_estimation on Jetson Nano

# download and install jetson-inference [source](https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md#quick-reference)

```bash

sudo apt-get update
sudo apt-get install git cmake libpython3-dev python3-numpy
git clone --recursive --depth=1 https://github.com/dusty-nv/jetson-inference
cd jetson-inference
mkdir build
cd build
cmake ../
make -j$(nproc)
sudo make install
sudo ldconfig
```


