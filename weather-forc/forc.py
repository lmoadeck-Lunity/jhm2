import requests
import matplotlib.pyplot as plt
api_key = '4fe58730ec324f36b3232041243011' # API KEY HERE, TODO: REMOVE

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
print(f"Temperacture: {temperacture}°C\nUV: {uv}\nHumidity: {humid}%")
plt.bar(['Temperacture', 'UV', 'Humidity'], [temperacture, uv, humid])
plt.show()
