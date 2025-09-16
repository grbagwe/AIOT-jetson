
# you can choose you the prebuilt docker container or build from scratch:

## 1. Prebuilt docker container
```
git clone --recursive --depth=1 https://github.com/dusty-nv/jetson-inference
cd jetson-inference
docker/run.sh
```

## 2. Build from scratch 
Follow the instructions below or run the script `install_jetson-inference.sh` in the `scripts` directory.

### Update package lists
```
sudo apt-get update
```

### Install dependencies
```
sudo apt-get install -y git cmake libpython3-dev python3-numpy
```



### Clone the jetson-inference repository with recursive submodules
```
cd /media/sdcard
git clone --recursive --depth=1 https://github.com/dusty-nv/jetson-inference
```

### Change directory to jetson-inference
```
cd jetson-inference
```

### Create a build directory and navigate into it
```
mkdir build
cd build
```

### Configure the build with CMake
```
cmake ../
```

### Compile the code using all available processors
```
make -j$(nproc)
```

### Install the compiled software
```
sudo make install
```

### Update shared library cache
```
sudo ldconfig
```

