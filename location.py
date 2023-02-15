import os
import requests
from datetime import date
from pyproj import Geod


# TODO: Write comments


def iss_location():
    # Request ISS location from open-notify
    r = requests.get("http://api.open-notify.org/iss-now.json").json()
    iss_position = r["iss_position"]

    # Set latitude and logitude values
    lat = iss_position["latitude"]
    lng = iss_position["longitude"]

    # Get date from the timestamp
    timestamp = r["timestamp"]
    last_update = date.fromtimestamp(timestamp).isoformat()


    # Reverse geocode lookup
    url_reverse = "https://trueway-geocoding.p.rapidapi.com/ReverseGeocode"
    querystring = {"location": f"{lat}, {lng}", "language": "en"}
    headers = {
            "X-RapidAPI-Key": os.environ.get("RAPIDAPI_KEY"),
            "X-RapidAPI-Host": "trueway-geocoding.p.rapidapi.com"
        }

    responce = requests.request("GET", url_reverse, headers=headers, params=querystring).json()
    print(responce['results'])

     # url_forward = "https://trueway-geocoding.p.rapidapi.com/Geocode"
    # querystring = {'address': responce['results'][0]['address'], "language": "en"}
    # responce_two = requests.request("GET", url_forward, headers=headers, params=querystring).json()
    # print(responce_two)


    

    # geodesic = Geod(ellps="WGS84")
    #         fwd_azimuth, back_asimuth, distance = geodesic.inv(lats1=[float(lat)], lons1=[float(lng)], lats2=[float(responce_two["results"][0]["location"]["lat"])], lons2=[float(responce_two["results"][0]["location"]["lng"])])
    #         print(fwd_azimuth)