#map

## Geocoding

import folium
from folium.plugins import HeatMap
import requests
import csv
from textblob import TextBlob

def make_sentiment_map(country: str):
    tweety = {}

    if country.lower() == 'canada':
        file = 'climate_twitter_canada_new.csv'
    else:
        file = 'climate_twitter_usa_new.csv'

    with open(file, encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            tweet = row[0]
            place = row[1]

            # Define the URL for the Nominatim API
            url = "https://nominatim.openstreetmap.org/search"
            if place != '' and place != 'Earth':
                # Define the parameters for the API request
                params = {
                    "q": place,
                    "format": "json"
                }

                # Send the API request and get the response
                response = requests.get(url, params=params).json()

                # Extract the latitude and longitude from the response
                latitude = response[0]["lat"]
                longitude = response[0]["lon"]
                coordinates = (latitude, longitude)
                tweety[tweet] = coordinates

    ## Sentiment analysis

    map_list = []

    for tweet in tweety:
        analysis = TextBlob(tweet)
        sentiment_score = analysis.sentiment.polarity
        map_list.append((tweety[tweet], sentiment_score))

    ## Folium map + heatmap
    my_map = folium.Map(location=[0, 0], zoom_start=12)

    latitude1 = []
    longitude1 = []
    sentiment_score1 = []

    for entry in map_list:
        latitude_entry = float(entry[0][0])
        longitude_entry = float(entry[0][1])
        sentiment_score_entry = float(entry[1])
    #    heat_data = [latitude, longitude, sentiment_score]
    #    print(heat_data)
        latitude1.append(latitude_entry)
        longitude1.append(longitude_entry)
        sentiment_score1.append(sentiment_score_entry)

    heat_data = list(zip(latitude1, longitude1, sentiment_score1))

    HeatMap(heat_data).add_to(my_map)
    my_map.save(f'{country}_sentiment_map.html')
