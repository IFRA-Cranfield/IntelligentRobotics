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

# ros2ir_serviceaction/python/ActionServer.py:

# ================================================================================= #
# Import libraries:

# Library required to execute ROS 2 w/ Python:
import rclpy
from rclpy.node import Node

# Required for ROS 2 ACTIONS:
from rclpy.action import ActionServer, CancelResponse, GoalResponse
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor

# Extra (required for the series operation):
import time

# Import data class:
from ros2ir_customdata.action import Series  # Custom data type, created in ros2ir_customdata package.

# ================================================================================= #
# Action SERVER class:

class ActionServer_(Node):

    # This function initialises the ActionServer, and it is executed when the class is instantiated in the main thread:
    def __init__(self):

        super().__init__('ros2ir_ActionServer')                                                       
        self._action_server = ActionServer(
            self,
            Series,
            'Action_SERIES',
            execute_callback = self.execute_callback,
            callback_group = ReentrantCallbackGroup(),
            goal_callback = self.goal_callback,
            cancel_callback = self.cancel_callback
        ) 

    def destroy(self):
        self._action_server.destroy()
        super().destroy_node()    

    # This function is executed when the ACTION is called, and it is used to ACCEPT/REJECT the action call:
    def goal_callback(self, goal_request):
        
        # GOAL REQUEST:
        number = goal_request.number
        limit = goal_request.limit
        
        print ("/Action_SERIES -> GOAL REQUEST:")
        print ("number: " + str(number))
        print ("limit: " + str(limit))
        print ("")

        if (number <= 0 or limit <= 0):
            print ("ERROR: <number> and <limit> must be positive (>0). GOAL -> REJECTED.")
            print ("")
            return GoalResponse.REJECT
        elif (number >= limit):
            print ("ERROR: <Limit> must be bigger than <number>. GOAL -> REJECTED.")
            print ("")
            return GoalResponse.REJECT
        else:
            print("/Action_SERIES: GOAL -> ACCEPTED.")
            print ("")
            return GoalResponse.ACCEPT

    # CANCEL ACTION CALL if a "CANCEL" (e.g.: CTRL+C) is requested:
    def cancel_callback(self, goal_handle):
        print ("CANCEL REQUEST: Cancelling /Action_SERIES ROS 2 Action request.")
        print ("")
        return CancelResponse.ACCEPT 

    # CALLBACK FUNCTION -> SERIES operation:
    async def execute_callback(self, goal_handle):

        print ("/Action_SERIES: Executing sequence...")

        # Assign -> GOAL variable:
        number = goal_handle.request.number
        limit = goal_handle.request.limit
        
        # Declare -> FEEDBACK MESSAGE:
        FEEDBACK_MSG = Series.Feedback()
        FEEDBACK_MSG.feedback = ""

        # LOOP:
        END = False
        i = 1
        while (END == False):

            # In the loop, check if a CANCEL REQUEST has been done:
            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                return(Series.Result())
        
            # OPERATION:
            RES = i*number 

            if (RES <= limit):
                FEEDBACK_MSG.feedback = "Iteration N" + str(i) + ": (number= " + str(number) +")*" + str(i) + " = " + str(RES) + " <= (limit=" + str(limit) +")"
                i = i + 1 
            else:
                FEEDBACK_MSG.feedback = "(LIMIT REACHED) -> Iteration N" + str(i) + ": (number= " + str(number) +")*" + str(i) + " = " + str(RES) + " > (limit=" + str(limit) +")" 
                END = True

            print(FEEDBACK_MSG.feedback)
            goal_handle.publish_feedback(FEEDBACK_MSG)
            time.sleep(1)

        goal_handle.succeed() # ACTION finished successfully.
        
        # Assign -> RESULT variable:
        RESULT = Series.Result()

        RESULT.result = "Limit reached -> ITERATION: " + str(i) + ", " + str(number) + "*" + str(i) + " = " + str(RES) + " > limit=" + str(limit)
        RESULT.iteration = i

        print("")

        return(RESULT)

# ================================================================================= #
# ===================================== MAIN ====================================== #
# ================================================================================= #

def main(args=None):

    rclpy.init(args=args)

    print (" ========== Intelligent Robotics - Short Course ==========")
    print ("(c) Centre for Robotics and Assembly, Cranfield University")
    print ("")

    # Declare ActionServer NODE:
    ActionServerNode = ActionServer_()
    print ("ros2ir_ActionServer ROS 2 Node generated.")
    print ("")

    # Use a MultiThreadedExecutor to enable processing goals concurrently:
    executor = MultiThreadedExecutor()

    # Spin ACTION -> The Action Server will execute the ActionCallback (execute_callback) every single time the action is called.
    rclpy.spin(ActionServerNode, executor)

    print ("Closing program... Bye!")

    ActionServerNode.destroy()
    rclpy.shutdown()

if __name__ == '__main__':
    main()