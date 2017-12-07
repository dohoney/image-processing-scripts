#!python3
import sys
import os
import cv2
import numpy

def filter(image_file, gray_value_upper_bound):
	img = cv2.imread(image_file, 0)
	ub = int(gray_value_upper_bound)
	assert ub>=0 and ub<=255, "invalid input gray_value_upper_bound: %d" % ub

	img[img > ub] = 255

	while True:
		cv2.imshow("Press 's' to save", img)
		keycode = cv2.waitKey(1) & 0xFF
		if keycode == ord('s'):
			cv2.imwrite('out.png', img)
			break
		elif keycode != 0xFF:
			break





if __name__ == '__main__':
	if len(sys.argv) != 3:
		print("Usage: [image_file] [gray_value_upper_bound]")
		print()
		exit()
	else:
		filter(sys.argv[1], sys.argv[2])

	