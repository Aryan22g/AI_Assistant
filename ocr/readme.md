Introduction to OCR (Optical Character Recognition)
 - electronic conversion of images of handwritten or printed text into machine-encoded text
 2 types of text:
    1. structured text
    2. unstructured text
OCR has most accuracy when reading the structured text

Traditional OCR Techniques:
    Using traditional OCR: Eg. Tesseract
        uses RNN and LSTM
        works fine with structured text data, but performance is poor with handwritten text.

    Learning:
        take all characters in a language
        detect the edges of each letter, the ngles, etc.
        code this result this into an OCR program

    Recognizing:
        load the image to check, pre-process it.
        compare with the existing parameters.

Setting up environment:
libraries and dependencies: python, tesseract OCR, NumPy, OpenCV, Keras, Tensorflow.
1. Download Anaconda (python 3.7 version or above)

Tesseract OCR Setup:
    Link: https://github.com/UB-Mannheim/tesseract/wiki  (Download 64 bit)
    copy the installation destination folder path eg. C:\Program-Files\Tesseract
    instal python bindings:
        pip install tesseract
        pip install pytesseract

OpenCV Setup:
    pip install opencv-python

Install Pillow (can't pass BGR array into tesseract fn, so we use pillow to convert it to PIL image to pass into tesseract OCR)
    pip install pillow
