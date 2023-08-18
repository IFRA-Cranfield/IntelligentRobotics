# Intelligent Robotics
## ROBOT Simulation and Control
The /ros2ir_robot folder contains 5 different packages:
- ros2ir_gazebo -> The Gazebo/Simulation package contains all the information related to the Gazebo Simulation of the Robot Cell/Environment. CAD and mesh files containing visual data and [.urdf]+[.xacro] files containing Robot (ROS-format) data are combined with ROS 2 control and simulation components, and a simple simulation of the Robot (without any motion control) is obtained in Gazebo.
- ros2ir_moveit2 -> For the Robot to be moved and controlled, a ROS 2 MoveIt!2 package is required. This package contains all the information related to the ROS 2 - MoveGroup (moveit2) node that controls the robot and its behaviour.
- ros2ir_bringup -> The Bringup package acts as the main connection point between ROS 2 and the Real Robot. It contains all the information about the robot controllers, and establishes the connection between moveit2 and the Real Robot. For the connection between ROS 2 and a Real Robot to be established, a ROS 2 Driver is required, which translates the ROS 2-based commands to the Robot Controller. This ROS 2 Driver is usually developed by the Robot vendor or a recognised ROS2-development company.
- ros2ir_execution -> Additional ROS2 Package containing source code for specific tasks such as program execution (and storage), spawning objects to the simulation environment and obtaining the robot's joint-space state.
- ros2ir_detection -> TBD.

## INSTRUCTIONS: Execute ROS2 Environments

__Launch Gazebo Simulation Environment__

The following command launches a Gazebo Simulation Environment with the ABB IRB-120 in it. It does not have any special functionality, but it could be useful to check that CAD/mesh files and components have been added to the environments successfully:
```sh
ros2 launch ros2ir_gazebo simulation.launch.py
```

__Launch Gazebo + MoveIt!2 Environment__

The following command launches the Gazebo Simulation Environment and the MoveIt!2 Framework for the control of the ABB IRB-120 robot:
```sh
ros2 launch ros2ir_moveit2 moveit2.launch.py
```

__Launch RobotBringup + MoveIt!2 Environment__

The following command launches the ROS2 Node that establishes the connection between the Robot's ROS2 Driver and the Robot Controller, and the MoveIt!2 Framework for the control of the robot:
```sh
ros2 launch ros2ir_bringup bringup.launch.py
```

## INSTRUCTIONS: Execute ROBOT MOVEMENTS

Robot movements can be executed in 2 different ways, which are defined in the ros2_SimRealRobotControl/ros2srrc_execution ROS2 Package:
- Using the /Move custom ROS2 action.
- Using the /Robmove custom ROS2 action.

### /Move ACTION

For /Move, the Robot Motion request consists of a simple ROS2 Action (/Move) call, where the following parameters must be specified:
- The ACTION that is going to be executed.
- The speed at which the robot will execute the action.
- The value of the action to be executed.

There are currently 9 different ACTION TYPES, which can be executed by running the following commands in the Ubuntu Terminal:

* MoveJ: The Robot moves to the specific waypoint, which is specified by Joint Pose values.
  ```sh
  ros2 action send_goal -f /Move ros2srrc_data/action/Move "{action: 'MoveJ', movej: {joint1: 0.00, joint2: 0.00, joint3: 0.00, joint4: 0.00, joint5: 0.00, joint6: 0.00}, speed: 1.0}"
  ```
* MoveG: The Gripper fingers move to the specific pose.
  ```sh
  ros2 action send_goal -f /Move ros2srrc_data/action/Move "{action: 'MoveG', moveg: 0.0, speed: 1.0}"
  ```
* MoveL: The Robot executes a CARTESIAN/LINEAR path. The End-Effector orientation is kept constant, and the position changes by +-(x,y,z).
  ```sh
  ros2 action send_goal -f /Move ros2srrc_data/action/Move "{action: 'MoveL', movel: {x: 0.00, y: 0.00, z: 0.00}, speed: 1.0}"
  ```
* MoveR: The Robot rotates the selected joint a specific amount of degrees.
  ```sh
  ros2 action send_goal -f /Move ros2srrc_data/action/Move "{action: 'MoveR', mover: {joint: '--', value: 0.00}, speed: 1.0}"
  ```
* MoveXYZW: The Robot moves to the specific waypoint, which is represented by the Position(x,y,z) + EulerAngles(yaw,pitch,roll) End-Effector coordinates.
  ```sh
  ros2 action send_goal -f /Move ros2srrc_data/action/Move "{action: 'MoveXYZW', movexyzw: {x: 0.00, y: 0.00, z: 0.00, yaw: 0.00, pitch: 0.00, roll: 0.00}, speed: 1.0}"
  ```
