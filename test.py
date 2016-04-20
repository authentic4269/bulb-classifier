import numpy as np
import cv2
 
cascades = ["classifier/cascade.xml"]
j = 0
while j < len(cascades):
	cascade = cv2.CascadeClassifier(cascades[j])
	i =180 
	while i < 200:
#		img = cv2.imread('test/t' + str(i) + '.png')
		img = cv2.imread('streetview_backgrounds/' + str(i) + '.png')
		
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		bulbs = cascade.detectMultiScale(gray,1.2,7) 
		
		for(x,y,w,h) in bulbs:
			cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

		cv2.imshow('img', img)
		cv2.waitKey(0)
		i = i + 1
	j = j + 1
