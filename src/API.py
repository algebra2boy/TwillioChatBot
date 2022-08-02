
import requests
import src.messages as m # import all the constants and messages


def get_weather_info(latitude:str, longtitude: str, weather_APIKEY: str) -> str:
	try:
		weather_info = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longtitude}&appid={weather_APIKEY}")
		weather_info.raise_for_status()
		# Code here will only run if the request is successful (200/201)
		return weather_info.json()
	except requests.exceptions.HTTPError:
		return m.weatherNOTFOUND






#TODO
