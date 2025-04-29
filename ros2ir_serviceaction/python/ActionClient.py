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

# ros2ir_serviceaction/python/ActionClient.py:

# ================================================================================= #
# Import libraries:

# Library required to execute ROS 2 w/ Python:
import rclpy
from rclpy.node import Node

# Library -> ActionClient:
from rclpy.action import ActionClient
from action_msgs.msg import GoalStatus

# Import data class:
from ros2ir_customdata.action import Series  # Custom data type, created in ros2ir_customdata package.

# ================================================================================= #
# ACTION CLIENT class:

class ActionClient_(Node):

    # Initialise ACTION CLIENT:
    def __init__(self):

        super().__init__('ros2ir_ActionClient')
        self._action_client = ActionClient(self, Series, "Action_SERIES")  

        print ("Waiting for ActionServer to be active...")
        self._action_client.wait_for_server()
        print ("/Service_Sum ROS 2 SERVICE detected!")  

        self.goal_handle = None

    # SEND GOAL:
    def send_goal(self, number, limit):

        print("Sending GOAL -> Number: " + str(number) + ", Limit: " + str(limit))
        
        goal_msg = Series.Goal()
        goal_msg.number = number
        goal_msg.limit = limit

        self._send_goal_future = self._action_client.send_goal_async(goal_msg,feedback_callback=self.feedback_callback)
        print("GOAL SENT!")
        print("")
        self._send_goal_future.add_done_callback(self.goal_response_callback)   

    # CHECK IF GOAL HAS BEEN ACCEPTED/REJECTED:
    def goal_response_callback(self, future):
        
        self.goal_handle = future.result()
        
        if not self.goal_handle.accepted:
            print("ERROR: GOAL has been rejected.")
            rclpy.shutdown()
            return

        print("/Action_SERIES -> GOAL has been accepted.")
        print("")

        self._get_result_future = self.goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)                                              

    # FEEDBACK:
    def feedback_callback(self, feedback):
        print("FEEDBACK MSG: " + str(feedback.feedback))

    # GET RESULT:
    def get_result_callback(self, future):
        
        result = future.result().result         # RESULT of the ACTION CALL.
        status = future.result().status         # STATUS of the ACTION CALL -> SUCCEEDED/FAILED.
        
        print("")

        if status == GoalStatus.STATUS_SUCCEEDED:
            print("ACTION CALL SUCCESSFUL! Result:")
            print("Message -> " + str(result.result))
            print("Iteration -> " + str(result.iteration))
            
        else:
            print("ACTION CALL FAILED!")
            print("Reason -> " + str(status))

        # SHUTDOWN after receiving the result:
        rclpy.shutdown()

    # CANCEL ACTION CALL:
    def CANCEL(self):
        self.goal_handle.cancel_goal_async()

# ================================================================================= #
# ===================================== MAIN ====================================== #
# ================================================================================= #

def main(args=None):

    rclpy.init()

    print (" ========== Intelligent Robotics - Short Course ==========")
    print ("(c) Centre for Robotics and Assembly, Cranfield University")
    print ("")

    # Declare ActionClient NODE:
    ActionClientNode = ActionClient_()
    print ("ros2ir_ActionClient ROS 2 Node generated.")
    print ("")

    # Get INPUT VALUES (number/limit) for ACTION CALL:
    print (" +++ /Action_SERIES +++ ")
    print ("Please input the values of <number> and <limit>:")
    number = int(input("number -> "))
    limit = int(input("limit -> "))
    print("")

    # ACTION CALL (send_goal):

    try:
        ActionClientNode.send_goal(number,limit)
        rclpy.spin(ActionClientNode)

    except KeyboardInterrupt:
        print("")
        print("CTRL+C detected. Cancelling ACTION CALL...")
        ActionClientNode.CANCEL()

    print ("")
    print ("Closing program... Bye!")

if __name__ == '__main__':
    main()