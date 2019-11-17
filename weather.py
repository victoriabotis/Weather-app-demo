import requests

from secrets import app_id

def weather():
	url = f"http://api.openweathermap.org/data/2.5/weather?q=Cluj-Napoca&appid={app_id}&units=metric"
	response = requests.get(url)
	weather_Cluj = response.json()
	temp_Cluj = weather_Cluj["main"]["temp"]
	return {"Cluj-Napoca" : round(temp_Cluj)}