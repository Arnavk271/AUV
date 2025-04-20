#!/usr/bin/env python3

import depthai as dai #depth ai is imported
import cv2


def main():
   
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
        print("ENter e to exit the camera view...")

        while True:
            
            frame = video.get().getCvFrame()

            
            cv2.imshow("Camera View", frame)

            
            if cv2.waitKey(1) & 0xFF == ord('e'): #we use e to exit from the code / function
                break

    cv2.destroyAllWindows()



if __name__ == '__main__':
    main()

