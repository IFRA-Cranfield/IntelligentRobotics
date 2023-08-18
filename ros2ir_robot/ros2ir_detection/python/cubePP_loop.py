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

# ros2ir_robot/ros2ir_detection/python/cubePP_loop.py:

# ================================================================================= #

# Required to include ROS2 and its components:
import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor

# Import additional elements:
import math
import time

# Import ROS2 MSG, SRV and ACTION (s):
from std_msgs.msg import String
from geometry_msgs.msg import Pose
from ros2srrc_data.action import Robmove
from ros2srrc_data.action import Move
from ros2srrc_data.msg import Action
from abb_robot_msgs.srv import SetIOSignal
from ros2ir_customdata.msg import Coordinates

# Data classes:
from dataclasses import dataclass

# Define GLOBAL VARIABLE -> COORDINATES:
COORDINATES = Coordinates()

# Define GLOBAL VARIABLE -> RES:
@dataclass
class feedback:
    MESSAGE: String
    SUCCESS: bool
RES = feedback("null", False)
RES_ABB = "null"

# =============================================================================== #
# Convert ANGLE to -> QUATERNION:

def toQuaternion(angle):

    # Declaration of GLOBAL VARIABLES --> CONSTANT VALUES for angle transformation (DEG->RAD):
    pi = 3.14159265358979
    k = pi/180.0

    # 1. Initial pose:
    Ax = 0.0
    Ay = 1.0
    Az = 0.0
    Aw = 0.0
    # 2. Get desired RELATIVE ROTATION:
    yaw = angle
    pitch = 0.0
    roll = 0.0
    cy = math.cos(k*yaw * 0.5)
    sy = math.sin(k*yaw * 0.5)
    cp = math.cos(k*pitch * 0.5)
    sp = math.sin(k*pitch * 0.5)
    cr = math.cos(k*roll * 0.5)
    sr = math.sin(k*roll * 0.5)
    Bx = sr * cp * cy - cr * sp * sy
    By = cr * sp * cy + sr * cp * sy
    Bz = cr * cp * sy - sr * sp * cy
    Bw = cr * cp * cy + sr * sp * sy
    # 3. Quaternion MULTIPLICATION:
    ROTATION = dict()
    ROTATION["ROTx"] = Aw*Bx + Ax*Bw + Ay*Bz - Az*By
    ROTATION["ROTy"] = Aw*By - Ax*Bz + Ay*Bw + Az*Bx
    ROTATION["ROTz"] = Aw*Bz + Ax*By - Ay*Bx + Az*Bw
    ROTATION["ROTw"] = Aw*Bw - Ax*Bx - Ay*By - Az*Bz

    return(ROTATION)

# =============================================================================== #
# ROS2 Subscriber to get COORDINATES:

class CoordinateSubscriber(Node):

    def __init__(self):

        super().__init__("ros2ir_CoordinateSubscriber")
        self.subscription_ = self.create_subscription(Coordinates, "ros2ir_BoxCoordinates", self.listener_callback, 10)

    def listener_callback(self, MSG):

        global COORDINATES

        COORDINATES.x = MSG.x
        COORDINATES.y = MSG.y
        COORDINATES.angle = MSG.angle

# =============================================================================== #
# ROS2 ActionClient for RobMove:

