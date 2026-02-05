import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import os

GESTURE_FILE = "/tmp/gesture.txt"

class GestureReader(Node):
    def __init__(self):
        super().__init__('gesture_reader')
        self.publisher = self.create_publisher(String, 'gesture_cmd', 10)
        self.timer = self.create_timer(0.1, self.read_gesture)

    def read_gesture(self):
        if os.path.exists(GESTURE_FILE):
            with open(GESTURE_FILE, "r") as f:
                gesture = f.read().strip()

            if gesture:
                msg = String()
                msg.data = gesture
                self.publisher.publish(msg)
                self.get_logger().info(f"Gesture: {gesture}")

def main():
    rclpy.init()
    node = GestureReader()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

