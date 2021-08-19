
import requests
import random
import time

from GoogleMapsAPIKey import get_my_key

types = [
"amusement_park",
"aquarium",
"art_gallery",
"bakery",
"bar",
"bowling_alley",
"cafe",
"casino",
"clothing_store",
"movie_theater",
"museum",
"night_club",
"park",
"restaurant",
"shopping_mall",
"spa",
"tourist_attraction",
"university",
"zoo"
]

def get_random_place(address, radius):
    API_KEY = get_my_key()
    print(API_KEY)

    # grabbing coordinates
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

        # generating random place
        timeout = time.time() + 10
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
            if time.time() > timeout:
                return "https://www.mlb.com/mariners/ballpark", "No Response", "No Response", "Please Enter a valid input. Here's my fav place."
        json_place = random.choice(response['results'])
        place_id = json_place['place_id']

        #generating place details from ID
        det_params = {
                'key': API_KEY,
                'place_id': place_id,
                'language' : "en"
            }
        det_url = "https://maps.googleapis.com/maps/api/place/details/json?"
        response = requests.get(det_url, params=det_params).json()

        #grabbing google url
        google_url = response['result']['url']
        #print(response['result'])

        #grabbing photo or icon url
        photo_ref = ""
        if 'photos' in response['result']:
            photo = response['result']['photos'][0]['photo_reference']
            photo_ref = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=" + photo + "&key=" + get_my_key()
        else:
            photo_ref = response['result']['icon']
        print(photo_ref)

        #grabbing name
        name = response['result']['name']
        return google_url, photo_ref, name, type






