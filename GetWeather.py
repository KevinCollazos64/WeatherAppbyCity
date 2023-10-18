import geocoder as geo
import requests


class GetWeather:
    def __init__(self):
        while True:
            self.key = input("Input city name: ")
            if isinstance(self.key, str) or isinstance(self.key, int):
                break
            else:
                print("Please enter a valid location")
        self.coder = geo.Geocoder(self.key)
        self.report(self.key)

    def report(self, key):
        api_key = ""
        lat, lon, state, country = self.coder.converter(key)
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric")
        if response.status_code == 200:
            data = response.json()
            main, wind, clouds = data['main'], data['wind'], data['clouds']
            print(f"{self.key.capitalize()}, {state} {country}:\n🌡:️{main}\n💨:{wind}\n☁:{clouds}")





