/*

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

*/

// ros2ir_simplepackage/src/HelloWorld.cpp:

// ================================================================================= //
// Import libraries:

// Library required to execute ROS 2 w/ C++:
#include "rclcpp/rclcpp.hpp"

// Generic library:
#include <iostream>

// ================================================================================= //
// ===================================== MAIN ====================================== //
// ================================================================================= //

int main(int argc, char **argv)
{

    rclcpp::init(argc, argv);

    std::cout << " ========== Intelligent Robotics - Short Course ========== \n";
    std::cout << "(c) Centre for Robotics and Assembly, Cranfield University \n";
    std::cout << "\n";

    std::cout << "Hello world! \n";
    std::cout << "\n";

    std::cout << "Closing program... Bye! \n";

    rclcpp::shutdown();
    return 0;

}