import numpy as np 
import cv2
import imutils
import pytesseract
import os


def Detect_plate(image):


	save_dir = os.getcwd() + '/Cropped_Image_text'

	if not os.path.exists(save_dir):
		os.mkdir(save_dir)


	#resize the image- change width to 500
	image = imutils.resize(image, width=500)

	#Display the original image
	cv2.imshow('original image', image)
	cv2.waitKey(0)

	#RGB to GRAY scale conversion
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	cv2.imshow("1 - Grayscale Conversion", gray)
	cv2.imwrite(save_dir + '/gray' + '.png', gray)  #writing gray image
	cv2.waitKey(0)

	#Noise removal with iterative bilateral filter(removes noise while preserving edges)
	gray = cv2.bilateralFilter(gray, 11,17,17)
	cv2.imshow("2- Bilateral filter", gray)
	cv2.imwrite(save_dir + '/without_noise' + '.png', gray)  # writing image after removing the noise
	cv2.waitKey(0)

	#Find edges of grayscale image
	edged = cv2.Canny(gray, 170, 200)
	cv2.imshow("3 - canny edges", edged)
	cv2.imwrite(save_dir + '/edged' + '.png', edged) #writing edged image
	cv2.waitKey(0)

	#Find Conotours based on edges
	cnts, new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

	#create copy of original image to draw all contours
	img1 = image.copy()
	cv2.drawContours(img1, cnts, -1, (0,255,0), 3)
	cv2.imwrite(save_dir + '/contours' + '.png', img1) #writing image with contours
	cv2.imshow("4 - All contours", img1)
	cv2.waitKey(0)

	#Sort Contours based on their area keeping minimum required area as '40' (anything smaller than that will not be considered)
	cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:40]
	NumberPlateCnt = None #we currently have no  Number plate Contour

	#Top 40 Contours
	img2 = image.copy()
	cv2.drawContours(img2, cnts, -1, (0,255,0), 3)
	cv2.imshow("5 - Top 40 Contours", img2)
	cv2.imwrite(save_dir + '/top40contours' + '.png', img2)
	cv2.waitKey(0)

	# loop over our contours to find the best possible approximate contour of number plate
	count = 0

	for c in cnts:
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.02 * peri, True)

		if len(approx) == 4: # Select the Contour with 4 corners
			NumberPlateCnt = approx # This is our approx Number Plate Contour

			# Crop those contours and store it in Cropped Images folder
			x, y, w, h = cv2.boundingRect(c)
			new_img = image[y:y+h, x:x+w] # create new image
			cv2.imwrite(save_dir + '/plate' + '.png', new_img) # Store new image

			break



	# Drawing the selected contour on the original image
	cv2.drawContours(image, [NumberPlateCnt], -1, (0,255,0), 3)
	cv2.imshow("Final Image with Number Plate Detected", image)
	cv2.imwrite(save_dir + '/final' + '.png', image) #writing final image with number plate
	cv2.waitKey(0)

	cropped_img_loc = save_dir + "/plate.png"
	cv2.imshow("cropped Image ", cv2.imread(cropped_img_loc))
	cv2.waitKey(0) # Wait for user input before closing the image displayed

	return new_img




