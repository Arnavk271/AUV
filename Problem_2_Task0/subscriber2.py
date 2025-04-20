#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32


def callback(msg):

    result = msg.data + 5
    
    rospy.loginfo(f"Received: {msg.data}, After *2,*10 we just add 5 to get: {result}")
    rospy.seleep(1)
    
    

def subscriber2():

    rospy.init_node('subscriber2_node', anonymous=True)
    
    rospy.Subscriber('multiplied_by_10', Int32, callback)
    
    rospy.spin()



if __name__ == '__main__':
    try:
        subscriber2()
    except rospy.ROSInterruptException:
        pass

