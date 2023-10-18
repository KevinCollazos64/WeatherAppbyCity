import requests


class Geocoder:
    def __init__(self, key):
        self.key = key
        self.converter(self.key)

    def converter(self, code):
        code_for_api = code.replace(" ", "%20")
        api_key = ""
        limit = 5
        response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={code_for_api}&limit={limit}&appid={api_key}')
        if response.status_code == 200:
            data = response.json()
            print(f"Pulling {code} locations...")
            if len(data) > 1:
                for i in range(limit):
                    name = data[i]
                    print(f"{i}: , {name}")
                while True:
                    try:
                        user_choice = int(input('Select the correct location: '))
                        if user_choice < limit:
                            lat, lon = data[user_choice]['lat'], data[user_choice]['lon']
                            return lat, lon
                        else:
                            print("Please enter a valid number")
                    except ValueError:
                        print("Please enter an integer")
            return data[0]['lat'], data[0]['lon']