* MoveXYZ: The Robot moves to the specific waypoint -> Position(x,y,z) maintaining the End-Effector orientation.
  ```sh
  ros2 action send_goal -f /Move ros2srrc_data/action/Move "{action: 'MoveXYZ', movexyz: {x: 0.00, y: 0.00, z: 0.00}, speed: 1.0}"
  ```
* MoveYPR: The Robot rotates/orientates the End-Effector frame according to the input: EulerAngles(yaw,pitch,roll). The YPR(yaw,pitch,roll)determines the FINAL ROTATION of the End-Effector, which is related to the GLOBAL COORDINATE FRAME.
  ```sh
  ros2 action send_goal -f /Move ros2srrc_data/action/Move "{action: 'MoveYPR', moveypr: {yaw: 0.00, pitch: 0.00, roll: 0.00}, speed: 1.0}"
  ```
* MoveROT: The Robot rotates/orientates the End-Effector frame according to the input: EulerAngles(yaw,pitch,roll). THE ROT(yaw,pitch,roll) determines the ADDED ROTATION of the End-Effector, which is applied to the END-EFFECTOR COORDINATE FRAME.
  ```sh
  ros2 action send_goal -f /Move ros2srrc_data/action/Move "{action: 'MoveROT', moverot: {yaw: 0.00, pitch: 0.00, roll: 0.00}, speed: 1.0}"
  ```
* MoveRP: End-Effector rotation AROUND A POINT -> The Robot rotates/orientates + moves the End-Effector frame according to the input: EulerAngles(yaw,pitch,roll) + Point(x,y,z). THE ROT(yaw,pitch,roll) determines the ADDED ROTATION of the End-Effector, which is applied to the END-EFFECTOR COORDINATE FRAME, AROUND THE (x,y,z) POINT.
  ```sh
  ros2 action send_goal -f /Move ros2srrc_data/action/Move "{action: 'MoveRP', moverp: {x: 0.00, y: 0.00, z: 0.00, yaw: 0.00, pitch: 0.00, roll: 0.00}, speed: 1.0}"
  ```
* NOTE: The Robot JOINT SPEED is controlled by the "speed" parameter when executing the specific ROS2.0 action. The value must be (0,1]. being 1 the maximum velocity and 0 the null velocity (which is not valid -> A small value must be defined, e.g.: 0.01 represents a very slow movement).

### /Robmove ACTION

/Robmove allows the user to move the robot to a specific End-Effector pose (tool0 frame). It is executed after defining the parameters listed below:
- The TYPE of movement: It can be LINEAR ("LIN"), or Point-to-Point ("PTP").
- The speed at which the robot will execute the action.
- The POSE, (POSITION - x,y,z + ROTATION - qx,qy,qz,qw).

/Robmove can be executed by running the following command in the Ubuntu Terminal:
```sh
ros2 action send_goal -f /Robmove ros2srrc_data/action/Robmove "{type: '---', speed: 1.0, x: 0.0, y: 0.0, z: 0.0, qx: 0.0, qy: 0.0, qz: 0.0, qw: 0.0}"
```
It is recommended to combine /Robmove with /Robpose (ROS2 Topic, see below). This ROS2 topic publishes the current (real-time) pose of the Robot's end-effector, which helps the user to define the robot's next pose.

## INSTRUCTIONS: Execution of a PROGRAM/SEQUENCE

Programs can be executed by running the following command in the Ubuntu Terminal:
```sh
ros2 run ros2ir_execution sequence.py --ros-args -p PROGRAM_FILENAME:="---" -p ROBOT_MODEL:="irb120" -p EE_MODEL:="egp64" -p GzBr_ENV:="---"
```
* The PROGRAM_FILENAME parameter is the name of the file which contains the program. The program is saved in a .txt file, and the name must be inputted excluding the ".txt" extension.
* The ROBOT_MODEL parameter represents the model of the robot. 
* The EE_MODEL parameter represents the model of the end-effector.
* The GzBr_ENV parameter defines whether the execution is being done in Gazebo or real robot. Options: gazebo - bringup.

__Pre-defined sequence: Format__

