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



file = csv.reader(open("C:\Users\Mahesh\Anaconda2\envs\MBET\ceo.csv"))
#print file

websites = []
dates = []
for row in file:
	#row[0], row[8], row[13]
	websites.append(row[13])
	dates.append(row[8])

#print dates
d = 1
scraped =[]
for item in websites[1:]:
	print item
	r = requests.get(item)
	data = BeautifulSoup(r.text,'html5lib')
	#print item
	#print data
	print dates[d],"\n" ,"time = ", data.select('time')," \n\n",# "title = ",data.select('title'),"\n",data.select('meta'),'\n', data.select('date')
	d = d+1

#print data
#print data.find('div',{'id':'Class'})
#print data.get_text(dates[1])
#print data.select('title')
#print data.select('time')
print"\ndone\n"

