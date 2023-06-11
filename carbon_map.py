#carbon-map
import requests
import folium
import csv
from folium.plugins import HeatMap

def make_carbon_map(country: str):
    map_list = []
    if country.lower() == "canada":
        file = "canada_carbon.csv"
    else:
        file = "usa_carbon.csv"

    with open(file) as f:
        reader = csv.reader(f)
        for row in reader:
            state = row[0]
            carbon = row[1]

            # Define the URL for the Nominatim API
            url = "https://nominatim.openstreetmap.org/search"
            # Define the parameters for the API request
            params = {
                "q": state,
                "format": "json"
            }

            # Send the API request and get the response
            response = requests.get(url, params=params).json()

            # Extract the latitude and longitude from the response
            latitude = response[0]["lat"]
            longitude = response[0]["lon"]
            coordinates = (latitude, longitude)
            map_list.append((state, coordinates, carbon))

    my_map = folium.Map(location=[0, 0], zoom_start=12)

    latitude1 = []
    longitude1 = []
    carbon_emissions1 = []

    for entry in map_list:
        latitude_entry = float(entry[1][0])
        longitude_entry = float(entry[1][1])
        carbon_emissions_entry = float(entry[2])
    #    heat_data = [latitude, longitude, sentiment_score]
    #    print(heat_data)
        latitude1.append(latitude_entry)
        longitude1.append(longitude_entry)
        carbon_emissions1.append(carbon_emissions_entry)

    heat_data = list(zip(latitude1, longitude1, carbon_emissions1))

    HeatMap(heat_data).add_to(my_map)
    my_map.save(f'{country}_carbon_map.html')
