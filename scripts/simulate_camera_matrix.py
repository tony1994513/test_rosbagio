#!/usr/bin/env python
import numpy as np
import rospy
import sys
from rospy.numpy_msg import  numpy_msg
from rospy_tutorials.msg import Floats
import ipdb

_rate = 30

def main():
    
    rospy.init_node("simulate_camera_output", anonymous=True)
    pub = rospy.Publisher('simulate_camera_output_pub', numpy_msg(Floats), queue_size=10)
    rate = rospy.Rate(_rate)
    
    while not rospy.is_shutdown():
        mat = np.random.rand(1920,604)
        pub.publish(mat)
        rate.sleep()

if __name__ == '__main__':
    try:
        sys.exit(main())   
    except rospy.ROSInterruptException:
        pass



