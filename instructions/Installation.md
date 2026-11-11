# IFRA-Cranfield: Intelligent Robotics

## Installation

The steps below must be followed in order to properly set-up a ROS 2 machine which will be used for the Intelligent Robotics short course. It is recommended to install Ubuntu 22.04 Desktop on your PC for a better performance. 

(NOTE): A Virtual Machine (for Windows) will be provided for all those who can't install Ubuntu on their PC. The VM will contain all the required packages for ROS 2 Robot Control and Simulation.

__PC Set-Up for Robot Simulation and Control in ROS 2 Humble__

The ROS 2 packages developed in IFRA-Cranfield/IntelligentRobotics are based on IFRA-Cranfield's [ros2srrc](https://github.com/IFRA-Cranfield/ros2srrc) GitHub Repository. Therefore, ros2srrc must be installed in order to set-up our IR packages in any Ubuntu 22.04 + ROS 2 Humble machine.

Installation steps can be found at: https://github.com/IFRA-Cranfield/ros2srrc/blob/humble/instructions/Installation.md

__Install IntelligentRobotics repository__

```sh
cd ~/dev_ws/src
git clone https://github.com/IFRA-Cranfield/IntelligentRobotics
cd ~/dev_ws
colcon build
```  

__Install additional (required) ROS 2 Packages__

The ABB IRB-120 and UR3 Robots will be used in the Intelligent Robotics Short Course. For that reason, the following resources must be downloaded and installed:

- IRB120-CranfieldRobotics:

    ```sh
    cd ~/dev_ws/src
    git clone https://github.com/IFRA-Cranfield/irb120_CranfieldRobotics
    cd ~/dev_ws
    colcon build
    ```  

- UR3-CranfieldRobotics:

    ```sh
    cd ~/dev_ws/src
    git clone https://github.com/IFRA-Cranfield/ur3_CranfieldRobotics
    cd ~/dev_ws
    colcon build
    ```    

- YOLO and OpenCV will be used to undertake the object detection, pose estimation and pick & place task:

    ```sh
    # Install OpenCV:
    pip install opencv-contrib-python

    # Install YOLO:
    pip install ultralytics
    ```