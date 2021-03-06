#!/usr/bin/env python3

#SPDX-License-Identifer: BSD-2
#*Copyright (c) 2021 Ryuichi Ueda. All rights resrved.


import rospy
from std_msgs.msg import Int32

n = 0

def cd(message):
    global n
    n = message.data*2

if __name__ == '__main__':
    rospy.init_node('twice')
    sub = rospy.Subscriber('count_up', Int32, cd)
    pub = rospy.Publisher('twice', Int32, queue_size=1)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish(n)
        rate.sleep()
