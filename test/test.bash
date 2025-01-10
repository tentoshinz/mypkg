#!/bin/bash
# SPDX-FileCopyrightText: 2025 tento
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc


# launch test

today=`date "+%Y/%m/%d"`
todayweek=`date "+%w"`
weekarray=("Sun" "Mon" "Tue" "Wed" "Thu" "Fri" "Sat")
weekstr=${weekarray[${todayweek}]}

timeout 10 ros2 launch mypkg future_week_calc.launch.py > /tmp/mypkg1.log
sleep 2
cat /tmp/mypkg1.log
cat /tmp/mypkg1.log |
grep "Listen str: ${today} is ${weekstr}" || 
{ echo "failure: use launch"; res=$((res + 1)); }


# zellers run test

search_num=1

search_str() {
    local search_str="$1"
    local current_line=$((search_num * 2 - 1))

    line_str=$(sed -n "${current_line}p" "/tmp/mypkg.log")

    if echo "$line_str" | grep -q "$search_str"; then
        echo success: "$search_num"
    else
        echo failure: run "$search_num"
	    res=$((res + 1))
    fi

    search_num=$((search_num + 1))
}




ros2 run mypkg zellers &
run_pid=$!

ros2 topic echo /calc_week > /tmp/mypkg.log &
echo_pid=$!


sleep 3

ros2 topic pub --once /date std_msgs/msg/UInt32 "data: 20040601"
ros2 topic pub --once /date std_msgs/msg/UInt32 "data: 19920719"
ros2 topic pub --once /date std_msgs/msg/UInt32 "data: 19780216"
ros2 topic pub --once /date std_msgs/msg/UInt32 "data: 20250105"


sleep 3

cat /tmp/mypkg.log

echo "kill start"

kill $run_pid
kill $echo_pid
echo "kill now"
wait
sleep 3

echo "kill end"

sleep 2
search_str "data: 3"
sleep 2
search_str "data: 1"
sleep 2
search_str "data: 5"
sleep 2
search_str "data: 1"
sleep 2






echo jobs
jobs -l

sleep 3

echo killed jobs
jobs -l


sleep 5

echo "res= $res"
cat /tmp/mypkg.log


exit $res


