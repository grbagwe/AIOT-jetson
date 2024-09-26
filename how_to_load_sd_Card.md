# insert the microsd card into the slot on the back of the board

# next, on you terminal, check if the sd card is detected by running the following command:
```
lsblk
```
# you should see a new device, usually named mmcblk0, check if it is mounted by running:

# if not mounted run the following command:
```
sudo mount /dev/mmcblk0p1 /media/microsd
```
# now you can access the sd card by navigating to /media/microsd

# if the sd card is already mounted, you can access it by navigating to /media/microsd


# modify the fstab file to automatically mount the sd card on boot by running the following command:
``` 
vim /etc/fstab
```

# add the following line to the end of the file:
```
/dev/mmcblk0p1 /media/microsd ext4 defaults 0 2
```

# change the permissions of the mount point by running the following command:
```
sudo chown -R $USER:$USER /media/microsd
```

# now the sd card will be automatically mounted on boot and you can access it by navigating to /media/microsd
