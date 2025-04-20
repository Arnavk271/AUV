#!/usr/bin/env python

import rospy
from bot.msg import bot_position



def callback(msg):

    rospy.loginfo(f"Bot Position ->> (x, y, direction) = ({msg.x}, {msg.y}, {msg.direction})") #calling the function to give the result



def listener():
    rospy.init_node('bot_listener_node', anonymous=True)
    
    rospy.Subscriber('bot_position', bot_position, callback)#call of subscriber
    rospy.spin()
    
    
    

if __name__ == '__main__':
    try:
        listener()#call of listener
    except rospy.ROSInterruptException:
        pass

