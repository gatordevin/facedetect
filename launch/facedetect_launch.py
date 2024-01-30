from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    realsense2_camera_launch_dir = get_package_share_directory('realsense2_camera')

    return LaunchDescription([
        # Include the RealSense launch file
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([realsense2_camera_launch_dir, '/launch/rs_launch.py']),
            launch_arguments={'depth_module.profile': '640x480x30'}.items()
        ),

        # Launch the facedetect node
        Node(
            package='facedetect',
            namespace='facedetect',
            executable='my_node',
            name='facedetect_node',
            output='screen'
        ),

        # Run rqt_image_view
        ExecuteProcess(
            cmd=['ros2', 'run', 'rqt_image_view', 'rqt_image_view'],
            output='screen'
        ),
    ])
