# There are two sets of demos from cuda

# ## CUDA Demos

# The first set of demos are from the CUDA toolkit. These are the demos that are included with the CUDA toolkit. They are located in the `NVIDIA_CUDA-10.0_Samples` directory. The demos are located in the `0_Simple` directory. The demos are compiled using the `make`

Locate the demos in the /usr/local/cuda folder, there will be a file called install-cuda*.sh copy ths to the sd 

```bash
cd /usr/local/cuda/bin
./cuda-install-samples-10.2.sh /media/sdcard
```

# to run the demos
```bash
cd /media/sdcard/NVIDIA_CUDA-10.2_Samples
make -j4
```
or go the each demo and run make
```bash
cd /media/sdcard/NVIDIA_CUDA-10.2_Samples/5_Simulations/nbody
make -j4
```
run the demos using by 
```bash
./nbody
```

# ## vision demos

The second set of demos are from the vision toolkit. These are the demos that are included with the vision toolkit. They are located in the `NVIDIA_VisionWorks-1.6-Samples` directory. The demos are located in the `samples` directory. The demos are compiled using the `cmake`


Locate the demos in the /usr/local/visionworks folder, there will be a file called install-samples.sh copy ths to the sd 

```bash
cd /usr/local/visionworks/sources
./install-samples.sh /media/sdcard
```

if the path does not exist, you can run the following command to install the samples
```bash
sudo apt-get install nvidia-visionworks-samples
```
then follow the steps below to run the demos
```
cd /usr/share/visionworks/sources
./install-samples.sh /media/sdcard
```

# to run the demos
```bash
cd /media/sdcard/VisionWorks-1.6-Samples/bin/aarch64/linux
./nvx_demo_feature_tracker
```

