# Intelligent Robotics
## ROS2 Service + Action Package
ROS2 Package containing:
- /Service_Sum ROS2 Service -> A + B = C
    - The SERVICE SERVER (ServiceServer.py) makes the ROS2 Service available (entering a loop/spin), and it executes the operation every single time the Service is called externally.
    - The SERVICE CLIENT (ServiceClient.py) makes a ROS2 Service Request to the ROS2 Service Server.
- /Action_SERIES ROS2 Action -> A + A + A + ... + A*N >= LIMIT
    - The ACTION SERVER (ActionServer.py) makes the ROS2 Action available (entering a loop/spin), and it executes the operation every single time the Action is called externally.
    - The ACTION CLIENT (ActionClient.py) makes a ROS2 Action Call (GOAL REQUEST) to the ROS2 Action Server.

### Execute: ROS2 Service
1. Open a terminal shell, and execute the ROS2 Service Server node:
    ```sh
    ros2 run ros2ir_serviceaction ServiceServer.py
    ```
2. Open a different terminal shell, and execute the ROS2 Service Client node:
    ```sh
    ros2 run ros2ir_serviceaction ServiceClient.py
    ```
3. The ROS2 Service can be manually called (requested) from the Terminal Shell as well:
    ```sh
    ros2 service call /Service_Sum ros2ir_customdata/srv/Sum "{a: 0.0, b: 0.0}"
    ```

### Execute: ROS2 Action
1. Open a terminal shell, and execute the ROS2 Action Server node:
    ```sh
    ros2 run ros2ir_serviceaction ActionServer.py
    ```
2. Open a different terminal shell, and execute the ROS2 Action Client node:
    ```sh
    ros2 run ros2ir_serviceaction ActionClient.py
    ```
3. The ROS2 Action can be manually called (requested) from the Terminal Shell as well:
    ```sh
    ros2 action send_goal /Action_SERIES ros2ir_customdata/action/Series "{number: 0, limit: 0}" --feedback
    ```