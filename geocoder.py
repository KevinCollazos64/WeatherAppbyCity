import requests


class Geocoder:
    def __init__(self, key):
        self.key = key

    def converter(self, code):
        code_for_api = code.replace(" ", "%20")
        api_key, limit = "", 5  # enter Weatherapi key here
        response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={code_for_api}&limit={limit}&appid={api_key}')
        if response.status_code == 200:
            data = response.json()
            print(f"Pulling {code} locations...")
            if len(data) > 1:
                for i in range(limit):
                    name, state, country = data[i]['name'], data[i]['state'], data[i]['country'],
                    print(f"{i}: , {name, state, country}")
                while True:
                    try:
                        user_choice = int(input('Select the correct location: '))
                        if user_choice < limit:
                            lat, lon, state, country = data[user_choice]['lat'], \
                                                       data[user_choice]['lon'], \
                                                       data[user_choice]['state'],\
                                                       data[user_choice]['country'],
                            return lat, lon, state, country
                        else:
                            print("Please enter a valid number")
                    except ValueError:
                        print("Please enter an integer")
            else:
                raise TypeError('Could not fetch info! Try again')




