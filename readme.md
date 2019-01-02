## Usage
Test rosbag performace. Especially for test rosbag record parameter `duration` and `chunksize`.  
## How to run

1. Runing roscore
 `roscore`
2. Runing bash shell
 ` ./run.sh`

#### Change path based on your own case
Read start_process comment for more details

#### csv data
Already tested the code in my own computer. Related `csv` file located in `/csv` folder


#### how to test hard drive reading speed
`dd if=/dev/zero of=/media/shuangda/EVO1/bag/test.txt  bs=8k count=10k conv=fdatasync; rm -f /media/shuangda/EVO1/bag/test.txt`