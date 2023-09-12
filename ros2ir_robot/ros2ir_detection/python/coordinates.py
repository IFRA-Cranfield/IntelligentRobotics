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

# ros2ir_robot/ros2ir_detection/python/coordinates.py:

# ================================================================================= #

# Library required to execute ROS2 w/ Python:
import rclpy
from rclpy.node import Node

# Import libraries for OpenCV and YOLO:
import os
import cv2
from ultralytics import YOLO
from cv2 import aruco
import numpy as np
import time

# ================================================================================= #
# ===================================== MAIN ====================================== #
# ================================================================================= #

def main(args=None):

    rclpy.init()

    print (" ========== Intelligent Robotics - Short Course ==========")
    print ("(c) Centre for Robotics and Assembly, Cranfield University")
    print ("")

    # Initialise YOLO model:
    ModelPath = os.path.join(os.path.expanduser('~'), 'dev_ws', 'src', 'IntelligentRobotics', 'ros2ir_robot', 'ros2ir_detection', 'yolov8') + "/yolov8model.pt"
    YOLOModel = YOLO(ModelPath)
    ModelNames = YOLOModel.names

    # Parameters: CALIBRATION, Arucos...
    w = 700
    h = 400
    aruco_param = cv2.aruco.DetectorParameters()
    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_1000)
    aruco_detector = aruco.ArucoDetector(aruco_dict, aruco_param)

    # Capture image data from WEBCAM using OpenCV:
    cap = cv2.VideoCapture(0)

    # READ cam input for about 1second:
    T = time.time() + 1.0
    while (time.time() <= T):
        ret, outputImage = cap.read()

    # ========== ARUCO: CALIBRATION ========== #
        
    # Detect ARUCO MARKERS and calibrate:
    markerCorners, markerIds, rejectedCandidates = aruco_detector.detectMarkers(outputImage)
    src = np.zeros((4, 2), dtype=np.float32)  # Points of the corners from the input image.
    dst = np.array([[0.0, 0.0], [w, 0.0], [0.0, h], [w, h]], dtype=np.float32)  # Points calibrated with w and h.
    poly_corner = np.zeros((4, 3), dtype=np.int32)
    
    # Get the first corner & ID of the markers:
    for i in range(4):
        poly_corner[i][0] = int(markerIds[i][0])
        poly_corner[i][1] = int(markerCorners[i][0][0][0])
        poly_corner[i][2] = int(markerCorners[i][0][0][1])

    # Arrange by ID: 
    for i in range(3):
        for j in range(i + 1, 4):
            if poly_corner[i][0] > poly_corner[j][0]:
                for k in range(3):
                    aux = poly_corner[i][k]
                    poly_corner[i][k] = poly_corner[j][k]
                    poly_corner[j][k] = aux

    # Get the source vector:
    for i in range(4):
        src[i] = np.array([poly_corner[i][1], poly_corner[i][2]], dtype=np.float32)

    # Get the transform matrix:
    perspTransMatrix = cv2.getPerspectiveTransform(src, dst)

    # Now that the calibration output -> PERSPECTIVE TRANSFORMATION MATRIX
    # has been obtained, it's time to detect and locate the box!

    while cap.isOpened():

        ret, frame = cap.read()
        cv2.aruco.drawDetectedMarkers(frame, markerCorners, markerIds)

        if not ret:
            break

        PERSPECTIVE = np.zeros_like(frame)

        # Get image of the perspective:
        PERSPECTIVE = cv2.warpPerspective(M=perspTransMatrix, dsize=(700, 400), src=frame)

        # =============== YOLO: DETECTION =============== #
        RESULT = YOLOModel(PERSPECTIVE)
        OUTPUT = RESULT[0].plot()
        cv2.imshow("YOLOv8 Model: CUBE DETECTION", OUTPUT)
        # =============== YOLO: DETECTION =============== #

        # =========== COORDINATE SUPPLY =========== #

        # PROCESS RESULTS:
        boxes = RESULT[0].boxes
        ids = []
        for box in boxes:
            box = boxes.xyxy
            for c in boxes.cls:
                ids.append(ModelNames[int(c)])

        if (len(boxes) == 0):

            xo = 0.0
            yo = 0.0
            angle = 0.0

        else:
        
            # GET ROI(Region-of-Interest):
            x1, y1, x2, y2 = boxes[0].xyxy[0]
            x = int(x1)-3
            y = int(y1)-3
            w = int(x2)+3
            h = int(y2)+3
            ROI = PERSPECTIVE[y:h, x:w]

            # Image PROCESSING to get COORDINATES:
            ROI = cv2.GaussianBlur(ROI,(3,3),0)
            imgHSV = cv2.cvtColor(ROI, cv2.COLOR_BGR2HSV)
            lowLimit = (10, 100, 20)
            upLimit = (25, 255, 255)
            mask = cv2.inRange(imgHSV, lowLimit, upLimit)

            # Find the contours in the dilated image:
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            poly_contour = []
            for contour in contours:
                area = cv2.contourArea(contour)
                if area > 500:
                    poly_contour.append(contour)
            
            if not poly_contour:
                xo = 0.0
                yo = 0.0
                angle = 0.0

            if poly_contour:
                cv2.drawContours(ROI, poly_contour, -1, (0, 255, 0), 1)

                # GET -> x0, y0 coordinates:
                for cnt in poly_contour:
                    rect = cv2.minAreaRect(cnt)
                    (xo, yo), (wo, ho), angle = rect
                    xo = xo + x
                    yo = yo + y
                    box = cv2.boxPoints(rect)
                    box = np.int0(box)
                    cv2.polylines(ROI, [box], True, (255,0,0), 2)

                cv2.imshow("YOLOv8 Model: CUBE DETECTION - ROI", ROI)

                # TRANSFORM to: CELL(m)
                COORD_x = y/1000 + 0.35
                COORD_y = x/1000 + 0.20
                COORD_angle = angle

        print("x -> " + str(COORD_x))
        print("y -> " + str(COORD_y))
        print("angle -> " + str(COORD_angle))
        print("")

        # Press key q to exit:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        

    print("")
    print("")
    print("Closing program... BYE!")
    rclpy.shutdown()

if __name__ == '__main__':
    main()