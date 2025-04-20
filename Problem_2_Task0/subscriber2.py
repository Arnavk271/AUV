#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32


def callback(msg):

    result = msg.data + 5 # we use this to add 5 as mention in the question
    
    rospy.loginfo(f"Received: {msg.data}, After *2,*10 we just add 5 to get: {result}") #we take multiple of 2 and then multiply by 10 and at the end add 5
    rospy.seleep(1)
    
    

def subscriber2():

    rospy.init_node('subscriber2_node', anonymous=True)#subscriber2 calls subscriber1 and then it functions
    
    rospy.Subscriber('multiplied_by_10', Int32, callback)
    
    rospy.spin()



if __name__ == '__main__':
    try:
        subscriber2() #calling subscriber2
    except rospy.ROSInterruptException:
        pass

