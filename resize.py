from os import listdir, remove
import cv2

directory = "./streetview_backgrounds/"
files = listdir(directory)
i = 1
for f in files:
	infile = cv2.imread(directory + f)
	cropped = infile[0:420, 0:1100]
	cv2.imshow("cropped", cropped)
	cv2.imwrite(directory + str(i) + ".png", cropped)
	i = i + 1
