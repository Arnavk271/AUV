#!/usr/bin/env python3

import rospy
import depthai as dai


import cv2


from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def main():

    rospy.init_node("edge_publisher_node")
    pub = rospy.Publisher("edge_image", Image, queue_size=10)
    
    
    bridge = CvBridge()

    pipeline = dai.Pipeline()
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

