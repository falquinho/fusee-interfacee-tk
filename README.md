# Fusée Launcher Interfacée
A very simple GUI for applying [Team {Re}Switched Fusée Launcher script](https://github.com/reswitched/fusee-launcher) onto your Nintendo Switch.


## Disclaimer
* As always, use at your own discretion. I take no reponsibility for any damages caused to your device.
* I'm assuming you understand how the exploit is done and the setup needed, this README is to help you run this specific app.
* Although Fusée is able to exploit any Tegra X1 device, this app is designed to work with Nintendo Switches only.
* The Fusée Launcher script included in this project is slightly modified to be used as a module.


## Running this app
You can run this app as a simple python script or by executing the binary file for your platform.

### Running as a script
* Have latest [python 3](https://www.python.org/downloads/) and [pyusb](https://github.com/pyusb/pyusb) installed.
* __On Windows__ have [libusbk](http://libusbk.sourceforge.net/UsbK3/index.html) as the device driver.
* __On Linux__ have libusb1 installed (you probably already have).
* Download/clone this repo and simply run `app.py` like you would any python script.


### Running the binary file
### Linux
* You need to have `libc ver. 2.61` or higher (if you use a moder distro you probably already have) 
* Download the linux binary from the [releases page](https://github.com/falquinho/fusee-interfacee-tk/releases) and run it. It *should* simply work.

### Windows
* Download the Windows binary from the [releases page](https://github.com/falquinho/fusee-interfacee-tk/releases) and run it. It *should* simply work.


## Using Fusée Launcher Interfacée
The app is very simple, it should be very intuitive to use:
* Click the `Select Payload` button to browse your files and select the desired payload.
* Connect your Switch in RCM mode to the computer. The progress bar will stop and fill up when the device is detected.
* When the `Launch Fusée!` button activate simply click it.
