import requests
import json
import datetime as dt
from flask import Flask, jsonify, request

app = Flask(__name__)

class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv["message"] = self.message
        return rv


API_TOKEN = "Medeya2017!"
#your personal key here
key = "RCWWMPLADXCCSTWC9Q6KCL9PG"

# request data from api using your personal key
# use the link to create your own one: https://www.visualcrossing.com/account
def generate_weather(location: str, date: str):
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{date}?include=days&key={key}"

    headers = {"X-Api-Key": key}

    response = requests.get(url, headers=headers)

    if response.status_code == requests.codes.ok:
        return json.loads(response.text)
    else:
        raise InvalidUsage(response.text, status_code=response.status_code)


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route("/")
def home_page():
    return "<p><h2>KMA L2: python Saas.</h2></p>"

# additional functions for changing data to the correct forms
def format_date(timestamp):
    return timestamp.split("T")[0]

def fahrenheit_to_celsius(t):
    return (t - 32) * 5.0/9.0

def to_milibars(value):
    return (value/10000)

# function for dict creating
def extract_weather_data(data, requester_name, location, date):
    weather_data = data['days'][0]
    weather = {
        "temp_c": fahrenheit_to_celsius(weather_data['temp']),
        "wind_kph": weather_data['windspeed'],
        "pressure_mb": to_milibars(weather_data['pressure']),
        "humidity": weather_data['humidity'],
    }
    result = {
        "requester_name": requester_name,
        "timestamp": dt.datetime.utcnow().isoformat(),
        "location": location,
        "date": date,
        "weather": weather
    }
    return result

#main method for componising our data
@app.route("/link", methods=["POST"])
def weather_endpoint():
    json_data = request.get_json()

    if json_data is None:
        raise InvalidUsage("Request data is missing or not in JSON format", status_code=400)
    # getting data from json doc and creating new vars using it
    date = json_data.get("date")
    requester_name = json_data.get("requester_name")
    location = json_data.get("location")
    # checking if toker is correct and is present, checking if other required members are present, etc.
    if date is None or requester_name is None or location is None:
        raise InvalidUsage("date, requester_name, and location are required fields", status_code=400)

    token = json_data.get("token")

    if token != API_TOKEN:
        raise InvalidUsage("wrong API token", status_code=403)

    #collecting data as an response to our request
    weather = generate_weather(location, date)
    # creating right output format via our data
    data = extract_weather_data(weather, requester_name, location, date)

    return data

