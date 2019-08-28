import pytesseract
import os


def Recognize_plate(plate):

	pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" #Enter your path where tesseract-ocr is installed

	curr_dir = os.getcwd()
	
	#converting the image of cropped plate to grayscale
	plate = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)
	
	#showing the grayscale image of plate, press 0 to continue when the image pops up...
	cv2.imshow('gray_plate', plate)
	cv2.waitKey(0)

	#Use tesseract to convert number in theimage into string by using its OCR Engine
	text = pytesseract.image_to_string(plate, lang='eng')
	print("Number is : ", text)
	
	#creating aand opening a text file to write the license plate number
	plate_number = open(curr_dir + "/plate_number.txt","w")
	
	#writing the license plate number into the text file.
	plate_number.write(text)
	
	#finally we need to close the text file.
	plate_number.close()
