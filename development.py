#import pymysql

#con = pymysql.connect(host='209.172.51.58',user='webahn_owner', password='BB3we5@baN3hn', db='webahn_database')

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
from selenium import webdriver


# Using Chrome to access web
file = csv.reader(open("C:\Users\Mahesh\Anaconda2\envs\MBET\GCS.csv"))
#file = open("C:\Users\Mahesh\Anaconda2\envs\MBET\GCS.csv")




CPW = requests.get("https://www.canadapost.ca/cpo/mc/personal/postalcode/fpc.jsf")
print CPW
data = BeautifulSoup(CPW.text,'html5lib')
data.prettify()

search =  data.find('input')
data.select('input[name=addressComplete]')


print data.find('addressContainer')
Address = []
City = []
pcode = []
for row in file:
	Address.append(row[0])
	City.append(row[1])

counter = 0
driver = webdriver.Chrome("C:\Users\Mahesh\Downloads\chromedriver_win32\chromedriver.exe")
r = driver.get("https://www.canadapost.ca/cpo/mc/personal/postalcode/fpc.jsf")
id_box = driver.find_element_by_id('addressComplete')
for i in Address[:len(Address)]:
	leni = len(i)
	id_box.send_keys(str(i)+", Montreal QC")
	search_button = driver.find_element_by_id('searchFpc')
	search_button.click()
	search_button.click()
	search_button.click()
	search_button.click()
	search_button.click()
	search_button.click()
	search_button.click()
	search_button.click()
	search_button.click()
	search_button.click()
	search_button.click()
	
	postalcodeC = driver.find_element_by_id("addressContainer").text
	#print postalcodeC
	postalcode = driver.find_element_by_id("printLabelContent").text
	pcode.append(postalcode[-7:])
	id_box.clear()
	counter =counter+1
	print counter

print pcode

myfile = open("C:\Users\Mahesh\Anaconda2\envs\MBET\GCS1.csv", "w")
readerf = csv.reader(file)

count=0


with myfile:
	writer= csv.writer(myfile)
	for i in pcode:
		writer.writerow([Address[count],City[count],i])
		count= count +1

# for row in file:
# 	print row
# 	row.append(pcode[count])
# 	print row
# 	count = count + 1

