from PIL import Image
import pytesseract
import cv2

#declare the tesseract executable path
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program-Files\\Tesseract-OCR\\tesseract.exe' # change path if needed & use 

image_to_ocr = cv2.imread('images/testing/fox_sample2.png')

#preprocess step 1: convert to gray
preprocessed_img = cv2.cvtColor(image_to_ocr,cv2.COLOR_BGR2GRAY)
#preprocess step 2: do binary and Otsu thresholding
preprocessed_img = cv2.threshold(preprocessed_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# preprocessed_img = cv2.threshold(preprocessed_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1] -- if any error occured with above line use this.
#preprocess step 3: median blur to remove noise in the image
preprocessed_img = cv2.medianBlur(preprocessed_img)

# save image to convert to PIL image
cv2.imwrite("temp_img.jpg", preprocessed_img)

# load image as PIL/Pillow image
preprocessed_pil_img = Image.open('temp_img.jpg')

#do ocr using tesseract
text_extracted = pytesseract.image_to_string(Image.open('temp_img.jpg'))

print(text_extracted)

#display the original image
cv2.imshow('Video',image_to_ocr)
