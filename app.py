
from flask import Flask
import json
import weather

app = Flask(__name__)


# @app.route("/")
# def hello():
#     return "Hello, World"

# @app.route("/weather-cities/")
# def weather_route():
#     temp = json.dumps(weather.weather())
#     return temp

@app.route("/weather-city/<city>")
def weather_city(city):
    temp = json.dumps(weather.weather(city))
    return "Temperature in " + city + " is " + temp

# @app.route("/weather/my-cities/")
# def weather_multiple_cities():
#     return "Cluj : 15, New York :10"
