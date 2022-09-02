#!/usr/bin/env python
import rospy
from std_msgs.msg import String, Float32MultiArray # String, Float32Multiarray import
import roslib
roslib.load_manifest('cvbridge')
import sys
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

def callback(data): # gp
    #print("access callback_gp")
#   rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
#    rospy.loginfo("GP x,y %f %f", data[0],data[1])
   # print(type(data)) # 
    rospy.loginfo(data)
    print(type(data))
def callback2(data): #image
    #print("access callback2_image")
    bridge = CvBridge()
   # rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    try:
      cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)

    (rows,cols,channels) = cv_image.shape
    if cols > 60 and rows > 60 :
      cv2.circle(cv_image, (50,50), 10, 255)
    rospy.loginfo(cv_image)
    print(type(cv_image))

    cv2.imshow("Image window", cv_image)
    cv2.waitKey(3)

"""
    try:
      image_pub.publish(bridge.cv2_to_imgmsg(cv_image, encoding="passthrough"))
      print("4")
    except CvBridgeError as e:
      print(e)
"""
  
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)
    print("1")
    rospy.Subscriber("tobiichatter", Float32MultiArray, callback) # gp 
    rospy.Subscriber("IMAGE", Image, callback2) # image 
   # rospy.Subscriber("tobiichatter", Float32MultiArray, callback) # gp
#    rospy.Subscriber("tobiichatter", Float, callback) # gp
    print("2")
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
