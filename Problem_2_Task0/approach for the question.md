We start by creating a publisher node that continuously sends multiples of 2 starting from 2. This node uses rospy.Publisher to publish numbers on a topic.
We pass messages using standard Int16/Int32 (anything might work) message type.
Then, we make a first subscriber node that listens, receives the number, multiplies it by 10, and publishes this result to a new subscriber. Inside the callback function, we take the incoming number, multiply it by 10, and publish the result.
The second subscriber node listens, takes the number, adds 5 to it, and simply prints it. FOr example- if x=2 then 2 *10 +5 = 25...etc
We use rospy.sleep(n) so that there is a time lag of n sec
The if_name == '_main_' thing is the default as provided in the notes.

Reference- session 1 of auv.

Problems faced- time management, deadline for submission was really close
