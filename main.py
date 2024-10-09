import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

BASE_URL = 'https://www.metaweather.com/api/location/'

def get_city_woeid(city_name):
    """Finds the WOEID (Where On Earth ID) of a city."""
    search_url = BASE_URL + 'search/'
    params = {'query': city_name}

    # Create a session with retry strategy
    session = requests.Session()
    retry = Retry(total=5, backoff_factor=0.1, status_forcelist=[500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('https://', adapter)

    try:
        # Make the request using the session with retries
        response = session.get(search_url, params=params)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching city WOEID: {e}")
        return None

    data = response.json()
    if data:
        return data[0]['woeid']
    else:
        print(f"City '{city_name}' not found.")
        return None

def get_weather(woeid):
    """Fetches the current weather for a city using its WOEID."""
    weather_url = BASE_URL + str(woeid) + '/'
    
    # Create a session with retry strategy
    session = requests.Session()
    retry = Retry(total=5, backoff_factor=0.1, status_forcelist=[500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('https://', adapter)
    
    try:
        response = session.get(weather_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching weather data: {e}")
        return
    
    data = response.json()
    city = data['title']
    weather_state = data['consolidated_weather'][0]['weather_state_name']
    temperature = data['consolidated_weather'][0]['the_temp']
    humidity = data['consolidated_weather'][0]['humidity']
    
    print(f"\nWeather in {city}:")
    print(f"Temperature: {temperature:.2f}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {weather_state}")

if __name__ == '__main__':
    city = input("Enter city name: ")
    woeid = get_city_woeid(city)
    
    if woeid:
        get_weather(woeid)
