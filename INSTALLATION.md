# IFRA-Cranfield: Intelligent Robotics

## Installation

The steps below must be followed in order to properly set-up a ROS2 machine which will be used for the Intelligent Robotics short course. It is recommended to install Ubuntu 22.04 Desktop on your PC for a better performance. 

(NOTE): A Virtual Machine (for Windows) will be provided for all those who can't install Ubuntu on their PC. The VM will contain all the required packages for ROS2 Robot Control and Simulation.

__PC Set-Up for Robot Simulation and Control in ROS2__

1. Install Ubuntu 22.04: https://ubuntu.com/desktop

2. Install Git:

    ```sh
    # In the terminal shell:
    sudo apt install git

    # Git account configuration:
    git config --global user.name YourUsername
    git config --global user.email YourEmail
    git config --global color.ui true
    git config --global core.editor code --wait # Visual Studio Code is recommended.
    git config --global credential.helper store
    ```

3. Install ROS2 Humble:
    - Follow instructions in: [ROS2 Humble Tutorials - Installation](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html).
    - Source the ROS2.0 Humble installation in the .bashrc file (hidden file in /home):
        ```sh
        source opt/ros/humble/setup.bash
        ```

4. Install MoveIt!2 for ROS2 Humble ([REF: MoveIt!2 Website](https://moveit.picknik.ai/humble/index.html)):

    ```sh
    # Command for BINARY INSTALL (recommended):
    sudo apt install ros-humble-moveit
    ```

    (__NOTE-REQUIRED__): A small improvement of the move_group_interface.h file has been developed in order to execute the Robot/Gripper triggers in this repository. Both the upgraded file and the instructions of how to implement it can be found here: [move_group_interface_improved.h](https://github.com/IFRA-Cranfield/ros2_SimRealRobotControl/tree/humble/include)

5. Create and configure the ROS2.0 Humble ~/dev_ws environment/workspace:
    - Follow instructions in: [ROS2 Humble Tutorials - Create a ROS2 Workspace](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html).
    - Source the ~/dev_ws workspace in .bashrc file:
        ```sh
        source ~/dev_ws/install/local_setup.bash
        ```

6. Install ROS2 packages, which are required for ROS2-based Robot Simulation and Control:

    ```sh
    # ROS2 Control + ROS2 Controllers:
    sudo apt install ros-humble-ros2-control
    sudo apt install ros-humble-ros2-controllers
    sudo apt install ros-humble-gripper-controllers


    # Gazebo for ROS2 Humble:
    sudo apt install gazebo
    sudo apt install ros-humble-gazebo-ros2-control
    sudo apt install ros-humble-gazebo-ros-pkgs

    # xacro:
    sudo apt install ros-humble-xacro

    # Fix cycle time issues in humble-moveit (temporary fix):
    sudo apt install ros-humble-rmw-cyclonedds-cpp 
    # (+) Add into .bashrc file -> export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
    ```   

7. __ABB DRIVER for ROS2__: The installation of the [abb_ros2](https://github.com/PickNikRobotics/abb_ros2) driver is required for the control of any real ABB robot using ROS 2.

    ```sh
    mkdir -p ~/dev_ws/src/ABBDriver
    cd ~/dev_ws/src/ABBDriver
    git clone https://github.com/PickNikRobotics/abb_ros2.git -b rolling
    sudo rosdep init
    rosdep update
    vcs import < abb_ros2/abb.repos
    rosdep install -r --from-paths . --ignore-src --rosdistro $ROS_DISTRO -y
    cd ~/dev_ws
    colcon build
    ```

8. (OPTIONAL) -> __Universal Robots ROS2 Driver__: The installation of the [ur-robot-driver](https://github.com/UniversalRobots/Universal_Robots_ROS2_Driver) is required for the control of any real UR robot using ROS 2. Binary install, for ROS2 Humble:

    ```sh
    sudo apt-get install ros-humble-ur
    ```

9. Import and install the following ROS2 Packages developed by IFRA-Cranfield:

    ```sh
    # IFRA-Cranfield/IFRA_LinkAttacher:
    cd ~/dev_ws/src
    git clone https://github.com/IFRA-Cranfield/IFRA_LinkAttacher.git
    cd ~/dev_ws
    colcon build
    
    # IFRA-Cranfield/IFRA_ObjectPose:
    cd ~/dev_ws/src
    git clone https://github.com/IFRA-Cranfield/IFRA_ObjectPose.git
    cd ~/dev_ws
    colcon build

    # IFRA-Cranfield/IFRA_LinkPose:
    cd ~/dev_ws/src
    git clone https://github.com/IFRA-Cranfield/IFRA_LinkPose.git
    cd ~/dev_ws
    colcon build
    ```

10. Import and install __ros2_SimRealRobotControl__ repository:

    ```sh
    cd ~/dev_ws/src
    git clone https://github.com/IFRA-Cranfield/ros2_SimRealRobotControl
    cd ~/dev_ws
    colcon build
    ```   

11. Import and install IFRA-Cranfield/IntelligentRobotics:

    ```sh
    cd ~/dev_ws/src
    git clone https://github.com/IFRA-Cranfield/IntelligentRobotics
    cd ~/dev_ws
    colcon build
    ```