class RobMoveClient(Node):

    def __init__(self):

        super().__init__('ros2ir_RobMove_Client')
        self._action_client = ActionClient(self, Robmove, 'Robmove')

        #print ("Waiting for /Robmove ROS2 ActionServer to be available...")
        self._action_client.wait_for_server()
        #print ("/Robmove ACTION SERVER detected.")

    def send_goal(self, TYPE, SPEED, TARGET_POSE):
        
        # 1. Assign variables:
        goal_msg = Robmove.Goal()
        goal_msg.type = TYPE
        goal_msg.speed = SPEED
        goal_msg.x = TARGET_POSE.position.x
        goal_msg.y = TARGET_POSE.position.y
        goal_msg.z = TARGET_POSE.position.z
        goal_msg.qx = TARGET_POSE.orientation.x
        goal_msg.qy = TARGET_POSE.orientation.y
        goal_msg.qz = TARGET_POSE.orientation.z
        goal_msg.qw = TARGET_POSE.orientation.w
        
        # 2. ACTION CALL:
        self._send_goal_future = self._action_client.send_goal_async(goal_msg)
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        
        goal_handle = future.result()

        if not goal_handle.accepted:
            #self.get_logger().info('RobMove ACTION CALL -> GOAL has been REJECTED.')
            return
        #self.get_logger().info('RobMove ACTION CALL -> GOAL has been ACCEPTED.')
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        
        global RES
        
        # Assign RESULT variable:
        RESULT = future.result().result
        RES.MESSAGE = RESULT.message
        RES.SUCCESS = RESULT.success

# =============================================================================== #
# ROS2 ActionClient for Move:

class MoveClient(Node):

    def __init__(self):

        super().__init__('ros2ir_Move_Client')
        self._action_client = ActionClient(self, Move, 'Move')

        #print ("Waiting for /Robmove ROS2 ActionServer to be available...")
        self._action_client.wait_for_server()
        #print ("/Move ACTION SERVER detected.")

    def send_goal(self, ACTION):
        
        # 1. Assign variables:
        goal_msg = Move.Goal()
        goal_msg.action = ACTION.action
        goal_msg.speed = ACTION.speed
        goal_msg.movej = ACTION.movej
        goal_msg.mover = ACTION.mover
        goal_msg.movel = ACTION.movel
        goal_msg.movexyzw = ACTION.movexyzw
        goal_msg.movexyz = ACTION.movexyz
        goal_msg.moverot = ACTION.moverot
        goal_msg.moveypr = ACTION.moveypr
        goal_msg.moverp = ACTION.moverp
        goal_msg.moveg = ACTION.moveg
        
        # 2. ACTION CALL:
        self._send_goal_future = self._action_client.send_goal_async(goal_msg)
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        
        goal_handle = future.result()

        if not goal_handle.accepted:
            #self.get_logger().info('Move ACTION CALL -> GOAL has been REJECTED.')
            return
        #self.get_logger().info('Move ACTION CALL -> GOAL has been ACCEPTED.')
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        
        global RES
        
        # Assign RESULT variable:
        RESULT = future.result().result
        RES.MESSAGE = RESULT.result

        if "FAILED" in RES.MESSAGE:
            RES.SUCCESS = False
        else:
            RES.SUCCESS = True

# =============================================================================== #
# ABB Robot I/O - ROS2 Service Client:

class abbRWS_IO(Node):

    def __init__(self):
        super().__init__('abbRWS_IO_client')
        self.cli = self.create_client(SetIOSignal, '/rws_client/set_io_signal')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            None
            #print('Waiting for ABB-RWS I/O Service Server to be available...')
        #print('ABB-RWS I/O Service Server detected.')
        self.req = SetIOSignal.Request()

    def send_request(self, signal, value):
        global RES_ABB
        self.req.signal = signal
        self.req.value = value
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        RES_ABB = self.future.result() 

# =============================================================================== #
# Declare ROS2 Init + MoveIt!2 global nodes:

# INITIALISE ROS NODE:
rclpy.init(args=None)

# GLOBAL VARIABLES -> INITIALISE RobMove+Move ACTION CLIENTs + CoordinateSubscriber:
RobMove_CLIENT = RobMoveClient()
Move_CLIENT = MoveClient()
abbIO_CLIENT = abbRWS_IO()
Coordinate_CLIENT = CoordinateSubscriber()

# =============================================================================== #
# CALIB, HomePose and GRIPPER routines:

