#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32


def publisher():

    x = 2 #used because the question says multiple of 2
    
    rospy.init_node('publisher_node', anonymous=True)
    pub = rospy.Publisher('multiple_of_2', Int32, queue_size=10) #publisher
    rate = rospy.Rate(1) 
 
    while not rospy.is_shutdown():
        pub.publish(x)
        rospy.loginfo(f"Output: {x}")
        x = x + 2 #used for table of 2, 2,4,6,......
        rate.sleep()

if __name__ == '__main__':
    try:
        print("The output->")
        publisher()
    except rospy.ROSInterruptException:
        pass

