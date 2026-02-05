import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import TwistStamped


class RobotController(Node):
    def __init__(self):
        super().__init__('robot_controller')

        self.subscription = self.create_subscription(
            String,
            'gesture_cmd',
            self.gesture_callback,
            10
        )

        self.publisher = self.create_publisher(
            TwistStamped,
            'cmd_vel',
            10
        )

        self.get_logger().info("🤖 Robot Controller Started (TwistStamped)")

    def gesture_callback(self, msg):
        twist = TwistStamped()
        twist.header.stamp = self.get_clock().now().to_msg()
        twist.header.frame_id = "base_link"

        if msg.data == "FORWARD":
            twist.twist.linear.x = 0.2
            twist.twist.angular.z = 0.0

        elif msg.data == "LEFT":
            twist.twist.linear.x = 0.0
            twist.twist.angular.z = 0.6

        elif msg.data == "RIGHT":
            twist.twist.linear.x = 0.0
            twist.twist.angular.z = -0.6

        elif msg.data == "STOP":
            twist.twist.linear.x = 0.0
            twist.twist.angular.z = 0.0

        self.publisher.publish(twist)


def main():
    rclpy.init()
    node = RobotController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
