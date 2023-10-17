import os
import requests

print("\nWeather Forcasting Application\n")

api_key = os.environ.get('API_KEY')


def get_weather_info(key):
    city = input("Enter the City: ")

    print("Fetching information...")
    r = requests.get("https://api.openweathermap.org/data/2.5/weather?",
                     params={"q": f"{city}", "APPID": f"{key}", "units": "metric"})

    if r.status_code == 200:
        weather_data = r.json()
        country = weather_data['sys']['country']
        print("\nWeather Information\n")
        print(f"Weather in {city}, {country}: {weather_data['weather'][0]['main']}")
        print(f"Temperature: {weather_data['main']['temp']} celsius")
        print(f"Feels like: {weather_data['main']['feels_like']}")
        print(f"Maximum temperature: {weather_data['main']['temp_max']}")
        print(f"Minimum temperature: {weather_data['main']['temp_min']}")

        print('Do you want to get info about any other city?  y/n')
        is_ask_again = input()
        if is_ask_again in ['y' or 'Y']:
            get_weather_info(key)
        else:
            print('Thank you for using our service!')
    else:
        print(r)


get_weather_info(api_key)


