import requests
import random

from GoogleMapsAPIKey import get_my_key

API_KEY = get_my_key()
det_params = {
                'key': API_KEY,
                'place_id': "Aap_uEDA-GB3efZvHfDiEbNSNcgxdll_ceflxzCigJIctywwcjdWIQgpNZw9LWY4ycMKAt5TXxdBpUcFa9u0C8yv-0Lrf8F71I11evTtZoPRFGowyylLRxX6gKmel8zD3zEEYYr1pR17B4V4guQ53TaRWK8gux6tUfMvcPTRJBOvHuFOGJqi",
                'maxheight': '400',
                'maxwidth': '400'
            }

det_url = "https://maps.googleapis.com/maps/api/place/photo?"
response = requests.get(det_url, params=det_params)
print(response)

https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=Aap_uEB3QlyPbWPDh7789fgwrhdqddFEbqsDtdeHGWke15-EYNP-6tPccZR7a_0a5Bw2FY0vM9DYdvuraBkPr26SLTSzTfQSbkJ-xEMm2k0pJMA-92EvvOwirCw0Qjpb7Y0Ai5-2EyZb2fECZn_JfNRQOHIl0yRX2SuQaSTpJmATEgB5W2Tt&key=AIzaSyBDECDTqdmc5LUcCE2jZ6hhZe6eLMBd4Ys