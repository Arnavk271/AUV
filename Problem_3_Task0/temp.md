We first create a custom message type called bot_pose.msg which contains:
    int32 x
    int32 y
    string direction

The publisher node allows the user to type commands like forward, left, right, etc..... Each command is published..
We use rospy.init_node() and proper loops or callbacks to keep the system running and responsive
The subscriber node listens and keeps track of the bot’s current state (x, y, and direction). Based on the command received, it updates the bot’s position and direction accordingly. It then publishes this updated position using the bot position custom message 
Inside the subscriber, we can define a direction and updating the bot’s state accordingly after each command. 
For example--->>
    If direction is north and command is forward → y increases by 1
The subscriber prints out the bot's current (x, y, direction) after each movement
We use rospy.sleep(n) so that there is a time lag of n sec
The if_name == '_main_' thing is the default as provided in the notes

problem faced- time management, and the logic used for this was needed. I had used ai to write the code, which converted my c code to python code to help me be effiecient.
