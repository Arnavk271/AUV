#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32


def callback(msg):

    val = msg.data * 10
    
    rospy.loginfo(f"Received-> {msg.data}, After multiplying by 10-> {val}")
    pub.publish(val)
    rospy.sleep(1)


def subscriber1():

    rospy.init_node('subscriber1_node', anonymous=True)
    
    rospy.Subscriber('multiple_of_2', Int32, callback)
    
    global pub
    pub = rospy.Publisher('multiplied_by_10', Int32, queue_size=10)

    rospy.spin()
    
    

if __name__ == '__main__':
    try:
        subscriber1()
    except rospy.ROSInterruptException:
        pass

