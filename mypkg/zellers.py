# SPDX-FileCopyrightText: 2025 tento
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16, UInt32, String
from rclpy.exceptions import ExternalShutdownException


class Zellers(Node):
    def __init__(self):
        super().__init__("zellers")
        self.sub = self.create_subscription(UInt32, "date", self.cb, 10)
        self.pub_week_num = self.create_publisher(Int16, "calc_week", 10)
        self.pub_week_str = self.create_publisher(String, "calc_week_str", 10)

    def cb(self, msg):
        subdate = str(msg.data)

        year = int(subdate[0:4])
        month = int(subdate[4:6])
        day = int(subdate[6:8])
        
        y = year
        m = month
        d = day

        if m <= 2:
            m = m + 12
            y -= 1

        C = y // 100
        Y = y % 100

        h = ( d + (26*(m+1)//10) + Y + (Y//4) - (2*C) + C//4 ) %7 

        msg_weeknum = Int16()
        msg_weekstr = String()
        week = ['Sat','Sun','Mon','Tue','Wed','Thu','Fri']

        msg_weeknum.data = h
        msg_weekstr.data = (f"{year}/{month:02d}/{day:02d} is {week[h]}")
        
        self.pub_week_num.publish(msg_weeknum)
        self.pub_week_str.publish(msg_weekstr)



def main():
    rclpy.init()
    node = Zellers()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    except ExternalShutdownException:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

    # rclpy.spin(node)
    # node.destroy_node()
    # rclpy.shutdown()