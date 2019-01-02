#!/usr/bin/env bash
duration=$1
chunksize=$2
echo "First arg: $1"
echo "Second arg: $2"

# start node
cd /home/shuangda/ros/xpeng_ws/src/test_rosbagio/scripts # location of simulate_camera_matrix.py; Change path based on your own case

nohup python simulate_camera_matrix.py > /dev/null 2>&1 & echo $! > /tmp/ros_node.pid


file_name="duration"${duration}_"chunksize"${chunksize}.csv
echo "saving to filename: ${file_name}"

cd /home/shuangda/tmp/csv # location of csv files;
nohup dstat -cd --output ${file_name} > /dev/null 2>&1 & echo $! > /tmp/monitor.pid

cd /home/shuangda/tmp/bag # location of bag files;
nohup rosbag record --split --duration=${duration} --chunksize=${chunksize} /simulate_camera_output_pub > /dev/null 2>&1 & echo $! > /tmp/bag.pid

echo "Going to sleep 20s"
sleep 20

echo "Going to kill long runing pid"

kill -9 `cat /tmp/bag.pid`
kill -9 `cat /tmp/monitor.pid`
kill -9 `cat /tmp/ros_node.pid`
kill -9 `ps -ef | awk '$8=="/opt/ros/kinetic/lib/rosbag/record" {print $2}'`
 # when launching rosbag record, another 'roscord pid' also will be launch. Need kill two of them


rm /home/shuangda/tmp/bag/*.bag # remove bag file
rm /home/shuangda/tmp/bag/*.bag.active