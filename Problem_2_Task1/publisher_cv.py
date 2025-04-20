#!/usr/bin/env python3

import rospy
import depthai as dai#depth ai is imported


import cv2 #imported cv2 cam


from sensor_msgs.msg import Image
from cv_bridge import CvBridge#bridge is used to get the image from opencv to ros

def main():

    rospy.init_node("edge_publisher_node")
    pub = rospy.Publisher("edge_image", Image, queue_size=10)#publisher is used 
    
    
    bridge = CvBridge()#the bridge thing mentioned earlier

    pipeline = dai.Pipeline()#pipeline is used 
    cam = pipeline.createColorCamera()
    cam.setPreviewSize(640, 480)
    cam.setBoardSocket(dai.CameraBoardSocket.RGB)
    cam.setInterleaved(False)


    xout = pipeline.createXLinkOut()
    xout.setStreamName("video")
    cam.preview.link(xout.input)


    with dai.Device(pipeline) as device:
    
        video = device.getOutputQueue(name="video")

        while not rospy.is_shutdown():
            frame = video.get().getCvFrame()
            edges = cv2.Canny(frame, 100, 200)
            msg = bridge.cv2_to_imgmsg(edges, encoding="mono8")
            pub.publish(msg)
            
            

if __name__ == "__main__":
    main()

