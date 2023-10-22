import os

import gradio
import requests

print("\nWeather Forcasting Application\n")

api_key = os.environ.get('API_KEY')


def get_weather_info(city: str, key=api_key):
    # city = input("Enter the City: ")
    city = city
    print("Fetching information...")
    r = requests.get("https://api.openweathermap.org/data/2.5/weather?",
                     params={"q": f"{city}", "APPID": f"{key}", "units": "metric"})

    if r.status_code == 200:
        weather_data = r.json()
        country = weather_data['sys']['country']
        weather_info = f"Weather in {city}, {country}:    {weather_data['weather'][0]['main']}"
        weather_info += f"\nTemperature:  {weather_data['main']['temp']} celsius\n"
        weather_info += f"Feels like:  {weather_data['main']['feels_like']}\n"
        weather_info += f"Maximum temperature:  {weather_data['main']['temp_max']}\n"
        weather_info += f"Minimum temperature:  {weather_data['main']['temp_min']}\n"
        return weather_info
    else:
        return "Error fetching weather information."

    #     print("\nWeather Information\n")
    #     print(f"Weather in {city}, {country}: {weather_data['weather'][0]['main']}")
    #     print(f"Temperature: {weather_data['main']['temp']} celsius")
    #     print(f"Feels like: {weather_data['main']['feels_like']}")
    #     print(f"Maximum temperature: {weather_data['main']['temp_max']}")
    #     print(f"Minimum temperature: {weather_data['main']['temp_min']}")
    #
    #     print('Do you want to get info about any other city?  y/n')
    #     is_ask_again = input()
    #     if is_ask_again in ['y' or 'Y']:
    #         get_weather_info(key)
    #     else:
    #         print('Thank you for using our service!')
    # else:
    #     print(r)


# get_weather_info(api_key)

gradio.Interface(fn=get_weather_info, inputs='text', outputs='text'
                 ).launch(share=True)
