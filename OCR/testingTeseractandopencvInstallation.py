import pytesseract
import pkg_resources
import cv2

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program-Files\\Tesseract-OCR\\tesseract.exe' # change path if needed & use double backslashes
print(pkg_resources.working_set.by_key['pytesseract'].version)

print(cv2.__version__)
