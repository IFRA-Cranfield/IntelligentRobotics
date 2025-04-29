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

# ros2ir_serviceaction/python/ServiceClient.py:

# ================================================================================= #
# Import libraries:

# Library required to execute ROS 2 w/ Python:
import rclpy
from rclpy.node import Node

# Import data class:
from ros2ir_customdata.srv import Sum  # Custom data type, created in ros2ir_customdata package.

# ================================================================================= #
# SERVICE CLIENT class:

class ServiceClient(Node):

    def __init__(self):

        super().__init__('ros2ir_ServiceClient')
        self.cli = self.create_client(Sum, "Service_Sum")  

        # Check if the ServiceServer is running:
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("/Service_Sum ROS 2 Service not available, waiting...")
        print("")
        print ("/Service_Sum ROS 2 SERVICE detected!")  

        # Declare REQUEST variable (of CUSTOM DATA type):
        self.req = Sum.Request()                                                   

    def service_REQUEST(self):
        
        # Get a and b values from user input, and call ROS 2 Service:
        print (" +++ /Service_Sum +++ ")
        print ("Please input the values of a and b:")
        self.req.a = float(input("a -> "))
        self.req.b = float(input("b -> "))

        # Assign RESULT value (future):
        self.future = self.cli.call_async(self.req)

# ================================================================================= #
# ===================================== MAIN ====================================== #
# ================================================================================= #

def main(args=None):

    rclpy.init()

    print (" ========== Intelligent Robotics - Short Course ==========")
    print ("(c) Centre for Robotics and Assembly, Cranfield University")
    print ("")

    # Declare ServiceClient NODE:
    ServiceClientNode = ServiceClient()
    print ("ros2ir_ServiceClient ROS 2 Node generated.")
    print ("")

    # EXECUTE ROS 2 Service CALL:
    ServiceClientNode.service_REQUEST()

    # Obtain RESULT:
    while rclpy.ok():

        rclpy.spin_once(ServiceClientNode)

        if ServiceClientNode.future.done():

            try:
                RESULT = ServiceClientNode.future.result()

            except Exception as exc:
                print("/Service_Sum ROS 2 Service call failed. ERROR: " + str(exc))

            else:
                print("RESULT: " + str(ServiceClientNode.req.a) + " + " + str(ServiceClientNode.req.b) + " = " + str(RESULT.result))

            break

    print ("")
    print ("Closing program... Bye!")

    ServiceClientNode.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()