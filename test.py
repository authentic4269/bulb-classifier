import numpy as np
import cv2
 
cascade = cv2.CascadeClassifier('classifier/cascade.xml')
img = cv2.imread('test/l1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
bulbs = cascade.detectMultiScale(gray, 1.3, 5)
for(x,y,w,h) in bulbs:
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('img', img)
cv2.waitKey(0)
