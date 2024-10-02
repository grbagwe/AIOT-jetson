# Reinstalling OS

Flashing the Jetson nano is not required but often needed for various reasons. The following steps will guide you through the process of flashing the Jetson nano. 
Follow this [link] (https://wiki.seeedstudio.com/reComputer_J1010_J101_Flash_Jetpack/)

- Remember to setup the jetson nano Force recovery mode by connecting pins 3 and 4 on the J40 header using a jumper wire.


# Setting up the SD card

Once the jetson nano is installed, the eemc memory is 16GB and you may want to expand it by adding an sd card. The following steps will guide you through the process of setting up the sd card.
After flashing, the sd card slot might not be enabled by default. To enable the sd card slot. You can check if the sd card slot is enabled by running the following command:
```
lsblk
```
you should see a device under mmcblk1, if not, you can enable the sd card slot by running the following command:
Use this link [link](https://wiki.seeedstudio.com/J101_Enable_SD_Card/)


next, on you terminal, check if the sd card is detected by running the following command:
```
lsblk
```
you should see a new device, usually named mmcblk1, check if it is mounted by running:

if not mounted run the following command:
```
sudo mount /dev/mmcblk1p1 /media/sdcard
```
now you can access the sd card by navigating to /media/sdcard

if the sd card is already mounted, you can access it by navigating to /media/sdcard


modify the fstab file to automatically mount the sd card on boot by running the following command:
``` 
vim /etc/fstab
```

add the following line to the end of the file:
```
/dev/mmcblk1p1 /media/sdcard ext4 defaults 0 2
```

change the permissions of the mount point by running the following command:
```
sudo chown -R $USER:$USER /media/sdcard
```

# check if you can mount the card and use it 
```
sudo mount -a
```
this should run without any errors, DO NOT REBOOT if you see any errors.

Also you should see the mount point in $lsblk$ and $df -h$.

now the sd card will be automatically mounted on boot and you can access it by navigating to /media/sdcard
