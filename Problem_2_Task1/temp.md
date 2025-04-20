We should take the camera image, detect the edge, and then send this image using ROS so that we can show it
We first create a rosnode and then a publisher who sends the image, then we use pipeline to use the cam and get edges, cv2Cannyframe is applied for the edge detection.
bridge is used to convert the opencv image to ros image, then we use pub.pulisher to send the image so that the subscriber can receive it 
so we build the connection bw publiisher and subscriber again..

sources---https://www.youtube.com/watch?v=6cXV8dhNu50 and the luxonis docs
had to use lil bit of ai for the functions such as cannyframe

problems- pipeline basics were not clear, so i had to watch lectures to understand. which was effective but then took a lot of time to solve and code.
i'll have to understand the opencv thing more properly and in depth.
