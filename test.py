import numpy as np
import cv2
 
cascade = cv2.CascadeClassifier('classifier/cascade.xml')
i = 4
while i < 16:
	img = cv2.imread('test/t' + str(i) + '.png')
	
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	bulbs = cascade.detectMultiScale(gray,1.05,7) 
	for(x,y,w,h) in bulbs:
		cv2.rectangle(img,(x-w,y-h),(x+w,y+h),(255,0,0),2)

	cv2.imshow('img', img)
	cv2.waitKey(0)
	i = i + 1
