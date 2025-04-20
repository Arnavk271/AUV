#!/usr/bin/env python

import rospy
from bot.msg import bot_position



def move_bot():
    rospy.init_node('bot_publisher_node', anonymous=True)
    pub = rospy.Publisher('bot_position', bot_position, queue_size=10) #use of publisher
    rate = rospy.Rate(1)  

    x= 0 #we define and assign some random values initially 
    y= 0
    direction = "up"

    while not rospy.is_shutdown():
        command = raw_input("Enter command 1.forward 2.left 3.right: ").lower()

#logic->
        if command == 'forward':
           if direction == "right":
                x = x+1
            elif direction == "left":
                x = x-1
            elif direction == "down":
                y = y-1
            elif direction == "up":
                y = y+1
                
                
                
       elif command == 'turn right':
            if direction == "up":
                direction = "right"
            elif direction == "right":
                direction = "down"
            elif direction == "down":
                direction = "left"
            elif direction == "left":
                direction = "up"




        elif command == 'turn left':
            if direction == "up":
                direction = "left"
            elif direction == "left":
                direction = "down"
            elif direction == "down":
                direction = "right"
            elif direction == "right":
                direction = "up"

        

        else:
            print("Unknown command, try again.")
            continue

#assigning the new position after updation
        position = bot_position()
        position.x = x
        position.y = y
        position.direction = direction
        
        
        pub.publish(position)
        rospy.loginfo(f"Bot Position: x={x}, y={y}, direction={direction}")

        rate.sleep()
        
        

if __name__ == '__main__':
    try:
        move_bot()
    except rospy.ROSInterruptException:
        pass

