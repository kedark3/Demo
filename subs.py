#!/usr/bin/env python

import rospy
from std_msgs.msg import String
def callback_receive_radio_data(msg):
    # rospy.loginfo("rxed")
    rospy.loginfo(msg)

if __name__ =='__main__':
    rospy.init_node('mylistener')
    sub=rospy.Subscriber('/topic',String,callback_receive_radio_data)
    ###callback_fun is to tell subs wat to do wen the msg is rx
    rospy.spin() ###keep on repeating the action,like subscribing 
    ##in a loop