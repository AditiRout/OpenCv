import cv2
import numpy as np
def empty():
    pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
cv2.createTrackbar("Saturation Min","TrackBars",0,255,empty)
cv2.createTrackbar("Saturation Max","TrackBars",255,255,empty)
cv2.createTrackbar("var Min","TrackBars",0,255,empty)
cv2.createTrackbar("var Max","TrackBars",255,255,empty)

cam=cv2.VideoCapture(0)
cam.set(3,640)#width
cam.set(4,480)#height

while True:
    ret,frame=cam.read()
    if ret==True:
         imgHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
         h_min=cv2.getTrackbarPos("Hue Min","TrackBars")
         h_max=cv2.getTrackbarPos("Hue Max","TrackBars")
         s_min=cv2.getTrackbarPos("Saturation Min","TrackBars")
         s_max=cv2.getTrackbarPos("Saturation Max","TrackBars")
         v_min=cv2.getTrackbarPos("var Min","TrackBars")
         v_max=cv2.getTrackbarPos("var Max","TrackBars")
         print(h_min,h_max,s_max,s_min,v_max,v_min)
         lower=np.array([h_min,s_min,v_min])
         upper=np.array([h_max,s_max,v_max])
         mask=cv2.inRange(imgHSV,lower,upper)
         cv2.imshow("Main",frame)
         cv2.imshow("HSV",imgHSV)
         cv2.imshow("track",mask)
         if cv2.waitKey(1) & 0xFF==ord('q'):
             break
cam.release()
cv2.destroyAllWindows()