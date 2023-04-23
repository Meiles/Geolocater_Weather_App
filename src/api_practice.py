from geopy.geocoders import Nominatim
import requests

#Grandma's Ranch coordinates: 32.323087, -98.374484
url = 'https://api.weather.gov/points/'


geolocator = Nominatim(user_agent="GEOAPI6")

def get_location_by_address(address):
    location = geolocator.geocode(address)
    return location

def input_coordinates_for_weather(url,latitude,longitude):
    weather_coordinates_url = url + f"{latitude:.4f}" + ',' + f"{longitude:.4f}"
    return weather_coordinates_url


def main():
    address = "4600 Bellaire Dr S, Fort Worth, TX 76109"
    location = get_location_by_address(address)
    local_geocode = input_coordinates_for_weather(url,location.latitude, location.longitude)

    response = requests.get(local_geocode)
    data = response.json()

    forecast_url = data["properties"]["forecast"]
    response = requests.get(forecast_url)
    data = response.json()

    print(data["properties"]["periods"][0]["detailedForecast"])

if __name__ == "__main__":
    main()          