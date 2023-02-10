import requests
from PIL import Image

def get_radar_image():
    # API key for OpenWeatherMap API
    API_KEY = "your_api_key_here"

    # Location for which to retrieve radar image
    location = "London,UK"

    # API call to retrieve radar image
    response = requests.get(f"http://api.openweathermap.org/img/w/radar.png?lat={location.split(',')[0]}&lon={location.split(',')[1]}&appid={API_KEY}")
    with open("radar.png", "wb") as f:
        f.write(response.content)

    # Display the radar image
    image = Image.open("radar.png")
    image.show()

if __name__ == "__main__":
    get_radar_image()





