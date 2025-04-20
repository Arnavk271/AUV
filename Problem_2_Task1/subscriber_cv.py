#!/usr/bin/env python3

import rospy


from sensor_msgs.msg import Image #importing 
from cv_bridge import CvBridge #bridge is used to convert image from opencv to ros 


import cv2 #importing cv2

def callback(msg):

    frame = bridge.imgmsg_to_cv2(msg, desired_encoding="mono 8")
    
    cv2.imshow("Edge Detected Image", frame)
    cv2.waitKey(1)
    

def main():


    rospy.init_node("edge_subscriber_node")
    rospy.Subscriber("edge_image", Image, callback) #subscriber is used 
    
    rospy.spin()

bridge = CvBridge() #bridge is used 


if __name__ == "__main__":
    main()

