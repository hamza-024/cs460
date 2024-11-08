# my_package/lighting_control_node.py

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class LightingControlNode(Node):
    def __init__(self):
        super().__init__('lighting_control_node')
        self.light_pub = self.create_publisher(Float32, '/light_intensity', 10)

    def set_light_intensity(self, intensity):
        msg = Float32()
        msg.data = intensity
        self.light_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = LightingControlNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
