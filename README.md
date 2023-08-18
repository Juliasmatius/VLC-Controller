# VLC-Controller
Control vlc through a python(can be compiled)
Found a bug? Report it [here](https://github.com/Juliasmatius/VLC-Controller/issues/new)(issues tab).
## Usage
1. Enable VLC http control. [Guide here](https://www.trishtech.com/2021/03/how-to-control-vlc-media-player-from-web-browser/)
2. Download/build the script.
3. Run the main file. You should see a windows like the one below.
![image](https://github.com/Juliasmatius/VLC-Controller/assets/80146546/a89888a5-f7ce-4e44-ba95-d3e2094e96dd)
4. In the "Enter base URL" text box enter the ip address of the pc with vlc. On windows 11 it can be found [here](https://support.microsoft.com/en-us/windows/find-your-ip-address-in-windows-f21a9bbc-c582-55cd-35e0-73431160a1b9#Category=Windows_11) and for windows 10 [here](https://support.microsoft.com/en-us/windows/find-your-ip-address-in-windows-f21a9bbc-c582-55cd-35e0-73431160a1b9#Category=Windows_10).
5. Make sure to add ":8080" on the end of that.
6. In the "Enter password" type the password you set earlier.
7. It should be working now.


## Building from source for windows.
1. Download main.py
2. Run the following command in the folder where main.py is located
```python -m PyInstaller --onefile --name VLC_Controller main.py```
3. Wait. This step can take looong.
4. After the command finishes take a look in /dist. You should see VLC_Controller.exe. Thats your file. Success!
