import os
import requests
import time
from datetime import date


def iss_location() -> list[str]:
    # Request ISS location from open-notify
    try:
        r = requests.get("http://api.open-notify.org/iss-now.json").json()

        iss_position = r["iss_position"]

        # Set latitude and logitude values
        lat = iss_position["latitude"]
        lng = iss_position["longitude"]
        # print(lat, lng, sep=", ")

        # Get date from the timestamp
        timestamp = r["timestamp"]
        timestamp = time.ctime(timestamp)[4:-8]
        # last_update = date.fromtimestamp(timestamp).isoformat()

    except requests.exceptions.RequestException as err:
        raise err

    # Attempt to find nearby toponym
    try:
        url_nearby = "http://api.geonames.org/findNearbyJSON"
        querystring_geonames = {
            "lat": {lat},
            "lng": {lng},
            "username": os.environ.get("GEONAMES_USERNAME"),
        }

        responce_geonames = requests.request(
            "GET", url_nearby, params=querystring_geonames
        ).json()

        if len(responce_geonames["geonames"]) >= 1:
            return [responce_geonames["geonames"][0]["adminName1"], timestamp]

    except requests.exceptions.RequestException as err:
        raise err

    # If toponyn not found assume in ocean and find what ocean
    if len(responce_geonames["geonames"]) == 0:
        try:
            url_ocean = "http://api.geonames.org/oceanJSON"

            responce_ocean = requests.request(
                "GET", url_ocean, params=querystring_geonames
            ).json()
            return [responce_ocean["ocean"]["name"], timestamp]
        except requests.exceptions.RequestException as err:
            raise err

    return ["ISS not found", str(date.today())]
