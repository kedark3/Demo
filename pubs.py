#!/usr/bin/env python

import rospy
from std_msgs.msg import String
if  __name__ =="__main__":
    rospy.init_node("pubs_node",anonymous=True)
    pub=rospy.Publisher('topic',String,queue_size=10)##name of the topic and type of the topic 
    ##q_siz is just to control the amt of messages it sends before waiting (something of this sorT),not
    ##to overcrowd the subrscriber
    rate=rospy.Rate(2)
    while not rospy.is_shutdown():
        msg=String()##type of the msg to be pubs on ros topic
        msg.data='hi this is topic demo' ##the msg
        pub.publish(msg) #publishing the msg
        rate.sleep()
    rospy.loginfo("killed node")

