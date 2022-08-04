import requests
import googlemaps
import src.messages as m  # import all the constants and messages
import src.messages as m # import all the constants and messages


def get_weather_info(latitude: str, longitude: str, weather_apikey: str) -> str:
    try:
        weather_info = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat="
                                    f"{latitude}&lon={longitude}&appid={weather_apikey}")
        weather_info.raise_for_status()
        # Code here will only run if the request is successful (200/201)
        return weather_info.json()
    except requests.exceptions.HTTPError:
        return m.weatherNOTFOUND

def get_address(lat, lon, key):
    """receives latitude, longitude, and googlemapsapi key to return address of a location"""
    geo = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lon}&key={key}").json()
    address_components = geo['results'][0]['address_components']
    return f"{address_components[0]['long_name']} {address_components[1]['long_name']} " \
           f"{address_components[2]['long_name']}, {address_components[4]['short_name']}"

def get_address(lat, lon, key):
    """receives latitude, longitude, and googlemapsapi key to return address of a location"""
    geo = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lon}&key={key}").json()
    address_components = geo['results'][0]['address_components']
    return f"{address_components[0]['long_name']} {address_components[1]['long_name']} " \
           f"{address_components[2]['long_name']}, {address_components[4]['short_name']}"


def get_directions_info(lat, lon, destination, mode, key):
    gmap = googlemaps.Client(key=key)
    origin = get_address(lat, lon, key)
    directions_result = gmap.directions(origin, destination, mode.lower())
    return f"To get from {origin} to {destination}, it will take {directions_result[0]['legs'][0]['duration']['text']}"\
        f" ({directions_result[0]['legs'][0]['distance']['text']}) by {mode.lower()}"
