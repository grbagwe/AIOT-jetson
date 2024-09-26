# AIOT-jetson
 AIOT demo with Jetson nano.


## Topics covered : 

- Introduction to Jetson nano.
- Introduction to github.
- Accessing the jetson nano through ssh.

## Hardware Overview:
![ports](https://files.seeedstudio.com/wiki/recomputer-Jetson-20-1-H1/jetson-a01mark.png)
![carrier board](https://files.seeedstudio.com/wiki/reComputer/reComputerJ101v2.png)

- Complete hardware specifications [link](https://wiki.seeedstudio.com/reComputer_Jetson_Series_Hardware_Layout/#detailed-comparison)

## Task 1 : Assembling the Jetson nano with the peripherals. 
- Connect the Jetson nano developer kit Module  with the carrier board.
![Jetson nano](https://files.seeedstudio.com/wiki/recomputer-Jetson-20-1-H1/reComputerreinstalltion2.jpg)
- Connect the camera ribbon cable to the camera, and to the carrier board.
![camera](https://files.seeedstudio.com/wiki/reComputer-Jetson-Nano/cha.jpg)
- Connect the power cable, wifi dongle, and the ubs-c cable to the data transmission port.
- Connect the power supply, and power on the Jetson nano.

## Task 1.2: (Already done) Installing Jetson nano OS on the SD card. 
- Jetson nano OS ( Jetpack 4.5.1) is already installed on the SD card. Alternatively can be installed using the following steps on the following link [Installing Jetpack](https://wiki.seeedstudio.com/reComputer_J1010_J101_Flash_Jetpack/)

## Task 2 : Accessing the Jetson nano through ssh.
- Knowing the IP address of the Jetson nano.
### For Mac/Linux users :
- use screen command on Mac/Linux terminal to access the Jetson nano.
``` 
screen /dev/tty.usbserial-XXXX 115200 
```
### For Windows users : 
- Use putty to access the Jetson nano.
- Download putty from the following link [Putty](https://www.putty.org/)
- Open putty, and enter the COM port number, and the baud rate (115200).

### Find the IP address of the Jetson nano.
``` 
ifconfig
```
- Username : user1 Password : aiot@2024
- Create additional users, and add them to the sudo group.
```
sudo adduser user2
sudo usermod -aG sudo user2
```
- Login using ssh 

``` 
ssh user1@<ip address>
```



