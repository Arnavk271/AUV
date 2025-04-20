For the first question, we had to build a convo between two people, using a single rosnode and same rostopic.
Acc to the notes provided, we first import rospy and then and after importing string we start with the call back function which will helps us print the input message.
We then create a convo function, so that we can build up a lil conversation between the two. Using name we give the input of the user speaking, and we also define the publisher and subscriber.
We use rospy.sleep(n) so that there is a time lag of n sec
We take the input from the user as a message, if the message is heh then we exit from the speaking stage of user input.
Else we just print the thing in the form of Name: message....
The if_name == '_main_' thing is the default as provided in the notes.

Reference- session 1 of auv.

Problems faced- time management, deadline for submission was really close.
