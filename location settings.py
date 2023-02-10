def save_location_settings(location, units, language):
    # Save the location-based settings to a file
    with open("location_settings.txt", "w") as f:
        f.write(f"{location}\n{units}\n{language}")

def load_location_settings():
    # Load the location-based settings from a file
    try:
        with open("location_settings.txt", "r") as f:
            data = f.readlines()
        location = data[0].strip()
        units = data[1].strip()
        language = data[2].strip()
        return location, units, language
    except FileNotFoundError:
        return None, None, None

if __name__ == "__main__":
    # Load the location-based settings
    location, units, language = load_location_settings()

    # If no location-based settings were found, prompt the user to set them
    if location is None or units is None or language is None:
        location = input("Enter location: ")
        units = input("Enter units (metric or imperial): ")
        language = input("Enter language (en, fr, etc.): ")
        save_location_settings(location, units, language)

    # Use the location-based settings
    print(f"Location: {location}")
    print(f"Units: {units}")
    print(f"Language: {language}")








