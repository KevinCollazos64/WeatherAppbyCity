import geocoder as geo
import requests

class GetWeather:
    def __init__(self):
        while True:
            self.key = input("Input city name or zip code: ")
            if isinstance(self.key, str) or isinstance(self.key, int):
                break
            else:
                print("Please enter a valid location")
        self.coder = geo.Geocoder(self.key)
        self.report(self.key)

    def report(self, key):
        api_key = "94fd6163437d7e2917266d7f9f6e11c8"
        lat, lon = self.coder.converter(key)
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}")
        #if response.status_code == 200:
            #data = response.json()
            #for k, v in data:
             #   print(k, v)


sample = GetWeather()


