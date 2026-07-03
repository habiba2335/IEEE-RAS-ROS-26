import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose2D
from std_msgs.msg import Int32
from rclpy.executors import SingleThreadedExecutor
import math

class Traffic(Node):

    def __init__(self):
        super().__init__('traffic')

        self.r1_x, self.r1_y, self.r1_p = 0.0, 0.0, 0
        self.r2_x, self.r2_y, self.r2_p = 0.0, 0.0, 0
        self.r3_x, self.r3_y, self.r3_p = 0.0, 0.0, 0

        self.declare_parameter('safety_zone', 2.0)
        self.safe_distance= self.get_parameter('safety_zone').get_parameter_value().double_value

        self.create_subscription(Pose2D, 'robot1_position', self.r1_pos_cb, 10)
        self.create_subscription(Int32, 'robot1_priority', self.r1_pri_cb, 10)
        
        self.create_subscription(Pose2D, 'robot2_position', self.r2_pos_cb, 10)
        self.create_subscription(Int32, 'robot2_priority', self.r2_pri_cb, 10)
        
        self.create_subscription(Pose2D, 'robot3_position', self.r3_pos_cb, 10)
        self.create_subscription(Int32, 'robot3_priority', self.r3_pri_cb, 10)

        self.timer = self.create_timer(1.0, self.decision)

    def r1_pos_cb(self, msg):
        self.r1_x = msg.x
        self.r1_y = msg.y
    def r1_pri_cb(self, msg):
        self.r1_p = msg.data

    def r2_pos_cb(self, msg):
        self.r2_x = msg.x
        self.r2_y = msg.y
    def r2_pri_cb(self, msg):
        self.r2_p = msg.data

    def r3_pos_cb(self, msg):
        self.r3_x = msg.x
        self.r3_y = msg.y
    def r3_pri_cb(self, msg):
        self.r3_p = msg.data

    def decision(self):
        robots_list = [
            {'name': 'Robot 1', 'x': self.r1_x, 'y': self.r1_y, 'p': self.r1_p},
            {'name': 'Robot 2', 'x': self.r2_x, 'y': self.r2_y, 'p': self.r2_p},
            {'name': 'Robot 3', 'x': self.r3_x, 'y': self.r3_y, 'p': self.r3_p}
        ]

        num_robots = len(robots_list)

        for i in range(num_robots):
            for j in range(i + 1, num_robots):
                robot_A = robots_list[i]
                robot_B = robots_list[j]

                dist = math.sqrt((robot_A['x'] - robot_B['x'])**2 + (robot_A['y'] - robot_B['y'])**2)

                if dist <= self.safe_distance:
                    if robot_A['p'] < robot_B['p']:
                        self.get_logger().warn(f'[DANGER] between {robot_A["name"]} & {robot_B["name"]}! {robot_B["name"]} MUST YIELD')
                    else:
                        self.get_logger().warn(f'[DANGER] between {robot_A["name"]} & {robot_B["name"]}! {robot_A["name"]} MUST YIELD')
                else:
                    self.get_logger().info(f'[CLEAR] {robot_A["name"]} & {robot_B["name"]} are at a safe distance')

def main(args=None):
    rclpy.init(args=args)
    manager_node = Traffic()
    
    try:
        rclpy.spin(manager_node)
    except KeyboardInterrupt:
        pass
    finally:
        manager_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()