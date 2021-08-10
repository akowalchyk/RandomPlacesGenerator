
import requests
import random

from GoogleMapsAPIKey import get_my_key

types = [
"amusement_park",
"aquarium",
"art_gallery",
"bakery",
"bar",
"bicycle_store",
"book_store",
"bowling_alley",
"cafe",
"casino",
"clothing_store",
"gym",
"hindu_temple",
"mosque",
"movie_theater",
"museum",
"night_club",
"park",
"restaurant",
"shopping_mall",
"spa",
"stadium",
"store",
"synagogue",
"tourist_attraction",
"university",
"zoo"
]

def get_random_place(address, radius):
    API_KEY = get_my_key()

    geo_params = {
        'key': API_KEY,
        'address': address
    }

    geo_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
    response = requests.get(geo_url, params=geo_params).json()
    if response['status'] == 'OK':
        geo = response['results'][0]['geometry']
        lat = str(geo['location']['lat'])
        lng = str(geo['location']['lng'])
        coords = lat + "," + lng
        print(coords)

        while True:
            type = random.choice(types)
            print(type)
            loc_params = {
                'key': API_KEY,
                'location': coords,
                'radius': radius,
                'type': type
            }
            loc_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
            response = requests.get(loc_url, params=loc_params).json()
            print(len(response['results']))
            if len(response['results']) > 0:
                break
        json_place = random.choice(response['results'])
        name = json_place['name']
        return type, name

#get_random_place('Nome', '5000')






