#!/usr/bin/env python
import rospy
import sys
import cv2
import pdb
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

def start_node():
    rospy.init_node('image_pub')
    rospy.loginfo('image_pub node started')

    filename = './src/detect_pump/nodes/pump.png'
    img = cv2.imread(filename)
    # cv2.imshow("image",img)
    # cv2.waitKey(2000)

    #Add a call to the CvBridge "cv2_to_imgmsg" method
    bridge = CvBridge()
    imgMsg = bridge.cv2_to_imgmsg(img,"bgr8")

    #Create ROS publisher to 
    pub = rospy.Publisher('IMAGE', Image, queue_size=10) 
    #'IMAGE' is the topic name
    #Image is the topic type
    while not rospy.is_shutdown():
    	pub.publish(imgMsg)
    	rospy.Rate(1.0).sleep() #1 Hz. 1 topic/second


if __name__=='__main__':
    try:
    	start_node()
    	# start_node(rospy.myargv(argv=sys.argv)[1])
    except rospy.ROSInterruptException:
        pass
