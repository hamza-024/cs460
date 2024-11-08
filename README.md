# CS460 Project 

## Overview

This package, `my_environments`, provides ROS 2 launch files for simulating `indoor` and `outdoor` environments in Webots using ROS 2 Humble. It allows users to easily set up and launch Webots simulations within a ROS 2 environment.

## Prerequisites

- **ROS 2 Humble** installed on your system.
- **Webots** installed and configured on your machine, with the `WEBOTS_HOME` environment variable set to the Webots installation directory.

## Setup Instructions

### Step 1: Source ROS 2 Humble

Start by sourcing the ROS 2 Humble setup file:
```bash
source /opt/ros/humble/setup.bash
```

### Step 2: Set the Webots Home Directory

To specify the Webots installation path, export `WEBOTS_HOME` as follows:
```bash
export WEBOTS_HOME=/mnt/c/Program\ Files/Webots
```

### Step 3: Build the Package

Navigate to your ROS workspace and build the package:
```bash
cd my_environments
colcon build
```

### Step 4: Source the Workspace

After building, source the workspace to ensure the package is accessible:
```bash
source install/setup.bash
```

## Launching the Simulations

### Indoor Environment

To launch the `indoor.wbt` world file, run:
```bash
ros2 launch my_environments indoor_launch.py
```

### Outdoor Environment

To launch the `outdoor.wbt` world file, run:
```bash
ros2 launch my_environments outdoor_launch.py
```

## Troubleshooting

- **Environment Variables**: Confirm that `WEBOTS_HOME` is correctly set to your Webots installation path.
- **Build Issues**: If the package doesn’t appear after building, try sourcing the workspace again with `source install/setup.bash`.
- **Launch Errors**: Ensure Webots is properly installed, accessible, and that all dependencies for ROS 2 are satisfied.
