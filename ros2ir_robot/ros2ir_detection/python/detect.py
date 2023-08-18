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

# ros2ir_robot/ros2ir_detection/python/detect.py:

# ================================================================================= #
# Import libraries:
import os
import cv2
from ultralytics import YOLO

# ================================================================================= #
# ===================================== MAIN ====================================== #
# ================================================================================= #

def main(args=None):

    print (" ========== Intelligent Robotics - Short Course ==========")
    print ("(c) Centre for Robotics and Assembly, Cranfield University")
    print ("")

    # 0. Initialise YOLO model:
    ModelPath = os.path.join(os.path.expanduser('~'), 'dev_ws', 'src', 'IntelligentRobotics', 'ros2ir_robot', 'ros2ir_detection', 'yolov8') + "/yolov8model.pt"
    YOLOModel = YOLO(ModelPath)
    ModelNames = YOLOModel.names

    # 1. Capture image data from WEBCAM using OpenCV:
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    # 2. Execute YOLO PREDICT:

    while cap.isOpened():

        ret, frame = cap.read()

        if not ret:
            break

        RESULT = YOLOModel(frame)
        OUTPUT = RESULT[0].plot()
        cv2.imshow("YOLOv8 Model: CUBE DETECTION", OUTPUT)

        # Press key q to exit:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    print("")
    print("")
    print("Closing program... BYE!")

if __name__ == '__main__':
    main()