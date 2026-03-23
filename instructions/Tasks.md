# IFRA-Cranfield: Intelligent Robotics
Practical Tasks - ROS 2 Workshop

## PART (1)
_Understanding ROS 2: Environment, Packages, Data Exchange and Task Execution_

### Task N1: Simple ROS 2 Package

- Objective: Understand how ROS 2 Packages are built, and execute a simple ROS 2 node.  
- Activity: 
    1. Realise the architecture of a simple [ROS 2 Package](https://github.com/IFRA-Cranfield/IntelligentRobotics/tree/humble/ros2ir_simplepackage). 
    2. Execute a simple “HelloWorld” Python script through ROS 2. 
    3. Execute a simple “HelloWorld” C++ script through ROS 2. 
    4. Explore how Python and C++ scripts are compiled and executed in ROS 2. 

### Task N2: Publisher/Subscriber

- Objective: Explore a custom ROS 2 Package containing 2 different ROS 2 nodes, one for publishing and another for subscribing to a ROS 2 message.  
- Activity: 
    - Part1: 
        1. Understand the ROS 2 Publisher and Subscriber nodes of a simple [ROS 2 Package](https://github.com/IFRA-Cranfield/IntelligentRobotics/tree/humble/ros2ir_pubsub). 
        2. Execute both nodes in the terminal. 
        3. Publish and subscribe manually from the terminal. 
    - Part2:  
        1. Understand how custom data messages are generated in ROS 2, using a [specific package](https://github.com/IFRA-Cranfield/IntelligentRobotics/tree/humble/ros2ir_customdata). 
        2. Explore the modified Publisher and Subscriber scripts, which allow integrating the custom ROS 2 message. 
        3. Execute both nodes in the terminal. 
        4. Publish and subscribe manually from the terminal. 

### Task N3: Service + Action

- Objective: Understand how ROS 2 Services and Actions work. This is realised through a custom ROS 2 Package containing 4 different ROS 2 nodes: 
    - ROS 2 Service: Server and Client. 
    - ROS 2 Action: Server and Client.  
- Activity: 
    - Part1: 
        1. Explore the ROS 2 Service Server and Client nodes of a simple [ROS 2 Package](https://github.com/IFRA-Cranfield/IntelligentRobotics/tree/humble/ros2ir_serviceaction). The ROS 2 Service consists of a A + B = C sum task. 
        2. Execute both nodes (server and client) in the terminal. 
        3. Call service manually from the terminal. 
    - Part2:  
        1. Explore the ROS 2 Action Server and Client nodes of a simple [ROS 2 Package](https://github.com/IFRA-Cranfield/IntelligentRobotics/tree/humble/ros2ir_serviceaction). The ROS 2 Action consists of a A + A + A … series, up to a B maximum. 
        2. Execute both nodes (service and client) in the terminal. 
        3. Call action manually from the terminal. 

## PART (2)
_Robot Simulation and Control through ROS 2_

ROS 2 Env Launch: [ros2srrc - ROS 2 Environment Launch]()
ROS 2 Packages - Robots: [IFRA-Cranfield/IntelligentRobotics/ros2ir_robot](https://github.com/IFRA-Cranfield/IntelligentRobotics/tree/humble/ros2ir_robot)

### Task N4: Robot Simulation in ROS 2-Gazebo

__ABB IRB-120 Robot__

- Objective: Launch and explore a ROS 2-based Robot Control and Simulation environment (Gazebo + MoveIt!2) for the ABB IRB-120. 
- Activity: 
    - Launch IRB120 MoveIt!2 environment (Cranfield IA Lab enclosure, w/ EGP-64 gripper). 
    - Move/jog the robot in MoveIt!2, realising collisions, joint limits, configurations… 
    - Explain IFRA_LinkAttacher, IFRA_ObjectPose and IFRA_LinkPose plugins. 
    - Execute custom ROS 2 Actions: /Move and /Robmove. 
    - Execute static program for Cube Pick and Place task.

### Task N5: Robot Simulation in ROS 2-Gazebo

__ABB IRB-120 Robot__

- Objective: Launch and explore a ROS 2-based Robot Control and Simulation environment (Gazebo + MoveIt!2) for the ABB IRB-120. 
- Activity: 
    - Launch IRB120 MoveIt!2 environment (Cranfield IA Lab enclosure, w/ EGP-64 gripper). 
    - Move/jog the robot in MoveIt!2, realising collisions, joint limits, configurations… 
    - Explain IFRA_LinkAttacher, IFRA_ObjectPose and IFRA_LinkPose plugins. 
    - Execute custom ROS 2 Actions: /Move and /Robmove. 
    - Execute static program for Cube Pick and Place task.

__UR3 Robot__ 

- Objective: Launch and explore a ROS 2-based Robot Control and Simulation environment (Gazebo + MoveIt!2) for the UR3. 
- Activity: 
    - Launch UR3 MoveIt!2 environment (Cranfield IA Lab stand, w/ Robotiq HandE gripper). 
    - Move/jog the robot in MoveIt!2, realising collisions, joint limits, configurations… 
    - Explain IFRA_LinkAttacher, IFRA_ObjectPose and IFRA_LinkPose plugins. 
    - Execute custom ROS 2 Actions: /Move and /Robmove. 
    - Execute static program for Cube Pick and Place task.

### Task N6: Control of Real Robot using ROS 2

__ABB IRB-120 Robot__

- Objective: Launch and explore a ROS 2-based Robot Control environment (w/ MoveIt!2) for the real ABB IRB-120 robot. 
- Activity: 
    - Launch irb120_bringup environment (Cranfield IA Lab enclosure, w/ EGP-64 gripper). 
    - Move/jog the robot in MoveIt!2, realising collisions, joint limits, configurations… 
    - Execute custom ROS 2 Actions: /Move and /Robmove. 
    - Execute static program for Cube Pick and Place. 

__UR3 Robot__

- Objective: Launch and explore a ROS 2-based Robot Control environment (w/ MoveIt!2) for the real UR3 Robot. 
- Activity: 
    - Launch ur3_bringup environment (Cranfield IA Lab stand, w/ Robotiq HandE gripper). 
    - Move/jog the robot in MoveIt!2, realising collisions, joint limits, configurations… 
    - Execute custom ROS 2 Actions: /Move and /Robmove. 
    - Execute static program for Cube Pick and Place. 

## PART (3)
_Integration of ML & AI within ROS 2: Object Detection, Pose Estimation and Pick & Place task_

### Task N7: Cube Pose Estimation and Pick&Place Task

___Gazebo Simulation Environment___

Objective: Combine our Robot Simulation ROS 2 Packages with YOLO+OpenCV (in Python) and _ROS 2 Communication Mechanisms_ to perform an automated object detection, pose estimation and handling task.

__ABB IRB-120 Robot__

Activity: 
- Launch IRB120 MoveIt!2 environment (Cranfield IA Lab enclosure, w/ EGP-64 gripper). 
- Run the Cube Detection + Pose Estimation ROS 2 Node.
- Run the CubePP script that coordinates the perception with the Robot Operation to undertake the automated handling task.

__UR3 Robot__

Activity: 
- Launch UR3 MoveIt!2 environment (Cranfield IA Lab stand, w/ Robotiq HandE gripper). 
- Run the Cube Detection + Pose Estimation ROS 2 Node.
- Run the CubePP script that coordinates the perception with the Robot Operation to undertake the automated handling task.

___Real Robot___

Objective: Combine our Real Robot Control ROS 2 Packages with YOLO+OpenCV (in Python) and _ROS 2 Communication Mechanisms_ to perform an automated object detection, pose estimation and handling task.

__ABB IRB-120 Robot__

Activity: 
- Launch irb120_bringup environment (Cranfield IA Lab enclosure, w/ EGP-64 gripper). 
- Run the Cube Detection + Pose Estimation ROS 2 Node.
- Run the CubePP script that coordinates the perception with the Robot Operation to undertake the automated handling task.

__UR3 Robot__

Activity: 
- Launch ur3_bringup environment (Cranfield IA Lab stand, w/ Robotiq HandE gripper). 
- Run the Cube Detection + Pose Estimation ROS 2 Node.
- Run the CubePP script that coordinates the perception with the Robot Operation to undertake the automated handling task.