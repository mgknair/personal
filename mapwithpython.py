import folium
import numpy as np

map_osm = folium.Map(location=[43.469781, -80.539380], zoom_start=20)
folium.Marker(location=[43.469781, -80.539380],popup ="DWG",icon= folium.Icon(color='green')).add_to(map_osm)


map_osm.save("C:\Users\Mahesh\Anaconda2\envs\MBET/map.html")