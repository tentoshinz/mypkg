# SPDX-FileCopyrightText: 2025 tento
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import UInt32
from datetime import datetime, timedelta

class Pubdate(Node):
    def __init__(self):
        super().__init__("pubdate")
        self.pub = self.create_publisher(UInt32, "date", 10)
        self.create_timer(1.0, self.cb)

        self.n = 0
        self.date = datetime.today().date()

    def cb(self):
        added_date = self.date + timedelta(days=self.n)
        self.n += 1

        msg = UInt32()
        msg.data = int(added_date.strftime('%Y%m%d'))
        self.pub.publish(msg)


def main():
    rclpy.init()
    node = Pubdate()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
