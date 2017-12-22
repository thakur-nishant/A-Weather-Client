import requests
import untangle

url = 'https://api.weather.gov/points/38.9588,-94.624/forecast'
headers = {'Accept': 'application/vnd.noaa.dwml+xml'}

r = requests.get(url, headers=headers)

xml = untangle.parse(r.text)

data = xml.dwml.data[0].parameters

print(data.temperature[0].name.cdata, '=', data.temperature[0].value[0].cdata, data.temperature[0]['units'])
print(data.temperature[1].name.cdata, '=', data.temperature[1].value[0].cdata, data.temperature[0]['units'])

data = xml.dwml.data[1].parameters

print("Dew point =", data.temperature[1].value.cdata, data.temperature[1]['units'])
print("Wind Speed =", data.wind_speed[0].value.cdata, "km/hr")

