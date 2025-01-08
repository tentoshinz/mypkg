#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

today=`date "+%Y/%m/%d"`

todayweek=`date "+%w"`
weekarray=("Sun" "Mon" "Tue" "Wed" "Thu" "Fri" "Sat")
weekstr=${weekarray[${todayweek}]}

timeout 10 ros2 launch mypkg future_week_calc.launch.py > /tmp/mypkg.log
cat /tmp/mypkg.log |
grep "Listen str: ${today} is ${weekstr}"


# ros2 run mypkg zellers &

{ timeout 10 ros2 topic pub /date std_msgs/msg/UInt32 "data: 20040601"; } || true &
{ timeout --signal=SIGINT 13 ros2 run mypkg zellers; } || true &
{ timeout 16 ros2 topic echo /calc_week > /tmp/mypkg.log; } || true
wait
cat /tmp/mypkg.log |
grep "data: 3"

{ timeout 10 ros2 topic pub /date std_msgs/msg/UInt32 "data: 19920719"; } || true &
{ timeout --signal=SIGINT 13 ros2 run mypkg zellers 13 ros2 run mypkg zellers; } || true &
{ timeout 16 ros2 topic echo /calc_week > /tmp/mypkg.log; } || true
wait
cat /tmp/mypkg.log |
grep "data: 1"


# timeout 10 ros2 run mypkg zellers