The pre-defined programs are saved inside the /programs folder as .txt files. Every single line of the .txt file represents an execution step (being the 1st line: 1st step, 2nd line: 2nd step, ...), and it is represented as a python dictionary. The following list showcases how every single Robot Movement has to be inputted in the program.txt:
* For MoveJ ---> {'action': 'MoveJ', 'value': {'joint1': 0.0, 'joint2': 0.0, 'joint3': 0.0, 'joint4': 0.0, 'joint5': 0.0, 'joint6': 0.0}, 'speed': 1.0}
* For MoveL ---> {'action': 'MoveL', 'value': {'x': 0.0, 'y': 0.0, 'z': 0.0}, 'speed': 1.0}
* For MoveR ---> {'action': 'MoveR', 'value': {'joint': '---', 'value': 0.0}, 'speed': 1.0}
* For MoveXYZW ---> {'action': 'MoveXYZW', 'value': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'yaw': 0.0, 'pitch': 0.0, 'roll': 0.0}, 'speed': 1.0}
* For MoveXYZ ---> {'action': 'MoveXYZ', 'value': {'x': 0.0, 'y': 0.0, 'z': 0.0}, 'speed': 1.0}
* For MoveYPR ---> {'action': 'MoveYPR', 'value': {'yaw': 0.0, 'pitch': 0.0, 'roll': 0.0}, 'speed': 1.0}
* For MoveROT ---> {'action': 'MoveROT', 'value': {'yaw': 0.0, 'pitch': 0.0, 'roll': 0.0}, 'speed': 1.0}
* For MoveRP ---> {'action': 'MoveRP', 'value': {'yaw': 0.0, 'pitch': 0.0, 'roll': 0.0, 'x': 0.0, 'y': 0.0, 'z': 0.0}, 'speed': 1.0}
* For MoveG (Gazebo) ---> {'action': 'MoveG', 'value': {'value': 0.0}, 'speed': 1.0}
* For MoveG (ABB Robot): 
    * To Open Gripper ---> {'action': 'GripperOpen'}
    * To Close Gripper ---> {'action': 'GripperClose'}
* For the object manipulation (IFRA_LinkAttacher Gazebo Plugin):
    * To attach object to end-effector ---> {'action': 'Attach', 'value': {'model1': '---', 'link1': '---', 'model2': '---', 'link2': '---'}}
    * To detach object from end-effector ---> {'action': 'Attach', 'value': {'model1': '---', 'link1': '---', 'model2': '---', 'link2': '---'}}
    * Elements are defined as follows:
      * model1 -> Name of the model/robot (defined in the robot .urdf). 
      * link1 -> Name of the end-effector link that the object will be attached to.
      * model2 -> Name of the object to be attached (defined in the object .urdf). 
      * link2 -> Name of the object link.

## Obtaining ROBOT INFORMATION

The __RobotState.py__ script allows the user to get the state of the robot in __joint values__, by simply executing the following command:
```sh
ros2 run ros2ir_execution RobotState.py
# The script returns the robot's JointState values in the standard format presented above, in the sequence definition:
# {'joint1': 0.0, 'joint2': 0.0, 'joint3': 0.0, 'joint4': 0.0, 'joint5': 0.0, 'joint6': 0.0}
```

The __robpose.cpp__ script allows the user to get the pose of the robot's end-effector (tool0 flange) in __(POS + ROT)__, by simply subscribing to the /Robpose ROS2 topic:
```sh
ros2 topic echo /Robpose
```

## Spawn any object (CAD file) into the Simulation Environment

The __SpawnObject.py__ script allows the user to spawn any object (defined in a .__urdf__ file) to a Gazebo simulation, by simply executing the following command:
```sh
ros2 run ros2ir_execution SpawnObject.py --package "{}" --urdf "{}.urdf" --name "{}" --x {} --y {} --z {}
# NOTE: It is assumed that the .urdf file of the object to be spawned is stored in the /urdf folder of the selected package.
```

## Execute -> cubePP program

```sh
# Spawn 4 different boxes into the cell:
ros2 run ros2ir_execution SpawnObject.py --package "ros2ir_gazebo" --urdf "box.urdf" --name "box1" --x 0.575 --y 0.525 --z 0.88
ros2 run ros2ir_execution SpawnObject.py --package "ros2ir_gazebo" --urdf "box.urdf" --name "box2" --x 0.575 --y 0.625 --z 0.88
ros2 run ros2ir_execution SpawnObject.py --package "ros2ir_gazebo" --urdf "box.urdf" --name "box3" --x 0.575 --y 0.725 --z 0.88
ros2 run ros2ir_execution SpawnObject.py --package "ros2ir_gazebo" --urdf "box.urdf" --name "box4" --x 0.575 --y 0.825 --z 0.88

# Execute sequence:
ros2 run ros2ir_execution sequence.py --ros-args -p PROGRAM_FILENAME:="irb120cubePP" -p ROBOT_MODEL:="irb120" -p EE_MODEL:="egp64" -p GzBr_ENV:="gazebo"

# For the REAL ROBOT:
ros2 run ros2ir_execution sequence.py --ros-args -p PROGRAM_FILENAME:="irb120cubePP_ROB" -p ROBOT_MODEL:="irb120" -p EE_MODEL:="egp64" -p GzBr_ENV:="gazebo"
```