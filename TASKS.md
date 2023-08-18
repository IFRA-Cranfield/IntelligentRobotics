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

- Objective: Launch and explore a ROS2-based Robot Control and Simulation environment (Gazebo + MoveIt!2) for the ABB IRB-120. 
- Activity: 
    - Launch irb120_moveit2 environment (Cranfield IA Lab enclosure, w/ EGP-64 gripper). 
    - Move/jog the robot in MoveIt!2, realising collisions, joint limits, configurations… 
    - Explain IFRA_LinkAttacher, IFRA_ObjectPose and IFRA_LinkPose plugins. 
    - Execute custom ROS2 Actions: /Move and /Robmove. 
    - Execute static program for Cube Pick and Place. 

### Task N5: Control of Real Robot using ROS2

- Objective: Launch and explore a ROS2-based Robot Control environment (w/ MoveIt!2) for the ABB IRB-120 in the Cranfield Uni IA Lab. 
- Activity: 
    - Launch irb120_bringup environment (Cranfield IA Lab enclosure, w/ EGP-64 gripper). 
    - Move/jog the robot in MoveIt!2, realising collisions, joint limits, configurations… 
    - Execute custom ROS2 Actions: /Move and /Robmove. 
    - Execute static program for Cube Pick and Place. 

## PART (3)
_Integration of Machine Learning within ROS2: Intelligent Robotics_

### Task N6: Combination of ML (YOLO-Perception) with Robot Control in ROS2 

- Objective: Understand how complex applications can be executed through ROS2 and how information can be exchanged between ML-nodes and the Robot through ROS2 in order to execute complex tasks. 
- Activity: 
    - Task 1: (detect.py)  
    Execute a simple YOLO detection script that detects a cube within the workspace. 
    - Task 2: (coordinates.py)  
    This script detects the cube within the workspace and returns its POSE coordinates. 
    - Task 3: (coordinates_topic.py)  
    The coordinates are shared within the ROS2 network à Published to a ROS2 Topic. 
    - Task 4: (cubePP.py)  
    This script subscribes to the ROS2 Topic where the cube coordinates are published, and it shares that information with the robot in order to pick the cube. 
    - Task 5: (cubePP_loop.py)  
        1. Get the cube coordinates. 
        2. Share coordinates with Robot. 
        3. Pick cube. 
        4. Place cube randomly within the cell. 
        5. Move robot back to HomePos. 
        6. Start again. 