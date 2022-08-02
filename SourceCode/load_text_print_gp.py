import cv2

f = open('C:/Users/SYOONI/Desktop/Aruco Marker 영상 & gp/gaze_point.txt','r')

cap = cv2.VideoCapture(r'C:/Users/SYOONI/Desktop/Aruco Marker 영상 & gp/ri5cbcj/segments/1/fullstream.mp4')
i=0
while(cap.isOpened()):
    
    line = f.readline()
    line.rstrip()
   
    if line.find('ts') >=0:
        continue
    ret,frame=cap.read()
    
    height,width=frame.shape[0:2]
    try:
        list_line = line.split()
        frame=cv2.circle(frame,(int(float(list_line[0])*width),int(float(list_line[1])*height)),10,(255,0,0),2)
        i+=1
        cv2.imshow('frame',frame)
    except(KeyError):
        i+=1
    if(cv2.waitKey(20)>0):
        break

f.close()
cap.release()
cv2.destroyAllWindows()
