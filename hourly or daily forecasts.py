import requests

def get_forecast(forecast_type):
    # API key for OpenWeatherMap API
    API_KEY = "your_api_key_here"

    # Location for which to retrieve weather information
    location = "London,UK"

    # API call to retrieve weather information
    response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_KEY}")
    data = response.json()

    if forecast_type == "hourly":
        # Display the hourly forecast
        print("Hourly Forecast:")
        for i in range(0, 8):
            forecast = data["list"][i]
            time = forecast["dt_txt"]
            temperature = forecast["main"]["temp"]
            weather = forecast["weather"][0]["description"]
            print(f"{time}: {temperature}°C, {weather}")
    elif forecast_type == "daily":
        # Display the daily forecast
        print("Daily Forecast:")
        for i in range(0, 5):
            forecast = data["list"][i * 8]
            date = forecast["dt_txt"].split(" ")[0]
            temperature = (forecast["main"]["temp_min"] + forecast["main"]["temp_max"]) / 2
            weather = forecast["weather"][0]["description"]
            print(f"{date}: {temperature}°C, {weather}")
    else:
        print("Invalid forecast type. Please specify 'hourly' or 'daily'.")

if __name__ == "__main__":
    forecast_type = input("Enter forecast type (hourly/daily): ")
    get_forecast(forecast_type)




