#Geospatial Analysis

import folium
from folium.plugins import HeatMap
from google.colab import drive
drive.mount('/content/drive')


# Initialize a map centered around the mean latitude and longitude
mean_lat = data['Latitude'].mean()
mean_lon = data['Longitude'].mean()
map_ = folium.Map(location=[mean_lat, mean_lon], zoom_start=2)

# Filter out rows with missing or invalid latitude/longitude values
data = data.dropna(subset=['Latitude', 'Longitude'])
data = data[(data['Latitude'].between(-90, 90)) & (data['Longitude'].between(-180, 180))]

# Add transaction locations to the map
heat_data = [[row['Latitude'], row['Longitude']] for index, row in data.iterrows()]
HeatMap(heat_data).add_to(map_)

# Save the map to an HTML file
map_.save('/content/drive/MyDrive/transaction_heatmap.html')
map_