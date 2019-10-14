# ArmVirtPkg.pug
Build ArmVirtPkg using iPug

## Prerequisites:
1. Python 2.7.10+ or Python 3.7.0+
2. git 2.19.0+


## Generic prerequisites for the UDK build:
1. nasm (2.0 or above)
2. iasl (version 2018xxxx or newer)
3. MSVC(Windows) or Xcode(Mac) or GCC(Open-source Posix)
4. build-essential uuid-dev (Posix)
5. pip2 install future (Python 2.7.x)
6. motc (Xcode)
7. iPug (a Python package, installed through pip)
0. Reference:
    - [Getting Started with EDK II](https://github.com/tianocore/tianocore.github.io/wiki/Getting%20Started%20with%20EDK%20II) 
    - [Xcode](https://github.com/tianocore/tianocore.github.io/wiki/Xcode)
    - [Arm: building-edkii-firmware](https://developer.arm.com/tools-and-software/open-source-software/firmware/edkii-uefi-firmware/building-edkii-firmware)
    - [Googulator's patches for QemuVideoDxe on ARM](https://github.com/Googulator/edk2/commits/NonKVM)
    - [Rafael Rivera's Arm64 build](https://withinrafael.com/2018/02/11/boot-arm64-builds-of-windows-10-in-qemu/)


## Tool installation
1. Debian-Based Linux:
    - `sudo apt update`
    - `sudo apt install nasm iasl build-essential uuid-dev gcc-aarch64-linux-gnu`
    - `pip install ipug --user'`


## Build:
1. `git clone https://github.com/timotheuslin/ArmVirtPkg.pug.git`
2. In the command console, change-directory to folder **ArmVirtPkg.pug**.
3. To build the code, run `make`.
4. Browse to folder **Build/ArmVirtPkg** for the build results.
5. Browse to folder **Build/Conf** for CONF_PATH setting files.
6. Run `make {clean, cleanall}` to clean (all) the intermediate files.


## Known issues:
1. Currently working for Linux/GCC only.
2. ArmVirtPkg contains some video porting issues which need [Googulator's patches for QemuVideoDxe on ARM](https://github.com/Googulator/edk2/commits/NonKVM). Or else the QEMU's video won't be connected.
