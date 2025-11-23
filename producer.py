import requests
from kafka import KafkaProducer
import json
import time
import os

# Get the API_KEY from the environment variable.
API_KEY = os.getenv("WEATHER_API_KEY")
if not API_KEY:
    raise ValueError("API_KEY not found! Check your environment variable or .env file.")

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

CITIES = ["Istanbul", "Ankara", "Izmir"]

while True:
    for city in CITIES:
        url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            simplified_data = {
                "city": data["location"]["name"],
                "temp_c": data["current"]["temp_c"],
                "humidity": data["current"]["humidity"],
                "condition": data["current"]["condition"]["text"],
                "timestamp": data["location"]["localtime"]
            }
            producer.send('sensor-data', value=simplified_data)
            print("Sent:", simplified_data)
        else:
            print("API request failed:", response.status_code)
    time.sleep(60)



