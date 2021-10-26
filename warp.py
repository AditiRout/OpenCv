import cv2
import numpy as np

img=cv2.imread("6484438.jpg")
print(img.shape)
width,height=250,350
pts1=np.float32([[111,219],[287,188],[154,482],[352,440]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])#size we want
matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgOutput=cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("output",imgOutput)
cv2.waitKey()