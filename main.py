import cv2
import imutils
import numpy as np 
import os
import detect_plate
import recognize_plate


def Main(file_path, image_name):
	
	full_path = file+path +"/"+ image_name

	plate = detect_plate.Detect_plate(full_path)

	recognize_plate.Recognize_plate(plate)


if __name__ == '__main__':

	path = input("enter path of the image")

	image_name = input("enter image name with extension")

	Main(file_path, image_name)

	