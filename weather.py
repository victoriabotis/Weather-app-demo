import requests

from secrets import app_id

# def weather():
# 	url1 = f"http://api.openweathermap.org/data/2.5/weather?q=Cluj-Napoca&appid={app_id}&units=metric"
# 	url2 = f"http://api.openweathermap.org/data/2.5/weather?q=Paris&appid={app_id}&units=metric"
# 	url3 = f"http://api.openweathermap.org/data/2.5/weather?q=Aruba&appid={app_id}&units=metric"
# 	response1 = requests.get(url1)
# 	weather_Cluj = response1.json()
# 	temp_Cluj = weather_Cluj["main"]["temp"]
# 	response2 = requests.get(url2)
# 	weather_Paris = response2.json()
# 	temp_Paris = weather_Paris["main"]["temp"]
# 	response3 = requests.get(url3)
# 	weather_Aruba = response3.json()
# 	temp_Aruba = weather_Aruba["main"]["temp"]
# 	return {"Cluj-Napoca" : round(temp_Cluj), "Paris" : round(temp_Paris), "Aruba" : round(temp_Aruba)}


def weather(city):

	url= f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={app_id}&units=metric"
	response = requests.get(url())
	weather_city = response.json()
	temp_city = weather_city["main"]["temp"] - 273.15
	return {f"{city}" : "%.2f" % (temp_city)}