Follow this article to setup vnc on the machine: [How to use VNC](https://developer.nvidia.com/embedded/learn/tutorials/vnc-setup)

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
