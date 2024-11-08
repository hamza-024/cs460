#!/usr/bin/env python

#!/usr/bin/env python

import os
import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import RegisterEventHandler
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from webots_ros2_driver.webots_launcher import WebotsLauncher
from webots_ros2_driver.webots_controller import WebotsController
from webots_ros2_driver.wait_for_controller_connection import WaitForControllerConnection


def generate_launch_description():
    package_dir = get_package_share_directory('my_environments')
    world = LaunchConfiguration('world', default='indoor.wbt')
    use_sim_time = LaunchConfiguration('use_sim_time', default=True)

    webots = WebotsLauncher(
        world=PathJoinSubstitution([package_dir, 'worlds', world]),
        ros2_supervisor=True
    )

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': '<robot name=""><link name=""/></robot>'}],
    )

    footprint_publisher = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        output='screen',
        arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'base_footprint'],
    )

    controller_manager_timeout = ['--controller-manager-timeout', '50']
    diffdrive_controller_spawner = Node(
        package='controller_manager',
        executable='spawner',
        output='screen',
        arguments=['diffdrive_controller'] + controller_manager_timeout,
    )
    joint_state_broadcaster_spawner = Node(
        package='controller_manager',
        executable='spawner',
        output='screen',
        arguments=['joint_state_broadcaster'] + controller_manager_timeout,
    )

    turtlebot_driver = WebotsController(
        robot_name='TurtleBot3Burger',
        parameters=[{'use_sim_time': use_sim_time}],
        remappings=[('/diffdrive_controller/cmd_vel_unstamped', '/cmd_vel'), ('/diffdrive_controller/odom', '/odom')],
        respawn=True
    )

    waiting_nodes = WaitForControllerConnection(
        target_driver=turtlebot_driver,
        nodes_to_start=[diffdrive_controller_spawner, joint_state_broadcaster_spawner]
    )

    return LaunchDescription([
        DeclareLaunchArgument('world', default_value='indoor.wbt', description='World file name'),
        webots, webots._supervisor, waiting_nodes, robot_state_publisher,
        footprint_publisher, turtlebot_driver,
        launch.actions.RegisterEventHandler(
            event_handler=launch.event_handlers.OnProcessExit(
                target_action=webots,
                on_exit=[launch.actions.EmitEvent(event=launch.events.Shutdown())],
            )
        ),
    ])
