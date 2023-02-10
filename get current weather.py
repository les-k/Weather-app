import requests

def get_weather():
    # API key for OpenWeatherMap API
    API_KEY = "your_api_key_here"

    # Location for which to retrieve weather information
    location = "London,UK"

    # API call to retrieve weather information
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}")
    data = response.json()

    # Extract relevant information from the API response
    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    # Display the weather information
    print(f"The current weather in {location} is {weather}.")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind speed: {wind_speed} meters/sec")

if __name__ == "__main__":
    get_weather()





