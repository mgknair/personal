import pandas as pd 

## The different variables and their index position ##
## 0.Time
## 1.Latitude
## 2.Longitude
## 3.Speed
## 4.Accuracy
## 5.Bearing
## 6.Label
## 7.X
## 8.Y
## 9.Z

cols = ['time', 'lat', 'lon', 'speed', 'accuracy', 'bearing', 'label', 'x', 'y', 'z']
df_cars = pd.read_csv('C:\Users\Mahesh\Anaconda2\envs\MBET\DATA/CARRO/AllCarro.csv', names=cols)
print(df_cars.shape)
# print(df_cars.describe)

Variables = np.array([TimeArrayNp, LatArrayNp, LonArrayNp, SpeedArrayNp, AccuracyArrayNp, BearingArrayNp, map(int,LabelArrayNp), XArrayNp, YArrayNp, ZArrayNp])
Variables = Variables.T

tempSpeed = np.empty()
SpeedExt = np.empty()
count = 0
for row in Variables:
	if count <= 100:
		temp.append(row[3])
		count+=1
	else:
		SpeedExt.append(np.mean(tempSpeed))
		count = 0
		tempSpeed = np.empty()
print(SpeedExt.shape)

meanSpeed = np.mean(Variables[:,3])
print(Variables[:,3])
avglist(newlist)



N = 100
x_featureExt = []
temp = []
count = 0
for row in df_cars:
	if count <= 100:
		temp.append(row['x'])
		count+=1
	else:
		x_mean = np.mean(temp)
		x_featureExt.append(x_mean)
		temp = []
		count = 0

print(x_featureExt.shape)
