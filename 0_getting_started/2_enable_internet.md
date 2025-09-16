# to enable internet on the jetson device when connected to eduroam network you need do enable the mac address of the device on the network

- go to the [clemson network registration page](https://netregistration.clemson.edu/netreg_public/) and register the mac address of the jetson device. 
- to find the mac address of the jetson device, 
```bash
ifconfig
```
- the mac address is the HWaddr of the wlan0 interface or 
- the mac address of the ethernet interface under eth0

- after registering the mac address, the jetson device should be able to connect to the internet; restart the device if needed

- if the device is still not able to connect to the internet, follow this link [link](https://ccit.clemson.edu/services/network-phones-cable/network/campus-network/)
