from PIL import Image
import numpy as np
import textract
import pytesseract
from pytesseract import image_to_string
import requests, bs4
from bs4 import BeautifulSoup
import argparse
import cv2
import os
import csv

#########Convert PDF in JPG##########################

#####################################################


src_path = 'C:\Users\Mahesh\Anaconda2\envs\MBET'

img = Image.open('PHOTO.jpg')
#crop_img = img.crop((0,0,img.width,img.height))
img2 = cv2.imread('PHOTO.jpg')

ret,th = cv2.threshold(img2,127,255,cv2.THRESH_BINARY)
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

ret1,th1 = cv2.threshold(gray,127,250,cv2.THRESH_BINARY_INV)
ret1,th2 = cv2.threshold(gray,127,250,cv2.THRESH_TRUNC)
ret1,th3 = cv2.threshold(gray,127,250,cv2.THRESH_TOZERO)
ret1,th4 = cv2.threshold(gray,127,250,cv2.THRESH_TOZERO_INV)
ret1,th5 = cv2.threshold(gray,127,250,cv2.THRESH_BINARY)

#ret,th2 = cv2.adaptiveThreshold(img2,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
#ret,th3 = cv2.adaptiveThreshold(img2,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)



cv2.imwrite('bnw.jpg',gray)
cv2.waitKey(0)
cv2.imwrite('threshold_binary.png',th5)
cv2.imwrite('threshold_Trunc.png',th2)
cv2.imwrite('threshold_tozero.png',th3)
cv2.imwrite('threshold_tozeroinv.png',th4)
cv2.imwrite('threshold_Binaryinv.png',th1)

cv2.waitKey(0)
#crop_img.save("Capture.png")

img_path = th3
print img_path
 

def get_string(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    cv2.imwrite(src_path + "removed_noise.png", img)

    #  Apply threshold to get image with only black and white
    #img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Write the image after apply opencv to do some ...
    cv2.imwrite(src_path + "threshold_binary.png", img)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(src_path + "threshold_binary.png"))

    # Remove template file
    #os.remove(temp)

    return result

#print get_string("C:\Users\Mahesh\Anaconda2\envs\MBET/bnw.jpg")
#x = get_string("C:\Users\Mahesh\Anaconda2\envs\MBET/thres.png")
print get_string("C:\Users\Mahesh\Anaconda2\envs\MBET/threshold_binary.png")

#r = requests.get('http://www.google.com/search', params={'q':'"'+x+'"',"tbs":"li:1"})
#soup = BeautifulSoup(r.text,'lxml')
#print soup
#print soup.find('div',{'id':'resultStats'}).text