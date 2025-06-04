import requests

def safe_weather_data_fetch(city):
    """Fetch weather data for a city from wttr.in API with basic error handling"""
    try:
        url = f"http://wttr.in/{city}?format=j1"
        response = requests.get(url)

        try:
            response.raise_for_status()  # Check if the request was successful
        except:
            return "Error: Failed to retrieve data from the weather service."

        data = response.json()

        try:
            weather_info = {
                'city': city,
                'temperature': data['current_condition'][0]['temp_C'],
                'wind_speed': data['current_condition'][0]['windspeedKmph'],
                'description': data['current_condition'][0]['weatherDesc'][0]['value']
            }
            return weather_info
        except:
            return "Error: Unable to extract weather data."

    except:
        return "Error: Something went wrong."

# Example usage
if __name__ == "__main__":
    city = input("Enter city name: ")
    result = safe_weather_data_fetch(city)
    print(result)
