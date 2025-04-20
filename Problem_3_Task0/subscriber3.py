#!/usr/bin/env python

import rospy
from bot.msg import bot_position



def callback(msg):

    rospy.loginfo(f"Bot Position ->> (x, y, direction) = ({msg.x}, {msg.y}, {msg.direction})")



def listener():
    rospy.init_node('bot_listener_node', anonymous=True)
    
    rospy.Subscriber('bot_position', bot_position, callback)
    rospy.spin()
    
    
    

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass

