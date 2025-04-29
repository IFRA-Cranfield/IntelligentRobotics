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

# ros2ir_simplepackage/python/HelloWorld.py:

# ================================================================================= #
# Import libraries:

# Library required to execute ROS 2 w/ Python:
import rclpy

# ================================================================================= #
# ===================================== MAIN ====================================== #
# ================================================================================= #

def main(args=None):

    rclpy.init()

    print (" ========== Intelligent Robotics - Short Course ==========")
    print ("(c) Centre for Robotics and Assembly, Cranfield University")
    print ("")

    print ("Hello world!")
    print ("")

    print ("Closing program... Bye!")

    rclpy.shutdown()

if __name__ == '__main__':
    main()