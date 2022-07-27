import requests

lat = 42.3785285949707
lon = -71.06903076171875
OpenWeatherAPI_KEY="1942a1109fed383d1ecff49c566b2dcd"

try:
	weather_info = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OpenWeatherAPI_KEY}")
	weather_info.raise_for_status()
	# Code here will only run if the request is successful (200/201)
except requests.exceptions.HTTPError as errh:
	print(errh)

print(weather_info)
print(weather_info.json())
print()