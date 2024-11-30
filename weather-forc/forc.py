import requests
import matplotlib.pyplot as plt
import py_dotenv
import os

py_dotenv.read_dotenv("./.env")

# api_key = 'd' # API KEY HERE, TODO: REMOVE
api_key = os.getenv('WEATHER_API_KEY')

headers = {
    'Content-Type': 'application/json',
}
url = 'http://api.weatherapi.com/v1/current.json?key=' + api_key
location = input("Enter the location: ")
url += '&q=' + location
response = requests.get(url, headers=headers)
data = response.json()
temperacture = data['current']['temp_c']
uv = data['current']['uv']
humid = data['current']['humidity']
print(f"Temperature: {temperacture}°C\nUV: {uv}\nHumidity: {humid}%")
plt.bar(['Temperature', 'UV', 'Humidity'], [temperacture, uv, humid])
plt.show()
