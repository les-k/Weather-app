import requests

def get_historical_weather(location, start_date, end_date):
    # API key for OpenWeatherMap API
    API_KEY = "your_api_key_here"

    # API call to retrieve historical weather data
    response = requests.get(f"http://api.openweathermap.org/data/2.5/history/city?q={location}&start={start_date}&end={end_date}&appid={API_KEY}")
    data = response.json()
    
    return data

if __name__ == "__main__":
    location = input("Enter location: ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    data = get_historical_weather(location, start_date, end_date)
    print(data)







