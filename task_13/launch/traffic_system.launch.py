from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    return LaunchDescription([

        DeclareLaunchArgument('safety_zone', default_value='2.0'),
        DeclareLaunchArgument('robot_priority', default_value='1'),
        DeclareLaunchArgument('robot_position', default_value='0.0'),

        Node(
            package='task_12_pkg',
            executable='traffic_node', 
            parameters=[{'safety_zone': LaunchConfiguration('safety_zone')}]
        ),


        Node(
            package='task_12_pkg',
            executable='fleet_node',  
            parameters=[{
                'robot_position': LaunchConfiguration('robot_position'),
                'robot_priority': LaunchConfiguration('robot_priority')
            }]
        )
    ])