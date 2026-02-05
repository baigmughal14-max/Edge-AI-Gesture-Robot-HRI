from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    turtlebot_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('turtlebot3_gazebo'),
                'launch',
                'turtlebot3_world.launch.py'
            )
        )
    )

    gesture_reader = Node(
        package='gesture_recognition',
        executable='gesture_reader',
        name='gesture_reader',
        output='screen'
    )

    robot_controller = Node(
        package='gesture_recognition',
        executable='robot_controller',
        name='robot_controller',
        output='screen'
    )

    return LaunchDescription([
        turtlebot_launch,
        gesture_reader,
        robot_controller
    ])
