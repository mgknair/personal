import folium
import numpy as np
import geopandas as gpd
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

#statisticAL INFORMATION
print (len(list(cd_df.CDNAME.values)))
print (list(cd_df.CDNAME.values))
cd_df.plot()
plt.show()

map_osm = folium.Map(location=[43.469781, -80.539380], zoom_start=20)
folium.Marker(location=[43.469781, -80.539380],popup ="DWG",icon= folium.Icon(color='green')).add_to(map_osm)



map_osm.save("C:/Users/Mahesh/Anaconda3/envs/MBET/map.html")