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

# ros2ir_pubsub/python/Publisher.py:

# ================================================================================= #
# Import libraries:

# Library required to execute ROS2 w/ Python:
import rclpy
from rclpy.node import Node

# Import data class:
from std_msgs.msg import String  # STRING msg type, included in the generic ROS2 data classes.

# ================================================================================= #
# PUBLISHER class:

class Publisher(Node):

    def __init__(self):

        # Declare NODE (+ Node name):
        super().__init__("ros2ir_PUBLISHER") 

        # Declare PUBLISHER:
        self.publisher = self.create_publisher(String, "ros2_TOPIC", 10)

# ================================================================================= #
# ===================================== MAIN ====================================== #
# ================================================================================= #

def main(args=None):

    rclpy.init()

    print (" ========== Intelligent Robotics - Short Course ==========")
    print ("(c) Centre for Robotics and Assembly, Cranfield University")
    print ("")

    # Declare PUBLISHER NODE:
    PublisherNode = Publisher()
    print ("ros2ir_PUBLISHER ROS2 Node generated.")

    # Publish message -> ONCE:

    # 1. Declare variable (+ data type):
    MSG = String()

    # 2. Fill in:
    MSG.data = "HELLO from ROS2!"

    # 3. Publish:
    PublisherNode.publisher.publish(MSG)
    print ('The message: "' +str(MSG.data)+ '" has been published to ros2_TOPIC.')
    print ("")

    print ("Closing program... Bye!")

    PublisherNode.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()