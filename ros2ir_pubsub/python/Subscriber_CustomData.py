#!/usr/bin/python3

# ================================================================================= #
#                                                                                   #
#                             Intelligent Robotics                                  #
#                             --------------------                                  #
#                                                                                   #
#  (c) Centre for Robotics and Assembly, Cranfield University                       #
#                                                                                   #
#  IFRA (Intelligent Flexible Robotics and Assembly) Group, CRANFIELD UNIVERSITY    #
#  Created on behalf of the IFRA Group at Cranfield University, United Kingdom      #
#  E-mail: IFRA@cranfield.ac.uk                                                     #                                                                                       #
#                                                                                   #
#  IFRA Group - Cranfield University                                                #
#  AUTHORS: Mikel Bueno Viso - Mikel.Bueno-Viso@cranfield.ac.uk                     #
#           Dr. Seemal Asif  - s.asif@cranfield.ac.uk                               #
#                                                                                   #
#  Date: September, 2023.                                                           #
#                                                                                   #
# ================================================================================= #

# ros2ir_pubsub/python/Subscriber.py:

# ================================================================================= #
# Import libraries:

# Library required to execute ROS2 w/ Python:
import rclpy
from rclpy.node import Node

# Import data class:
from ros2ir_customdata.msg import Custom  # Custom data type, created in ros2ir_customdata package.

# ================================================================================= #
# SUBSCRIBER class:

class Subscriber(Node):

    def __init__(self):

        # Declare NODE (+ Node name):
        super().__init__("ros2ir_SUBSCRIBER_CustomData") 

        # Declare SUBSCRIBER:
        self.subscription = self.create_subscription(
            Custom,                                                                                                               
            "ros2_TOPIC_CustomData",                                                                   
            self.listener_callback,                                                    
            10)                                                                
        self.subscription # Prevent unused variable warning.

    def listener_callback(self, MSG):
        print (" (*) Message received to ros2_TOPIC: ")  
        print ("        - Name: " + str(MSG.name))
        print ("        - Age: " + str(MSG.age))
        print ("")

# ================================================================================= #
# ===================================== MAIN ====================================== #
# ================================================================================= #

def main(args=None):

    rclpy.init()

    print (" ========== Intelligent Robotics - Short Course ==========")
    print ("(c) Centre for Robotics and Assembly, Cranfield University")
    print ("")

    # Declare SUBSCRIBER NODE:
    SubscriberNode = Subscriber()
    print ("ros2ir_SUBSCRIBER ROS2 Node generated.")

    # Spin SUBSCRIBER, create CALLBACK:
    print ("Subscribing to /ros2_TOPIC_CustomData, waiting for a message to be published...")
    print ("")
    rclpy.spin(SubscriberNode)

    SubscriberNode.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()