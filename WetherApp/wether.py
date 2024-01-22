import requests
from datetime import datetime
def get_weather(api_key, city):
    url = 'https://api.tomorrow.io/v4/weather/forecast'
    params = {
        'location': city,
        'apikey': api_key
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return f"Error: {response.status_code}, {response.text}"



def main():
    api_key = 'gGk6s1NX8nGje8Auybi1sIcLqj12o5bx'  # Replace with your actual API key
    city = input("Enter the city name: ")

    weather_data = get_weather(api_key, city)

    if isinstance(weather_data, dict):
        print(f"Weather information for {weather_data['location']['name']}:\n")
    

        formatted_time = datetime.strptime(weather_data['timelines']['minutely'][0]['time'], '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d %H:%M:%S')



        print(f"Last Updated Time: {formatted_time}")
        print(f"Last Updated Time {weather_data['timelines']['minutely'][0]['time']}")
        print(f"Tempeture : {weather_data['timelines']['minutely'][0]['values']['temperature']}")
        print(f"Humidity : {weather_data['timelines']['minutely'][0]['values']['humidity']}")
        print(f"Wind Speed : {weather_data['timelines']['minutely'][0]['values']['windSpeed']}")
        print(f"Visibility : {weather_data['timelines']['minutely'][0]['values']['visibility']}")
        print(f"Dew Point : {weather_data['timelines']['minutely'][0]['values']['dewPoint']}")

    else:
        print(f"Wether Details for {city} is not found")

if __name__ == "__main__":
    main()
