#!/bin/bash
# SPDX-FileCopyrightText: 2025 tento
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc


res=0

error () {
    echo failure: ${1},
	res=$((res + 1))
}


today=`date "+%Y/%m/%d"`
todayweek=`date "+%w"`
weekarray=("Sun" "Mon" "Tue" "Wed" "Thu" "Fri" "Sat")
weekstr=${weekarray[${todayweek}]}

timeout 10 ros2 launch mypkg future_week_calc.launch.py > /tmp/mypkg.log
wait $!
cat /tmp/mypkg.log |
grep "Listen str: ${today} is ${weekstr}" || error "$LINENO"


ros2 run mypkg zellers &
ROS_PID=$!

{ timeout 10 ros2 topic pub /date std_msgs/msg/UInt32 "data: 20040601"; } &
timeout 12 ros2 topic echo /calc_week > /tmp/mypkg.log
wait $!
cat /tmp/mypkg.log |
grep "data: 3" || error "$LINENO"


{ timeout 10 ros2 topic pub /date std_msgs/msg/UInt32 "data: 19920719"; } &
timeout 12 ros2 topic echo /calc_week > /tmp/mypkg.log
wait $!
cat /tmp/mypkg.log |
grep "data: 1" || error "$LINENO"

{ timeout 10 ros2 topic pub /date std_msgs/msg/UInt32 "data: 19780216"; } &
timeout 12 ros2 topic echo /calc_week > /tmp/mypkg.log
wait $!
cat /tmp/mypkg.log |
grep "data: 5" || error "$LINENO"

{ timeout 10 ros2 topic pub /date std_msgs/msg/UInt32 "data: 20250105"; } &
timeout 12 ros2 topic echo /calc_week > /tmp/mypkg.log
wait $!
cat /tmp/mypkg.log |
grep "data: 1" || error "$LINENO"

kill -SIGINT $ROS_PID


exit $res


