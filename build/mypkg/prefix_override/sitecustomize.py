import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/tento/ros2_ws/src/robosys2024_ros/install/mypkg'
