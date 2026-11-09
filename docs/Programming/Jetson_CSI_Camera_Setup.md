# Jetson CSI Camera Setup

This guide documents setup and testing of the Raspberry Pi Camera Module V2 on the team’s NVIDIA Jetson Orin Nano.

## Hardware

- NVIDIA Jetson Orin Nano
- Raspberry Pi Camera Module V2 (IMX219)
- Raspberry Pi CSI camera ribbon cable
- AX3000 Wi-Fi adapter used to connect the Jetson to the internet
- External monitor, keyboard, and mouse used during setup
- Jetson power supply

## Jetson and Ubuntu

The Jetson runs Ubuntu on an ARM64 system. The camera connects to the Jetson’s CSI camera connector.

The Python script selects the camera with `sensor-id=0`. It uses NVIDIA’s GStreamer camera source, `nvarguscamerasrc`, rather than opening the CSI camera as a standard USB webcam.

## Enable the CSI Camera

1. Power off the Jetson and check that the camera ribbon cable is fully inserted and secured at both ends.
2. Open the Jetson application menu and launch **Jetson-IO**.
3. Select the available IMX219 camera configuration, save it, and reboot if prompted.
4. After reboot, check whether Linux detects the camera:

   ```bash
   v4l2-ctl --list-devices
   ```

During setup, the camera appeared as an IMX219 device at `/dev/video0`. The Python program accesses it through the Jetson camera pipeline.

## Install Software

Connect the Jetson to the internet, then install OpenCV and the V4L2 camera tools:

```bash
sudo apt update
sudo apt install python3-opencv v4l-utils
```

Check that Python can import OpenCV:

```bash
python3 -c "import cv2; print(cv2.__version__)"
```

An optional camera preview test is:

```bash
nvgstcapture-1.0
```

If that preview opens, stop it with **Ctrl+C** before running the Python program.

## Clone and Update the Repository

Clone the repository on the Jetson once:

```bash
cd ~
git clone https://github.com/lgebhart/GCC-ASME-Robot-2027.git
```

For later updates, go into the existing repository and pull the latest changes:

```bash
cd ~/GCC-ASME-Robot-2027
git pull
```

Run Git commands from inside the cloned repository.

## Bash Helper Script

The repository includes `scripts/jetson_camera.sh` for common Jetson camera tasks. From the repository root, run one of these commands:

```bash
bash scripts/jetson_camera.sh install

## Run the Camera Script

From the repository root, run:

```bash
python3 src/computer_vision/obstacle_course.py
```

The script uses a GStreamer pipeline with `sensor-id=0`, configured for 1920 × 1080 video at 30 frames per second. It displays the camera frame and prints beanbag and pencil template-match confidence scores in the terminal.

Press **Q** while the camera preview window is selected to quit.

The template image filenames in `src/computer_vision/assets/` are case-sensitive on Linux. The script must use the exact filenames:

- `Beanbag.PNG`
- `Pencil.PNG`

## GitHub Update Workflow

1. Edit and save the code or documentation on the development computer.
2. In VS Code **Source Control**, review and stage the intended files.
3. Enter a descriptive commit message, commit the changes, and push or sync them to GitHub.
4. On the Jetson, pull the changes from the repository:

   ```bash
   cd ~/GCC-ASME-Robot-2027
   git pull
   ```

## Troubleshooting

### Python reports `No module named 'cv2'`

Install OpenCV for the system Python:

```bash
sudo apt install python3-opencv
```

### Python cannot load a template image

List the asset filenames:

```bash
ls -l src/computer_vision/assets
```

Check that the script’s image paths match the filenames exactly, including capitalization.

### `git pull` reports “not a git repository”

Go to the cloned repository before pulling:

```bash
cd ~/GCC-ASME-Robot-2027
git pull
```

Running `cd` without a folder returns to the home directory.

### The camera reports “No cameras available”

Check the camera ribbon connection with the Jetson powered off. Confirm that the IMX219 camera configuration is selected in Jetson-IO, save it, and reboot. Then check camera detection:

```bash
v4l2-ctl --list-devices
```

### `apt` reports a DNS or name-resolution error

Connect the Jetson to Wi-Fi, then retry the installation command.

### The beanbag or pencil is not detected

The script only reports a detection when the confidence score reaches its configured threshold. Make sure the target is visible and resembles its template image in size, angle, and lighting. The current thresholds are 0.50 for the beanbag and 0.70 for the pencil.

### Running without a monitor

The current script displays video with `cv2.imshow()` and uses **Q** to quit. It therefore needs a graphical display while running. Headless use requires changing the script’s display and quit handling. The Jetson still needs its power supply.

## Setup Result

Setup was confirmed when the Python program displayed live camera video and printed template-match confidence scores.
