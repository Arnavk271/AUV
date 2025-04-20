#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(msg):
    print("\n" + msg.data)
    
    
    

def convo():
    rospy.init_node('convo_node', anonymous=True)
    
    name = raw_input("Enter your name: ") #to give input name

    pub = rospy.Publisher('convo_topic', String, queue_size=10) # the publisher use
    rospy.Subscriber('convo_topic', String, callback) #the subscriber use

    rospy.sleep(1)  #sleeps for 1 sec acc to notes

    print("Enter the message or type heh to exit....")

    while not rospy.is_shutdown():
        msg = raw_input("You: ")

        if msg.lower() == 'heh': #to quit the convo
            print("Exiting chat...")
            break

        result = f"{name}: {msg}"
        pub.publish(result)
        print("Message is sent, wohoo")




if __name__ == '__main__':
    try:
        convo()
    except rospy.ROSInterruptException:
        pass

