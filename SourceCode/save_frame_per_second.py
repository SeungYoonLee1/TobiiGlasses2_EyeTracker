import cv2
import numpy as np
import time
import rospy
from std_msgs.msg import String


if hasattr(__builtins__, 'raw_input'):
      input=raw_input

from tobiiglassesctrl import TobiiGlassesController

#----------------------------------------------------------------------#
"""
class image_converter:

  def __init__(self):
    self.image_pub = rospy.Publisher("image_topic_2",Image)

    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("image_topic",Image,self.callback)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)

    (rows,cols,channels) = cv_image.shape
    if cols > 60 and rows > 60 :
      cv2.circle(cv_image, (50,50), 10, 255)

    cv2.imshow("Image window", cv_image)
    cv2.waitKey(3)

    try:
      self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
    except CvBridgeError as e:
      print(e)
"""
#------------------------------------------------------------------------#

def tobii_talker():
      pub = rospy.Publisher('tobiichatter', String, queue_size=10)
      rospy.init_node('talker', anonymous=True)
      rate = rospy.Rate(100)
      tobiiglasses = TobiiGlassesController("10.2.70.109")
      tobiiglasses.start_streaming()
      time.sleep(3.0)
      while not rospy.is_shutdown():
               tobii_gp = "Gaze Position: %s " % tobiiglasses.get_data()['gp']
               rospy.loginfo(tobii_gp)
               pub.publish(tobii_gp)
               rate.sleep()
      tobiiglasses.stop_streaming()
      tobiiglasses.close()

ipv4_address = "10.2.70.109"

tobiiglasses = TobiiGlassesController(ipv4_address, video_scene=True)

project_id = tobiiglasses.create_project("Test live_scene_and_gaze.py")

participant_id = tobiiglasses.create_participant(project_id, "participant_test")

calibration_id = tobiiglasses.create_calibration(project_id, participant_id)

input("Put the calibration marker in front of the user, then press enter to calibrate")
tobiiglasses.start_calibration(calibration_id)

res = tobiiglasses.wait_until_calibration_is_done(calibration_id)


if res is False:
	print("Calibration failed!")
	exit(1)


cap = cv2.VideoCapture("rtsp://%s:8554/live/scene" % ipv4_address)

# Check if camera opened successfully
if (cap.isOpened()== False):
  print("Error opening video stream or file")

# Read until video is completed
tobiiglasses.start_streaming()
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
# --------------------------------------  
  #ic = image_converter()
  #rospy.init_node('image_converter', anonymous=True)
  #rospy.spin()
#-------------------------------
  hms = time.ctime().split(' ')[-2]
  hms2 = hms.split(':')
  h = hms2[0]
  m = hms2[1]
  s = hms2[2]
  cv2.imwrite("camera_images/{}-{}-{}.jpg".format(h,m,s), frame)
  
#-------------------------------
  if ret == True:
    height, width = frame.shape[:2]
    data_gp  = tobiiglasses.get_data()['gp']
    if data_gp['ts'] > 0:
        cv2.circle(frame,(int(data_gp['gp'][0]*width),int(data_gp['gp'][1]*height)), 60, (0,0,255), 5)

    # Display the resulting frame
    cv2.imshow('Tobii Pro Glasses 2 - Live Scene',frame)
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
