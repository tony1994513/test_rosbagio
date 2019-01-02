#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from scipy.misc import imread,imsave
from numpy import zeros
import numpy as np
import sys
import ipdb


count = 0

def usage():
    return "please input image height,width,fps. for example 640 720 30"

def generate_fake_img_random(img_height,img_width):
    img = np.zeros([img_height,img_width],dtype=np.uint8)  
    for x in range(img_height):
        for y in range(img_width):
            if x % 2 == 0:
                if y % 4 == 0 :
                    rondom = np.random.randint(low=0, high=255)     
                    img[x,y] = rondom
                else:
                    img[x,y] = rondom
            else:
                img[x,:] = img[x-1,:]    
    return img


def generate_pattern(img_height,img_width):
    global count
    img = np.ones([img_height,img_width],dtype=np.uint8)* 255 # white
    if count % 4 == 0:
        img[0:img_height/2,0:img_width/2] = 0
    elif count % 4 == 1:
        img[0:img_height/2,img_width/2:img_width] = 0
    elif count % 4 == 2:
        img[img_height/2:img_height,img_width/2:img_width] = 0
    elif count % 4 == 3:
        img[img_height/2:img_height,0:img_width/2] = 0
    return img

def main():
    # img_height = 1208 
    # img_width = 1920 * 2
    # _rate = 1

    rospy.init_node("generate_fake_img", anonymous=True)
    img_height = int(rospy.get_param('img_height', 1208))
    img_width = int(rospy.get_param('img_width', 1920))*2
    _rate = int(rospy.get_param('fps', 30))

    pub = rospy.Publisher('simulate_camera_output_pub', Image, queue_size=10)
    rate = rospy.Rate(_rate)
    
    while not rospy.is_shutdown():
        global count
        count = count + 1
        # img = generate_fake_img_random()
        img = generate_pattern(img_height,img_width)
        msg = Image()
        msg.data = img.tostring()
        msg.header.stamp = rospy.Time.now()
        msg.height = img_height 
        msg.width = img_width / 2
        msg.encoding = 'bayer_rggb16'
        msg.is_bigendian = 0
        msg.step = img_width        
        pub.publish(msg)
        rate.sleep()


if __name__ == '__main__':
    try:
        sys.exit(main())   
    except rospy.ROSInterruptException:
        pass
