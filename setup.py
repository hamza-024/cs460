from setuptools import find_packages, setup

package_name = 'my_environments'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include both launch files
        ('share/' + package_name + '/launch', [
            'launch/outdoor_launch.py',
            'launch/indoor_launch.py'
        ]),
        # Include both world files
        ('share/' + package_name + '/worlds', [
            'worlds/outdoor.wbt',
            'worlds/indoor.wbt'
        ]),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hadnan',
    maintainer_email='hadnan@todo.todo',
    description='ROS package for simulating outdoor and indoor environments',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)
