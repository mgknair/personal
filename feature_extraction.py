import os
import numpy as np
import matplotlib
import csv
import time
from sklearn import preprocessing, cross_validation, neighbors, svm, tree 
from sklearn.model_selection import train_test_split
from sklearn.datasets import samples_generator
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.pipeline import Pipeline
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.naive_bayes import GaussianNB
import argparse
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
import pandas as pd


########## Read the file to be compressed

def removedot(a):
	final =[]
	for lst in a:
		final.append(lst)
		countofa = 0
		for i in lst:
			if countofa >= 2:
				break
			countofa = 0
			for element in i:
				if element == ".":
					countofa += 1
				if countofa >= 2:
					final = final[:-1]
					break
	return final


f =removedot(csv.reader(open('C:\Users\Mahesh\Anaconda2\envs\MBET\DATA/CARRO/AllCarro.csv')))

##Global N###

n = 100

#variance = np.var(F, dtype=np.float64)
def variance(x):
	np.var(x,dtype=np.float64)
#print "the variance is " + str(variance)
#print "The Max is " + str(max(F))
#print "The min is " + str(min(F))

#Average =  sum(F)/float(len(F))
def average(x):
	sum(x)/float(len(x))
#print "the average is " + str(Average)

#Gradient = np.gradient(F)
def gradient(x):
	return np.gradient(x)
#print "The gradient is " + str(Gradient)

#Minlist =[min(F) for i in range(0,len(F),n)] 
def minlist(x):
	output = []
	index = 0
	while index != len(x):
		if index % n != 0:
			output.append(min(x[index:len(x)]))
			#print output
		if x[index:index+n] == []:
			#print output
			return output
		step1 = min(x[index:index+n])
		output.append(step1)
		index = index + n
	return output
	#return [min(x) for i in range(0,len(x),n)] 

def avglist(x):
	output = []
	index = 0
	while index <= len(x):
		if index % n != 0:
			output.append(sum(x[index:len(x)])/len(x[index:index+n]))
			#print output
		if x[index:index+n] == []:
			#print output
			return output
		step1 = sum(x[index:index+n])/len(x[index:index+n])
		output.append(step1)
		index = index + n
	return output



newlist = [286.27, 213.41, 111.8, 82.52, 196.74, 190.39, 189.79, 191.51, 182.65, 219.53, 214.35, 211.78, 201.61, 244.0, 291.29, 145.55, 296.62, 228.25, 267.21, 296.04, 291.16, 226.89, 0.0, 77.88, 283.71, 275.7, 216.17, 221.92, 197.33, 170.63, 174.03, 171.74, 114.41, 163.06, 175.05, 185.92, 185.39, 91.72, 164.72, 135.13, 184.14, 189.46, 214.81, 232.88, 203.02, 240.94, 241.15, 242.15, 241.54, 242.56, 242.6, 245.65, 155.69, 255.29, 265.79, 273.31, 273.52, 205.07, 172.2, 0.0, 0.0, 270.34, 17.03, 146.71, 33.97, 11.916666666666666]


def variancelist(x):
	output = []
	index = 0
	while index != len(x):
		if index % n != 0:
			output.append(np.var(x[index:len(x)]))
			#print output
		if x[index:index+n] == []:
			#print output
			return output
		step1 = np.var(x[index:index+n])
		output.append(step1)
		index = index + n
	return output

#Maxlist = [max(F) for i in range(0,len(F),n)]
def maxlist(x):
	output = []
	index = 0
	while index <= len(x):
		if index % n != 0:
			output.append(max(x[index:len(x)]))
		if x[index:index+n] == []:
			#print output
			return output
		step1 = max(x[index:index+n])
		output.append(step1)
		index = index + n
	return output
	#return [max(x) for i in range(0,len(x),n)]


###############################################################

TimeArray = []
LatArray = []
LonArray = []
speedArray =[]
accuracyArray=[]
bearingArray=[]
labelArray = []
XArray =[]
YArray =[]
ZArray =[]
# Add more feature if you want

for row in f:
	#row = row[0:10]
	if len(row) == 10:
		TimeArray.append(float(row[0])) 
		LatArray.append(float(row[1]))
		LonArray.append(float(row[2]))
		speedArray.append(float(row[3]))
		accuracyArray.append(float(row[4]))
		bearingArray.append(float(row[5]))
		labelArray.append(row[6])
		XArray.append(float(row[7]))
		YArray.append(float(row[8]))
		ZArray.append(float(row[9]))
	else:
		pass



cols = ['time', 'lat', 'lon', 'speed', 'accuracy', 'bearing', 'label', 'x', 'y', 'z']
df_cars = pd.read_csv('C:\Users\Mahesh\Anaconda2\envs\MBET\DATA/CARRO/AllCarro.csv', names=cols)
print(df_cars.shape)

