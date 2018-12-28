import folium
import numpy as np
import geopandas as gpd
from geopandas import GeoDataFrame
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import pyproj


canada_cd = "C:/Users/Mahesh/Documents/GitHub/personal/src/canada_censusivision/gcd_000a11a_e.shp"
canada_pr = "C:/Users/Mahesh/Documents/GitHub/personal/src/canada_provinces/gpr_000a11a_e.shp"
#converting to a data fram
cd_df = gpd.read_file(canada_cd)
pr_df = gpd.read_file(canada_pr)

# setting the projection
cd_df = cd_df.to_crs({'init' : 'epsg:3347'})
pr_df = pr_df.to_crs({'init' : 'epsg:3347'})
cencusdivdf = pd.DataFrame(cd_df)

#Cooking
#1. Show unique name in the column name of the dataframe
print (cencusdivdf.PRNAME.unique())
#2. show the list of column names in the DF
print (cencusdivdf.columns)
#3 show the type of data, of the columns selected
# eg. DF.COLUMNNAME.dtype
print (cencusdivdf.geometry.dtype)
#4. using indexers or loc(using index to seperatly selected indexed rows)
#eg DF.loc[0] will give the first row in the DF
#   DF.loc[:] will give everything 
print (cencusdivdf.loc[0])

#5. create a new suset DF from an old DF
# query should be inside the loc parameters
# eg DF.loc[DF["COLUMNNAME"]==""], 
# so.. DF where the columnname has the term equal to "Ontario" 
newdf = cencusdivdf.loc[cencusdivdf["PRNAME"]=="Ontario"]
newdf_yukon = cencusdivdf.loc[cencusdivdf["PRNAME"]=="Yukon"]
mergeddataset = pd.concat([newdf,newdf_yukon])

#6. Make into a new Geodataframe so we can visualize it.
ontario = GeoDataFrame(newdf)
yukon = GeoDataFrame(newdf_yukon)
# Merging 2 dataframes so that we can 
merged_data = GeoDataFrame(mergeddataset) 


#statisticAL INFORMATION
#.7 print the length of the dataset
print (len(list(cd_df.CDNAME.values)))
#.8 print all values in column names
print (list(cd_df.CDNAME.values))

#ploting and showing
#.9 plot the DF
ontario.plot()
yukon.plot()
merged_data.plot()
#8. show the data frame
plt.show()




map_osm = folium.Map(location=[43.469781, -80.539380], zoom_start=20)
folium.Marker(location=[43.469781, -80.539380],popup ="DWG",icon= folium.Icon(color='green')).add_to(map_osm)



map_osm.save("C:/Users/Mahesh/Anaconda3/envs/MBET/map.html")