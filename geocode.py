#!/usr/bin/env python3

import httplib2
import json
import requests

def getGeocodeLocation(inputString):
    # Use Google Maps to convert a location into Latitute/Longitute coordinates
    # FORMAT: https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=API_KEY
    google_api_key = ""
    locationString = inputString.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'% (locationString, google_api_key))
    #h = httplib2.Http()
    print(url)
    #reply_str = h.request(url,'GET')[1]
    #print(reply_str)
    #result = json.loads(str(reply_str))
    result = requests.get(url).json()
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    return (latitude,longitude)

getGeocodeLocation("Tokyo, Japan")

print(getGeocodeLocation("Tokyo Japan"))
print(getGeocodeLocation("Jakarta Indonesia"))
print(getGeocodeLocation("Maputo Mozambique"))
print(getGeocodeLocation("Geneva Switzerland"))
print(getGeocodeLocation("Los Angeles California USA"))
