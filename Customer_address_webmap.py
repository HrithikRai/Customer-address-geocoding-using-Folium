import pandas as pd
import folium
from geopy.geocoders import ArcGIS
nom = ArcGIS()

df = pd.read_csv("supermarkets.csv")
df['location']=df.Address+','+df.City+','+df.State+','+df.Country

add= []
coordinates=[]
lat=[]
long=[]

for item in range(0,6):
    add.append(nom.geocode(df.location[item]))
    
for item in range(0,6):
    lat.append(add[item].latitude)
    
for item in range(0,6):
    long.append(add[item].longitude)


map = folium.Map(location=[37.756648011392286,37.757819005175406],zoom_start=6,tiles='Stamen Terrain')

fg = folium.FeatureGroup(name = 'My Map')
for item in range(0,6):
    fg.add_child(folium.Marker(location=[lat[item],long[item]],popup='location no- %s'%item,icon=folium.Icon(color='green')))
    map.add_child(fg)

map.save("customer_map.html")
