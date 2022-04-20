#!/usr/bin/env python3


import rospy
from geometry_msgs import Twist
from turtlesim.msg import Pose

def pose_callback(msg:Pose):
    pass

if (__name__=='__main__'):
    rospy.init_node('Team Abhiyaan')
    rospy.loginfo("Node started")
    pub=rospy.Publisher('',Twist,queue_size=20)
    sub=rospy.Subscriber('',Pose,callback=pose_callback)
    rospy.loginfo("Team Abhiyaan rocks:")

    rospy.spin()

