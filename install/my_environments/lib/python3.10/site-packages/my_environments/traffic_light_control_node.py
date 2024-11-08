# my_package/traffic_light_control_node.py

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class TrafficLightControlNode(Node):
    def __init__(self):
        super().__init__('traffic_light_control_node')
        self.traffic_light_pub = self.create_publisher(Int32, '/traffic_light_color', 10)

    def change_light(self, color_code):
        msg = Int32()
        msg.data = color_code  # 0 for red, 1 for yellow, 2 for green
        self.traffic_light_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TrafficLightControlNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
