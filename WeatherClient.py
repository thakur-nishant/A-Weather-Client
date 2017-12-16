'''
Weather Client - Nishant Thakur
University of Texas at Arlington - UID: 1001544591
'''
import json
import requests

#function to request for weather report which takes location coordinates as parameters
def get_weather_report(location):
    #make a request to national weather service using the location cordinates
    response = requests.get('https://api.weather.gov/points/'+location)
    #loading the response in a variable
    json_data = json.loads(response.text)
    #parsing the response to get the location of nearest weather server to the location coordinates
    data = json_data['properties']
    # print(data)
    gridData = data['forecastGridData']
    #make a request to the server for weather report
    response = requests.get(gridData)
    json_data = json.loads(response.text)
    #parse the response to get values from the response
    data = (json_data['properties'])
    # print(data)
    #print the requires data to get the result
    print("Maximum Temprature = ", data['maxTemperature']['values'][0]['value'],"°C")
    print("Minimum Temprature = ", data['minTemperature']['values'][0]['value'],"°C")
    print("Dew Point = ", data['dewpoint']['values'][0]['value'],"°C")
    print("relativeHumidity = ", data['relativeHumidity']['values'][0]['value'],"%")
    print("windDirection = ", data['windDirection']['values'][0]['value'],"degree angle")
    print("windSpeed = ", data['windSpeed']['values'][0]['value'],"m/s")
    print("probabilityOfPrecipitation = ", data['probabilityOfPrecipitation']['values'][0]['value'],"%")

#ask user for the coordinates of the location
location = input("Enter cooridinates: ")
#loop through the entire process for refresh
while True:
    # "32.7357,-97.1081" - Arlington
    # "32.7767,-96.7970" - Dallas
    # "40.7128,-74.0060"  - New York
    # "36.7783,-119.4179" - California

    #function call to get the weather report
    get_weather_report(location)

    refresh = input("Press 'Y' or 'y' to refresh or any other key to exit: ")
    if refresh == 'Y' or refresh == 'y':
        pass
    else:
        print("Exiting Weather Client!")
        break
