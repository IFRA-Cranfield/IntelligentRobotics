# Intelligent Robotics
## ROS2 Publisher + Subscriber Package
ROS2 Package containing:
- Publisher.py -> ROS2 node that publishes a simple message (String) to /ros2_TOPIC.
- Subscriber.py -> ROS2 node that subscribes to /ros2_TOPIC, and prints the received message.
- Publisher_CustomData.py -> ROS2 node that publishes a custom message (Name+Age) to /ros2_TOPIC_CustomData.
- Subscriber_CustomData.py -> ROS2 node that subscribes to /ros2_TOPIC_CustomData, and prints the received message.

### Execute: Publisher + Subscriber
1. Open a terminal shell, and execute the ROS2 Subscriber node:
    ```sh
    ros2 run ros2ir_pubsub Susbcriber.py
    ```
2. Open a different terminal shell, and execute the ROS2 Publisher node:
    ```sh
    ros2 run ros2ir_pubsub Publisher.py
    ```

### Execute: Publisher + Subscriber (CustomData)
1. Open a terminal shell, and execute the ROS2 Subscriber node:
    ```sh
    ros2 run ros2ir_pubsub Susbcriber_CustomData.py
    ```
2. Open a different terminal shell, and execute the ROS2 Publisher node:
    ```sh
    ros2 run ros2ir_pubsub Publisher_CustomData.py
    ```

### Publish to a ROS2 Topic manually from the Terminal Shell
ROS2 Messages can be manually published from the Terminal Shell by running the following command:
```sh
# Publish to /ros2_TOPIC:
ros2 topic pub --rate 1 /ros2_TOPIC std_msgs/msg/String "{data: 'HELLO from ROS2! '}"
ros2 topic pub --once /ros2_TOPIC std_msgs/msg/String "{data: 'HELLO from ROS2! '}"

# Publish to /ros2_TOPIC_CustomData:
ros2 topic pub --rate 1 /ros2_TOPIC_CustomData ros2ir_customdata/msg/Custom "{name: 'Mikel Bueno', age: 25}"
ros2 topic pub --once /ros2_TOPIC_CustomData ros2ir_customdata/msg/Custom "{name: 'Mikel Bueno', age: 25}"
```
You can easily subscribe to a ROS2 Topic by executing the following command:
```sh
# Subscribe to /ros2_TOPIC:
ros2 topic echo /ros2_TOPIC

# Subscribe to /ros2_TOPIC_CustomData:
ros2 topic echo /ros2_TOPIC_CustomData
```