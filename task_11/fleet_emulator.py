#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose2D
from std_msgs.msg import Int32


class Fleet(Node):
    def __init__(self):
     super().__init__('fleet')

     self.pose = self.create_publisher(Pose2D, 'robot_pose', 10)
     self.priority = self.create_publisher(Int32, 'robot_priority', 10)
     self.timer = self.create_timer(0.1, self.publish_data)
     self.get_logger().info('Fleet Node has started!')

    def publish_data(self):
        x = 1.2          
        y = 1.0          
        priority = 2

        pose_msg = Pose2D()
        pose_msg.x = x
        pose_msg.y = y
        pose_msg.theta = 0.0
        self.pose.publish(pose_msg)

        priority_msg = Int32()
        priority_msg.data = priority
        self.priority.publish(priority_msg)

        self.get_logger().info(f'Position: ({x}, {y}), Priority: {priority}')

def main(args=None):
    rclpy.init(args=args)
    node = Fleet()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
