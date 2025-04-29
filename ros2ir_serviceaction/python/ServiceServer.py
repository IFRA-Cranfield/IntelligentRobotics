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

# ros2ir_serviceaction/python/ServiceServer.py:

# ================================================================================= #
# Import libraries:

# Library required to execute ROS 2 w/ Python:
import rclpy
from rclpy.node import Node

# Import data class:
from ros2ir_customdata.srv import Sum  # Custom data type, created in ros2ir_customdata package.

# ================================================================================= #
# SERVICE SERVER class:

class ServiceServer(Node):

    def __init__(self):

        super().__init__('ros2ir_ServiceServer')                                                       
        self.srv = self.create_service(Sum, "Service_Sum", self.service_Callback)       

    def service_Callback(self, request, response):
        
        # Execute operation:
        response.result = request.a + request.b

        # Print some feedback:
        print("SERVICE REQUEST:")
        print("a: " + str(request.a))
        print("b: " + str(request.b))
        print("RESULT = " + str(request.a) + " + " + str(request.b) + " = " + str(response.result))
        print("")

        return(response)

# ================================================================================= #
# ===================================== MAIN ====================================== #
# ================================================================================= #

def main(args=None):

    rclpy.init()

    print (" ========== Intelligent Robotics - Short Course ==========")
    print ("(c) Centre for Robotics and Assembly, Cranfield University")
    print ("")

    # Declare ServiceServer NODE:
    ServiceServerNode = ServiceServer()
    print ("ros2ir_ServiceServer ROS 2 Node generated.")
    print ("")

    # Spin SERVICE -> The Service Server will execute the service_Callback every single time the service is called.
    rclpy.spin(ServiceServerNode)

    print ("Closing program... Bye!")

    ServiceServerNode.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()