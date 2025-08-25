import re
import requests

API_KEY = "906b6939735602a519447e37a839d229"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def is_valid_zip(zip_code):
    return re.fullmatch(r'\d{5}', zip_code) is not None

def get_weather(zip_code):
    params = {
        "zip": zip_code,
        "appid": API_KEY,
        "units": "imperial"  # Use 'metric' for Celsius
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        city = data.get("name")
        weather = data["weather"][0]["description"].title()
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]

        print(f"\n📍 Weather for {city} (ZIP: {zip_code}):")
        print(f"   - Condition: {weather}")
        print(f"   - Temperature: {temp}°F (Feels like: {feels_like}°F)")
        print(f"   - Humidity: {humidity}%\n")

    except requests.HTTPError as http_err:
        if response.status_code == 404:
            print("[!] Error: Zip code not found in weather database.")
        else:
            print(f"[!] HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"[!] Unexpected error: {err}")

def main():
    print("=== Weather Forecast App ===")
    while True:
        zip_code = input("Enter a 5-digit US ZIP code (or type 'exit' to quit): ").strip()
        if zip_code.lower() == 'exit':
            print("Goodbye!")
            break

        if not is_valid_zip(zip_code):
            print("[!] Invalid ZIP code format. Please enter exactly 5 digits.\n")
            continue

        get_weather(zip_code)

if __name__ == "__main__":
    main()
