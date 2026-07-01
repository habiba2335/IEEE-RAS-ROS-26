import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose2D
from std_msgs.msg import Int32
from rclpy.executors import SingleThreadedExecutor

class Fleet(Node):

    def __init__(self, robot_name, x, y, priority):
        super().__init__(robot_name)

        self.robot_name = robot_name
        self.current_x = x
        self.current_y = y
        self.priority = priority


        self.pos_publisher= self.create_publisher(Pose2D, f'{robot_name}_position', 10)
        self.pri_publisher= self.create_publisher(Int32, f'{robot_name}_priority', 10)
        self.timer = self.create_timer (0.1 , self.timer_callback)

    def timer_callback(self):
        p_msg = Pose2D()
        p_msg.x = self.current_x
        p_msg.y = self.current_y
        self.pos_publisher.publish(p_msg)
        i_msg = Int32()
        i_msg.data = self.priority
        self.pri_publisher.publish(i_msg)
        self.get_logger().info(f'position: ({p_msg.x},{p_msg.y}) and Priority: {i_msg.data}')

def main (args = None):
    rclpy.init(args = args)
    robot1 = Fleet("robot1", 0.0, 0.0, 1)
    robot2 = Fleet("robot2", 1.0, 1.0, 2)
    robot3 = Fleet("robot3", 15.0, 15.0, 3)

    executor = SingleThreadedExecutor()
    executor.add_node(robot1)
    executor.add_node(robot2)
    executor.add_node(robot3)

    try:
       
        executor.spin()
    except KeyboardInterrupt:
        pass
    finally:
        
        robot1.destroy_node()
        robot2.destroy_node()
        robot3.destroy_node()

        rclpy.shutdown()

if __name__ == '__main__':
    main()
