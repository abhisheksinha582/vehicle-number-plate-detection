import pytesseract
import os


def recognize_plate(plate):

	pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" #Enter your path where tesseract-ocr is installed

	curr_dir = os.getcwd()

	#Use tesseract to convert image into string
	text = pytesseract.image_to_string(cropped_img_loc, lang='eng')
	print("Number is : ", text)

	plate_number = open(curr_dir + "/plate_number.txt","w") 

	plate_number.write(text)
	plate_number.close()
