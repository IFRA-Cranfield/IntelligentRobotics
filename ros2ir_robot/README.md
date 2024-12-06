# Intelligent Robotics
## ROBOT Simulation and Control
The /ros2ir_robot folder contains 5 different packages:
- ros2ir_gazebo -> The Gazebo/Simulation package contains all the information related to the Gazebo Simulation of the Robot Cell/Environment. CAD and mesh files containing visual data and [.urdf]+[.xacro] files containing Robot (ROS-format) data are combined with ROS 2 control and simulation components, and a simple simulation of the Robot (without any motion control) is obtained in Gazebo.
- ros2ir_moveit2 -> For the Robot to be moved and controlled, a ROS 2 MoveIt!2 package is required. This package contains all the information related to the ROS 2 - MoveGroup (moveit2) node that controls the robot and its behaviour.
- ros2ir_execution -> Additional ROS2 Package containing robot programs.

## INSTRUCTIONS: Execute ROS2 Environments

__Launch Gazebo Simulation Environment__

The following command launches a Gazebo Simulation Environment with the robot in it. It does not have any special functionality, but it could be useful to check that CAD/mesh files and components have been added to the environments successfully:
```sh
ros2 launch ros2srrc_launch simulation.launch.py package:=ros2ir config:=<CONFIG_NAME>
```

__Launch Gazebo + MoveIt!2 Environment__

The following command launches the Gazebo Simulation Environment and the MoveIt!2 Framework for the control of the robot:
```sh
ros2 launch ros2srrc_launch moveit2.launch.py package:=ros2ir config:=<CONFIG_NAME>
```

__Launch RobotBringup + MoveIt!2 Environment__

The following command launches the ROS2 Node that establishes the connection between the Robot's ROS2 Driver and the Robot Controller, and the MoveIt!2 Framework for the control of the robot:
```sh
# For ABB Robot:
ros2 launch ros2srrc_launch bringup_abb.launch.py package:=ros2ir config:=<CONFIG_NAME> robot_ip:=<ROBOT_IP>
# For UR Robot:
ros2 launch ros2srrc_launch bringup_ur.launch.py package:=ros2ir config:=<CONFIG_NAME> robot_ip:=<ROBOT_IP>
```

## INSTRUCTIONS: Robot Operation

You can find all the commands and information [here](https://github.com/IFRA-Cranfield/ros2_SimRealRobotControl/blob/humble/instructions/RobotOperation.md).

## INSTRUCTIONS: Program Execution

You can find all the commands and information [here](https://github.com/IFRA-Cranfield/ros2_SimRealRobotControl/blob/humble/instructions/ProgramExecution.md).

## TASK: cubePP

```sh
# For the ABB IRB-120 Cell (simulation):
ros2 run ros2srrc_execution SpawnObject.py --package "ros2ir_gazebo" --urdf "Cube.urdf" --name "Cube" --x 0.625 --y 0.525 --z 0.88
ros2 run ros2srrc_execution ExecuteProgram.py package:=ros2ir_execution program:=cubePP_irb120

# For the IRB120 Cell (robot):
ros2 run ros2srrc_execution ExecuteProgram.py package:=ros2ir_execution program:=cubePP_irb120_ROB

# For the UR3 Cell (simulation):
ros2 run ros2srrc_execution SpawnObject.py --package "ros2ir_gazebo" --urdf "Cube.urdf" --name "Cube" --x -0.25 --y 0.60 --z 0.80
ros2 run ros2srrc_execution ExecuteProgram.py package:=ros2ir_execution program:=cubePP_ur3

# For the UR3 Cell (robot):
ros2 run ros2srrc_execution ExecuteProgram.py package:=ros2ir_execution program:=cubePP_ur3_ROB
```

## TASK: Cylinder Stacking

```sh
# For the ABB IRB-120 Cell (simulation):
ros2 run ros2srrc_execution SpawnObject.py --package "ros2ir_gazebo" --urdf "BaseCylinder.urdf" --name "BaseCylinder" --x 0.625 --y 0.425 --z 0.88
ros2 run ros2srrc_execution SpawnObject.py --package "ros2ir_gazebo" --urdf "TopCylinder.urdf" --name "TopCylinder" --x 0.625 --y 0.525 --z 0.88
ros2 run ros2srrc_execution ExecuteProgram.py package:=ros2ir_execution program:=cylinderstacking_irb120
```

## TASK: Cube Kitting

```sh
# For the ABB IRB-120 Cell (simulation):
ros2 run ros2srrc_execution SpawnObject.py --package "ros2ir_gazebo" --urdf "WhiteCube.urdf" --name "WhiteCube" --x 0.625 --y 0.525 --z 0.88
ros2 run ros2srrc_execution SpawnObject.py --package "ros2ir_gazebo" --urdf "RedCube.urdf" --name "RedCube" --x 0.625 --y 0.525 --z 0.88
ros2 run ros2srrc_execution SpawnObject.py --package "ros2ir_gazebo" --urdf "BlueCube.urdf" --name "BlueCube" --x 0.625 --y 0.525 --z 0.88
ros2 run ros2srrc_execution SpawnObject.py --package "ros2ir_gazebo" --urdf "GreenCube.urdf" --name "GreenCube" --x 0.625 --y 0.525 --z 0.88
ros2 run ros2srrc_execution ExecuteProgram.py package:=ros2ir_execution program:=cubeKitting_ur3

# For the ABB IRB-120 Cell (robot):
ros2 run ros2srrc_execution ExecuteProgram.py package:=ros2ir_execution program:=cubeKitting_ur3_ROB
```