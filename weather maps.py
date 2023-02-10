import requests
import folium

def get_weather_data(location):
    # API key for OpenWeatherMap API
    API_KEY = "your_api_key_here"

    # API call to retrieve weather information
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}")
    data = response.json()
    
    return data

def display_weather_map(data):
    # Create a map centered at the location
    map = folium.Map(location=[data["coord"]["lat"], data["coord"]["lon"]], zoom_start=10)
    
    # Add a marker for the location with the current temperature
    folium.Marker(
        location=[data["coord"]["lat"], data["coord"]["lon"]],
        popup=f"Temperature: {data['main']['temp']}°C, {data['weather'][0]['description']}",
        ).add_to(map)

    # Display the map
    map.save("weather_map.html")

if __name__ == "__main__":
    location = input("Enter location: ")
    data = get_weather_data(location)
    display_weather_map(data)






