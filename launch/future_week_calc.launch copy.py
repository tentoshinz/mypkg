# SPDX-FileCopyrightText: 2025 tento
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():
    listener = launch_ros.actions.Node(
            package = 'mypkg',
            executable = 'listener',
            output = 'screen'
            )
    
    pubdate = launch_ros.actions.Node(
            package = 'mypkg',
            executable = 'pubdate',
            )
    
    zellers = launch_ros.actions.Node(
            package = 'mypkg',
            executable = 'zellers',
            )
    

    return launch.LaunchDescription([listener, pubdate, zellers])