def calibMoveIt2():

    global Move_CLIENT
    global RES

    CALIB = Action()
    CALIB.action = "MoveR"
    CALIB.speed = 0.1
    CALIB.mover.joint = "joint1"
    CALIB.mover.value = 1.0
    Move_CLIENT.send_goal(CALIB)

    while rclpy.ok():
        rclpy.spin_once(Move_CLIENT)
        if (RES.MESSAGE != "null"):
            break
    
    if (RES.SUCCESS == False):
        rclpy.shutdown()
        print(RES.MESSAGE)
        print("CLOSING PROGRAM...")
        exit()
    
    RES.MESSAGE = "null"
    RES.SUCCESS = False

    CALIB.mover.value = -1.0
    Move_CLIENT.send_goal(CALIB)

    while rclpy.ok():
        rclpy.spin_once(Move_CLIENT)
        if (RES.MESSAGE != "null"):
            break

    if (RES.SUCCESS == False):
        rclpy.shutdown()
        print(RES.MESSAGE)
        print("CLOSING PROGRAM...")
        exit()
    
    RES.MESSAGE = "null"
    RES.SUCCESS = False

def HomePos():

    global Move_CLIENT
    global RES

    ACTION = Action()
    ACTION.action = "MoveJ"
    ACTION.speed = 1.0
    ACTION.movej.joint1 = 0.0
    ACTION.movej.joint2 = -30.0
    ACTION.movej.joint3 = 30.0
    ACTION.movej.joint4 = 0.0
    ACTION.movej.joint5 = 90.0
    ACTION.movej.joint6 = 0.0
    Move_CLIENT.send_goal(ACTION)
    
    while rclpy.ok():
        rclpy.spin_once(Move_CLIENT)
        if (RES.MESSAGE != "null"):
            break

    if (RES.SUCCESS == False):
        rclpy.shutdown()
        print(RES.MESSAGE)
        print("CLOSING PROGRAM...")
        exit()
    
    RES.MESSAGE = "null"
    RES.SUCCESS = False

def GRIPPER(action):

    global abbIO_CLIENT
    global RES_ABB

    if (action == "OPEN"):
        signal = "CloseGripper"
        value = "0"
        abbIO_CLIENT.send_request(signal,value)
        signal = "OpenGripper"
        value = "1"
        abbIO_CLIENT.send_request(signal,value)
    elif (action == "CLOSE"):
        signal = "OpenGripper"
        value = "0"
        abbIO_CLIENT.send_request(signal,value)
        signal = "CloseGripper"
        value = "1"
        abbIO_CLIENT.send_request(signal,value)
    
    RES_ABB = "null"

# ================================================================================= #
# ===================================== MAIN ====================================== #
# ================================================================================= #

