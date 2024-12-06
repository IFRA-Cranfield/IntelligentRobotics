# IFRA-Cranfield: Intelligent Robotics
Practical Tasks - ROS2 Workshop

## PART (1)
_Understanding ROS2: Environment, Packages, Data Exchange and Task Execution_

### Task N1: Simple ROS2 Package

- Objective: Understand how ROS2 Packages are built, and execute a simple ROS2 node.  
- Activity: 
    1. Realise the architecture of a simple [ROS2 Package](https://github.com/IFRA-Cranfield/IntelligentRobotics/tree/main/ros2ir_simplepackage). 
    2. Execute a simple “HelloWorld” Python script through ROS2. 
    3. Execute a simple “HelloWorld” C++ script through ROS2. 
    4. Explore how Python and C++ scripts are compiled and executed in ROS2. 

### Task N2: Publisher/Subscriber

- Objective: Explore a custom ROS2 Package containing 2 different ROS2 nodes, one for publishing and another for subscribing to a ROS2 message.  
- Activity: 
    - Part1: 
        1. Understand the ROS2 Publisher and Subscriber nodes of a simple [ROS2 Package](https://github.com/IFRA-Cranfield/IntelligentRobotics/tree/main/ros2ir_pubsub). 
        2. Execute both nodes in the terminal. 
        3. Publish and subscribe manually from the terminal. 
    - Part2:  
        1. Understand how custom data messages are generated in ROS2, using a [specific package](https://github.com/IFRA-Cranfield/IntelligentRobotics/tree/main/ros2ir_customdata). 
        2. Explore the modified Publisher and Subscriber scripts, which allow integrating the custom ROS2 message. 
        3. Execute both nodes in the terminal. 
        4. Publish and subscribe manually from the terminal. 

### Task N3: Service + Action

- Objective: Understand how ROS2 Services and Actions work. This is realised through a custom ROS2 Package containing 4 different ROS2 nodes: 
    - ROS2 Service: Server and Client. 
    - ROS2 Action: Server and Client.  
- Activity: 
    - Part1: 
        1. Explore the ROS2 Service Server and Client nodes of a simple [ROS2 Package](https://github.com/IFRA-Cranfield/IntelligentRobotics/tree/main/ros2ir_serviceaction). The ROS2 Service consists of a A + B = C sum task. 
        2. Execute both nodes (server and client) in the terminal. 
        3. Call service manually from the terminal. 
    - Part2:  
        1. Explore the ROS2 Action Server and Client nodes of a simple [ROS2 Package](https://github.com/IFRA-Cranfield/IntelligentRobotics/tree/main/ros2ir_serviceaction). The ROS2 Action consists of a A + A + A … series, up to a B maximum. 
        2. Execute both nodes (service and client) in the terminal. 
        3. Call action manually from the terminal. 

## PART (2)
_Robot Simulation and Control through ROS2_

### Task N4: Robot Simulation in ROS2-Gazebo

ROS 2 Packages: [IFRA-Cranfield/IntelligentRobotics/ros2ir_robot](https://github.com/IFRA-Cranfield/IntelligentRobotics/tree/main/ros2ir_robot)

__ABB IRB-120 Robot__

- Objective: Launch and explore a ROS2-based Robot Control and Simulation environment (Gazebo + MoveIt!2) for the ABB IRB-120. 
- Activity: 
    - Launch irb120_moveit2 environment (Cranfield IA Lab enclosure, w/ EGP-64 gripper). 
    - Move/jog the robot in MoveIt!2, realising collisions, joint limits, configurations… 
    - Explain IFRA_LinkAttacher, IFRA_ObjectPose and IFRA_LinkPose plugins. 
    - Execute custom ROS2 Actions: /Move and /Robmove. 
    - Execute static program for Cube Pick and Place.
    - Execute static program for Cylinder Stacking use-case.

__UR3 Robot__ 

- Objective: Launch and explore a ROS2-based Robot Control and Simulation environment (Gazebo + MoveIt!2) for the UR3. 
- Activity: 
    - Launch ur3_moveit2 environment (Cranfield IA Lab cell, w/ Robotiq HandE gripper). 
    - Move/jog the robot in MoveIt!2, realising collisions, joint limits, configurations… 
    - Explain IFRA_LinkAttacher, IFRA_ObjectPose and IFRA_LinkPose plugins. 
    - Execute custom ROS2 Actions: /Move and /Robmove. 
    - Execute static program for Cube Pick and Place.
    - Execute static program for Cube Kitting use-case.

### Task N5: Control of Real Robot using ROS2

__ABB IRB-120 Robot__

- Objective: Launch and explore a ROS2-based Robot Control environment (w/ MoveIt!2) for the real ABB IRB-120 robot. 
- Activity: 
    - Launch irb120_bringup environment (Cranfield IA Lab enclosure, w/ EGP-64 gripper). 
    - Move/jog the robot in MoveIt!2, realising collisions, joint limits, configurations… 
    - Execute custom ROS2 Actions: /Move and /Robmove. 
    - Execute static program for Cube Pick and Place. 
    - Execute static program for Cylinder Stacking use-case.

__UR3 Robot__

- Objective: Launch and explore a ROS2-based Robot Control environment (w/ MoveIt!2) for the real UR3 Robot. 
- Activity: 
    - Launch ur3_bringup environment (Cranfield IA Lab cupboard, w/ Robotiq HandE gripper). 
    - Move/jog the robot in MoveIt!2, realising collisions, joint limits, configurations… 
    - Execute custom ROS2 Actions: /Move and /Robmove. 
    - Execute static program for Cube Pick and Place. 
    - Execute static program for Cube Kitting use-case.