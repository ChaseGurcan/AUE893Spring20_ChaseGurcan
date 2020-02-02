
import rospy
from geometry_msgs.msg import Twist

if __name__ == '__main__':
        rospy.init_node('circle')
	publisher = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size = 10)
	velocity = Twist()


	velocity.linear.x = 7
	velocity.linear.y = 0
        velocity.linear.z = 0
	 


	velocity.angular.x= 0
	velocity.angular.y = 0
	velocity.angular.z = 7


	while not rospy.is_shutdown():
	    publisher.publish(velocity)
