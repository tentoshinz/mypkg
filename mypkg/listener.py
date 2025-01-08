# SPDX-FileCopyrightText: 2025 tento
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16, String

class sub_week(Node):
    def __init__(self):
        super().__init__("sub_num")
        self.subnum = self.create_subscription(Int16, "calc_week", self.cb_num, 10)
        self.substr = self.create_subscription(String, "calc_week_str", self.cb_str, 10)
    
    def cb_num(self, msg):
        self.get_logger().info("Listen num: %d" % msg.data) 

    def cb_str(self, msg):
        self.get_logger().info("Listen str: %s" % msg.data) 


def main():
    rclpy.init()
    node= sub_week()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
