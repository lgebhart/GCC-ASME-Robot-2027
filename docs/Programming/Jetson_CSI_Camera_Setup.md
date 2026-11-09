# Jetson CSI Camera Setup

## Hardware

- NVIDIA Jetson Orin Nano
- Raspberry Pi Camera Module V2 (IMX219)
- Raspberry Pi CSI camera ribbon cable
- Wi-Fi adapter used to connect the Jetson to the internet
- External monitor, keyboard, and mouse used during setup

## Jetson and Ubuntu

The Jetson runs Ubuntu on an ARM64 system. The camera is connected to the Jetson's CSI camera connector.

The camera sensor used by the Python script is `sensor-id=0`.

## Enable the CSI Camera

1. Connect the IMX219 camera ribbon cable to the Jetson's CSI connector. With the Jetson powered off, check that the ribbon is fully inserted and secured.
2. Open the Jetson's application menu and launch **Jetson-IO**.
3. Select the camera option for the IMX219 camera, then save the configuration and reboot if prompted.
4. After reboot, check that Linux detects the camera:

   ```bash
   v4l2-ctl --list-devices

## Install Software

Install OpenCV and the V4L2 camera tools:

```bash
sudo apt update
sudo apt install python3-opencv v4l-utils

## Clone and Update the Repository

Clone the repository on the Jetson once:

```bash
cd ~
git clone https://github.com/lgebhart/GCC-ASME-Robot-2027.git

## Run the Camera Script

## Troubleshooting

## Notes
