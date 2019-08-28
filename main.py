import cv2
import imutils
import numpy as np 
import os
import detect_plate
import recognize_plate


def Main(image_name):
	
	image = cv2.imread(image_name)

	plate = detect_plate.Detect_plate(image)

	recognize_plate.Recognize_plate(plate)


if __name__ == '__main__':

	print("please make sure the image is in the same folder in which the file main.py is\n")

	image_name = input("enter image name with extension: ")

	Main(image_name)

	