def main(args=None):

    # Use a MultiThreadedExecutor to enable processing goals concurrently:
    executor = MultiThreadedExecutor()

    print (" ========== Intelligent Robotics - Short Course ==========")
    print ("(c) Centre for Robotics and Assembly, Cranfield University")
    print ("")

    # Import GLOBAL VARIABLES:
    global RES
    global RES_ABB
    global RobMove_CLIENT
    global Move_CLIENT 
    global abbIO_CLIENT
    global Coordinate_CLIENT

    # 1. OPEN GRIPPER and HomePos:
    GRIPPER("OPEN")
    calibMoveIt2()
    HomePos()

    # 2. Subscribe to /ros2ir_BoxCoordinates until a BOX is detected:
    InfiniteLoop = True
    STEP = 1

    while InfiniteLoop:

        if STEP == 1:

            time.sleep(1)

            rclpy.spin_once(Coordinate_CLIENT, executor=executor)
            if (COORDINATES.x != 0):
                STEP = 2
                print("Cube Pick&Place -> Cube detected! Executing P&P process:")

        if STEP == 2:

            # 3. Obtain ROBOT POSE:

            # Rotation QUATERNION:
            ANGLE = COORDINATES.angle
            if (ANGLE < 80 and ANGLE > 10) or (ANGLE > -80 and ANGLE < -10):
                ROT = toQuaternion(ANGLE)
            else:
                ROT = {"ROTx": 0.0, "ROTy": 1.0, "ROTz": 0.0, "ROTw": 0.0}

            calibMoveIt2()

            # Robot Pose + MOVE:
            TARGET_POSE = Pose()
            TARGET_POSE.position.x = COORDINATES.x
            TARGET_POSE.position.y = COORDINATES.y
            TARGET_POSE.position.z = 1.10
            TARGET_POSE.orientation.x = ROT["ROTx"]
            TARGET_POSE.orientation.y = ROT["ROTy"]
            TARGET_POSE.orientation.z = ROT["ROTz"]
            TARGET_POSE.orientation.w = ROT["ROTw"]

            RobMove_CLIENT.send_goal("PTP", 0.3, TARGET_POSE)

            while rclpy.ok():
                rclpy.spin_once(RobMove_CLIENT)
                if (RES.MESSAGE != "null"):
                    break

            if (RES.SUCCESS == False):
                rclpy.shutdown()
                print(RES.MESSAGE)
                print("CLOSING PROGRAM...")
                exit()
            
            RES.MESSAGE = "null"
            RES.SUCCESS = False

            print("1. Robot Moved to (PickApproach) pose.")

            # 4. Move to PICK POSITION:
            TARGET_POSE.position.z = 1.07

            RobMove_CLIENT.send_goal("LIN", 0.1, TARGET_POSE)

            while rclpy.ok():
                rclpy.spin_once(RobMove_CLIENT)
                if (RES.MESSAGE != "null"):
                    break

            if (RES.SUCCESS == False):
                rclpy.shutdown()
                print(RES.MESSAGE)
                print("CLOSING PROGRAM...")
                exit()
            
            RES.MESSAGE = "null"
            RES.SUCCESS = False

            print("2. Robot Moved to (Pick) pose.")

            # 5. CLOSE GRIPPER:
            time.sleep(0.2)
            GRIPPER("CLOSE")
            time.sleep(0.5)

            print("3. Gripper closed.")

            # 6. Lift CUBE:
            TARGET_POSE.position.z = 1.12

            RobMove_CLIENT.send_goal("LIN", 0.1, TARGET_POSE)

            while rclpy.ok():
                rclpy.spin_once(RobMove_CLIENT)
                if (RES.MESSAGE != "null"):
                    break

            if (RES.SUCCESS == False):
                rclpy.shutdown()
                print(RES.MESSAGE)
                print("CLOSING PROGRAM...")
                exit()
            
            RES.MESSAGE = "null"
            RES.SUCCESS = False

            print("4. Robot Moved to (PickLift) pose.")

            # 7. Move to MID CELL:
            TARGET_POSE.position.x = 0.55
            TARGET_POSE.position.y = 0.52
            TARGET_POSE.position.z = 1.12
            TARGET_POSE.orientation.x = 0.0
            TARGET_POSE.orientation.y = 1.0
            TARGET_POSE.orientation.z = 0.0
            TARGET_POSE.orientation.w = 0.0

            RobMove_CLIENT.send_goal("PTP", 0.3, TARGET_POSE)

            while rclpy.ok():
                rclpy.spin_once(RobMove_CLIENT)
                if (RES.MESSAGE != "null"):
                    break

            if (RES.SUCCESS == False):
                rclpy.shutdown()
                print(RES.MESSAGE)
                print("CLOSING PROGRAM...")
                exit()
            
            RES.MESSAGE = "null"
            RES.SUCCESS = False

            print("5. Robot Moved to (CubeRelease) pose.")

            # 8. OPEN GRIPPER:
            time.sleep(0.2)
            GRIPPER("OPEN")
            time.sleep(0.5)
            print("6. Gripper opened.")

            # 9. BACK TO HomePos:
            HomePos()
            print("7. Robot Moved to (HomePos) pose.")
            print("CubePP routine successfully finished!")
            print("")

            STEP = 1

    rclpy.shutdown()

if __name__ == '__main__':
    main()