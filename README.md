# facedetect

## Contact
For any questions or issues regarding this package, please contact Devin Willis at devinwillis@ufl.edu.

## Prerequisites
- Hardware Platform: Jetson Orin Nano
- ROS2 Humble: Make sure you have ROS2 Humble is installed on your system
- OS: Ubuntu 20.04 focal
- L4T Version: nvidia-l4t-core 35.4.1
- Python version: Python 3.8.10

## Overview
This ROS2 package utilizes the Intel RealSense camera package to capture images from the Intel RealSense camera. It then processes the raw camera frames to detect faces and outputs an image with face boxes drawn over it. The processed image is republished for further use. Additionally, the package launches a viewer to display the camera frame along with the detected faces.

## Installation
1. Clone the `facedetect` package into your ROS2 workspace:
    ```bash
    cd /path/to/your/ros2_ws/src
    git clone https://github.com/your_username/facedetect.git
    ```
2. Install realsense camera package ```sudo apt install ros-humble-realsense2-*```

3. Build the package:
    ```bash
    cd /path/to/your/ros2_ws
    colcon build --packages-select facedetect
    ```

## Usage
1. Launch the `facedetect` package:
    ```bash
    source /path/to/your/ros2_ws/install/setup.bash
    source install/local_setup.bash
    ros2 launch facedetect facedetect_launch.py
    ```