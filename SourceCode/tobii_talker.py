#!/usr/bin/env python
import roslib
roslib.load_manifest('cvbridge')
import sys
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

import cv2
import numpy as np
import time
import rospy
from std_msgs.msg import String, Float32MultiArray, MultiArrayDimension #String
from PIL import Image as IM
from tobiiglassesctrl import TobiiGlassesController



ipv4_address = "10.2.70.106"

tobiiglasses = TobiiGlassesController(ipv4_address, video_scene=True)

def tobii_talker():
      pub = rospy.Publisher('tobiichatter', Float32MultiArray, queue_size=1)
       #pub = rospy.Publisher('tobiichatter', Float32MultiArray, queue_size=1)   
      image_pub = rospy.Publisher('IMAGE',Image,queue_size = 10); 
      bridge = CvBridge()
      imgMsg = bridge.cv2_to_imgmsg(frame,"bgr8") # opencv image -> ros imgmsg 
      rospy.init_node('talker', anonymous=True)
      rate = rospy.Rate(100)
      tobiiglasses.start_streaming()
      time.sleep(3.0)
     
      while not rospy.is_shutdown():
               #tobii_gp = "Gaze Position: %s " % tobiiglasses.get_data()['gp']
               #rospy.loginfo(tobii_gp)
               #pub.publish(tobii_gp)
               msg = Float32MultiArray() # send for floating type - generate object
	       data = tobiiglasses.get_data()['gp']
	       data_gp = data.get('gp')  # dict type's data -> list type's gp
               rospy.loginfo('image send')
               msg.data = data_gp # data_gp : list type
               pub.publish(msg) # only gp send  #lsy #cuz, send FloatArray type
	       #pub.publish(data_gp) # only gp send  #lsy #cuz, String need to casting
	       #pub.publish(data_gp[0]) # eye's x-coordinate gp
               #pub.publish(data_gp[1]) # eye's y-coordinate gp
               
	       rospy.loginfo(data_gp) # data_gp is list type
	       #print(type(data))    # verify data's type : dict
	       #print(type(data_gp)) # verify data_gp's type : list
	       #print(type(data_gp[0])) # verify data_gp[0]'s type : float
               # if you want to send data for floating type -> access list's element
	       image_pub.publish(imgMsg) #lsy
               #cv_image = bridge.imgmsg_to_cv2(imgMsg, desired_encoding='passthrough')
       	       #cv2.imshow('IMG',cv_image)
               #time.sleep(2.0)
               rate.sleep()
      tobiiglasses.stop_streaming()
      tobiiglasses.close()


cap = cv2.VideoCapture("rtsp://%s:8554/live/scene" % ipv4_address)

# Check if camera opened successfully
if (cap.isOpened()== False):
  print("Error opening video stream or file")

tobiiglasses.start_streaming()
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
    height, width = frame.shape[:2]
    data_gp  = tobiiglasses.get_data()['gp']
    if data_gp['ts'] > 0:
        cv2.circle(frame,(int(data_gp['gp'][0]*width),int(data_gp['gp'][1]*height)), 60, (0,0,255), 6)
    # Display the resulting frame
    #cv2.imshow('Tobii Pro Glasses 2 - Live Scene',frame)
    tobii_talker()
    # Press Q on keyboard to  exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  # Break the loop
  else:
    break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
tobiiglasses.stop_streaming()
tobiiglasses.close()
