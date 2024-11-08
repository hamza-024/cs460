import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/hadnan/ros2_ws/src/my_environments/install/my_environments'
