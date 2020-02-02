#!/usr/b_in/env python
import rospy
import numpy as np
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
PI = 3.1515926535897



def move():
	#distance value and speed is defined here
	distance = 2
	speed = 0.2

	#Linear velocity is specified
	vel.linear.x = 0.2
	vel.linear.y = 0
	vel.linear.z = 0

	vel.angular.x = 0
	vel.angular.y = 0
	vel.angular.z = 0

	#Initializing the present distance to be 0
	current_distance = 0
	time0 = rospy.Time.now().to_sec()

	while(current_distance < distance):

		#Updating the present distance
		pub.publish(vel)
		time1 = rospy.Time.now().to_sec()
		current_distance = speed * (time1 - time0)
	vel.linear.x = 0
	pub.publish(vel)

def rotate():
	#Angle value set here
	angular_speed = 0.2
	angle = 90*PI/180

	#Velocity for rotation is specified
	vel.linear.x = 0
	vel.linear.y = 0
	vel.linear.z = 0

	vel.angular.x = 0
	vel.angular.y = 0
	vel.angular.z = angular_speed

	#Initializing the present angle to be 0
	current_angle = 0
	time0 = rospy.Time.now().to_sec()

	while(current_angle < angle):

		#Updating the present angle
		pub.publish(vel)
		time1 = rospy.Time.now().to_sec()
		current_angle = angular_speed * (time1 - time0)
	vel.angular.z = 0
	pub.publish(vel)


if __name__ == '__main__':

	rospy.init_node('square')
	pub = rospy.Publisher('/turtle1/cmd_vel' , Twist, queue_size = 10)
	vel = Twist()
	try:
		#Calling the function for four times for square trajectory
	    for i in range(4):
		move()
		rotate()

	except rospy.ROSInterruptExeception:
	    pass