TimeArrayNp = np.array(TimeArray)
LatArrayNp = np.array(LatArray)
LonArrayNp = np.array(LonArray)
SpeedArrayNp = np.array(speedArray)
AccuracyArrayNp = np.array(accuracyArray)
BearingArrayNp = np.array(bearingArray)
LabelArrayNp = np.array(labelArray)
XArrayNp = np.array(XArray)
YArrayNp = np.array(YArray)
ZArrayNp = np.array(ZArray)
# print timeArrayNp.shape

##### avergares
TimeArrayAVG = np.array(avglist(TimeArray))
LatArrayAVG = np.array(avglist(LatArray))
LonArrayAVG = np.array(avglist(LonArray))
SpeedArrayAVG = np.array(avglist(speedArray))
AccuracyArrayAVG = np.array(avglist(accuracyArray))
BearingArrayAVG = np.array(avglist(bearingArray))
LabelArrayAVG = np.array(avglist(map(int,labelArray)))
XArrayAVG = np.array(avglist(XArray))
YArrayAVG = np.array(avglist(YArray))
ZArrayAVG = np.array(avglist(ZArray))



##### maxes
TimeArrayMAX = np.array(maxlist(TimeArray))
LatArrayMAX = np.array(maxlist(LatArray))
LonArrayMAX = np.array(maxlist(LonArray))
SpeedArrayMAX = np.array(maxlist(speedArray))
AccuracyArrayMAX = np.array(maxlist(accuracyArray))
BearingArrayMAX = np.array(maxlist(bearingArray))
LabelArrayMAX = np.array(maxlist(map(int,labelArray)))
XArrayMAX = np.array(maxlist(XArray))
YArrayMAX = np.array(maxlist(YArray))
ZArrayMAX = np.array(maxlist(ZArray))


##### mins
TimeArrayMIN = np.array(minlist(TimeArray))
LatArrayMIN = np.array(minlist(LatArray))
LonArrayMIN = np.array(minlist(LonArray))
SpeedArrayMIN = np.array(minlist(speedArray))
AccuracyArrayMIN = np.array(minlist(accuracyArray))
BearingArrayMIN = np.array(minlist(bearingArray))
LabelArrayMIN = np.array(minlist(map(int,labelArray)))
XArrayMIN = np.array(minlist(XArray))
YArrayMIN = np.array(minlist(YArray))
ZArrayMIN = np.array(minlist(ZArray))

# Variables = np.array([TimeArray, LatArray, LonArray, speedArray, accuracyArray, bearingArray, map(int,labelArray), XArray, YArray, ZArray])
Variables = np.array([TimeArrayNp, LatArrayNp, LonArrayNp, SpeedArrayNp, AccuracyArrayNp, BearingArrayNp, map(int,LabelArrayNp), XArrayNp, YArrayNp, ZArrayNp])
VariablesT = Variables.T

Topline = np.array([TimeArrayMIN, TimeArrayMAX, TimeArrayAVG, 
			LatArrayMIN, LatArrayMAX, LatArrayAVG, 
			LonArrayMIN, LonArrayMAX, LonArrayAVG, 
			SpeedArrayMIN, SpeedArrayMAX, SpeedArrayAVG, 
			AccuracyArrayMIN, AccuracyArrayMAX, AccuracyArrayAVG, 
			BearingArrayMIN, BearingArrayMAX, BearingArrayAVG, 
			LabelArrayMIN, LabelArrayMAX, LabelArrayAVG, 
			XArrayMIN, XArrayMAX, XArrayAVG, 
			YArrayMIN,YArrayMAX, YArrayAVG, 
			ZArrayMIN, ZArrayMAX, ZArrayAVG])


print "topline shape is", Topline.shape

ToplineT = Topline.T

print "toplinet shape is", ToplineT.shape

print ToplineT[1]

#processLst = [maxlist, minlist, avglist]
###############################################################################
#print(Variables.shape)
#print(VariablesT.shape)

# Feature Extraction


#### Writing on a Excel file### 
csvf = open("C:\Users\Mahesh\Anaconda2\envs\MBET/newfile.csv","wb")
wr = csv.writer(csvf,dialect='excel')
for i in ToplineT:
	wr.writerow(i)

	
###############################################################
y1 =np.array(map(float,[1,2,3,4,5,1,2,3,4,5]))
y2 =np.array(map(float,[1,2,3,2,5,1,2,3,4,5]))

correct = y1 == y2
print correct.sum()
length = len(correct)
print length
accuracy = correct.sum() / float(length)
print accuracy
