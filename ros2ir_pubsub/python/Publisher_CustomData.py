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

# ros2ir_pubsub/python/Publisher_CustomData.py:

# ================================================================================= #
# Import libraries:

# Library required to execute ROS 2 w/ Python:
import rclpy
from rclpy.node import Node

# Import data class:
from ros2ir_customdata.msg import Custom  # Custom data type, created in ros2ir_customdata package.

# ================================================================================= #
# PUBLISHER class:

class Publisher(Node):

    def __init__(self):

        # Declare NODE (+ Node name):
        super().__init__("ros2ir_PUBLISHER_CustomData") 

        # Declare PUBLISHER:
        self.publisher = self.create_publisher(Custom, "ros2_TOPIC_CustomData", 10)

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
    print ("ros2ir_PUBLISHER ROS 2 Node generated.")

    # Publish message -> ONCE:

    # 1. Declare variable (+ data type):
    MSG = Custom()

    # 2. Fill in:
    MSG.name = "Mikel Bueno"
    MSG.age = 25

    # 3. Publish:
    PublisherNode.publisher.publish(MSG)
    print ('The CustomMessage has been published to ros2_TOPIC_CustomData:') 
    print ('Name -> ' + str(MSG.name))
    print ('Age -> ' + str(MSG.age))
    print ("")

    print ("Closing program... Bye!")

    PublisherNode.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()