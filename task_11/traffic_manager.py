#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose2D
from std_msgs.msg import Int32
import math


class Traffic(Node):
    def __init__(self):
     super().__init__('traffic')

     self.my_x = 0.0
     self.my_y = 0.0
     self.my_priority = 5
     self.other_priority = 0

     self.priority_sub = self.create_subscription(Int32, 'robot_priority', self.priority_callback, 10)
     self.pose_sub = self.create_subscription(Pose2D, 'robot_pose', self.pose_callback, 10)
     self.get_logger().info('Traffic Node has started!')

    def priority_callback(self, msg):
     self.other_priority = msg.data


    def pose_callback(self, msg):
        other_x = msg.x
        other_y = msg.y
        
        distance = math.sqrt((other_x - self.my_x)**2 + (other_y - self.my_y)**2)

        if distance < 2.0 and self.other_priority > self.my_priority:
            self.get_logger().warn(f'[DANGER]! Robot approaching with higher priority = {self.other_priority} and Distance = {distance:.2f}')
        else:
            self.get_logger().info(f'[CLEAR]! Distance = {distance:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = Traffic()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

