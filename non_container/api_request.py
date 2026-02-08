import requests
api_key="18ae3ef9a4d1c7e7e85097ff9c2342ea"
api_url ="https://api.weatherstack.com/current?access_key=18ae3ef9a4d1c7e7e85097ff9c2342ea&query=New York"

 #"https://api.weatherstack.com/current?access_key={api_key}&query=New York"
#https://api.weatherstack.com/current?access_key=18ae3ef9a4d1c7e7e85097ff9c2342ea&query=New York

def fetch_data():
    print("Fetching data from API")
    try:
        response=requests.get(api_url)
        response.raise_for_status()
        print("Api Response received successfully")
        return response.json()
        
    
    except requests.exceptions.RequestException as e:
        print("Error ouccred e is: {e}")
        raise



def moc_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2026-01-31 22:52', 'localtime_epoch': 1769899920, 'utc_offset': '-5.0'}, 'current': {'observation_time': '03:52 AM', 'temperature': -9, 'weather_code': 113, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0008_clear_sky_night.png'], 'weather_descriptions': ['Clear '], 'astro': {'sunrise': '07:07 AM', 'sunset': '05:13 PM', 'moonrise': '03:46 PM', 'moonset': '06:28 AM', 'moon_phase': 'Waxing Gibbous', 'moon_illumination': 95}, 'air_quality': {'co': '203.85', 'no2': '12.15', 'o3': '61', 'so2': '2.75', 'pm2_5': '5.55', 'pm10': '5.85', 'us-epa-index': '1', 'gb-defra-index': '1'}, 'wind_speed': 21, 'wind_degree': 16, 'wind_dir': 'NNE', 'pressure': 1017, 'precip': 0, 'humidity': 53, 'cloudcover': 0, 'feelslike': -17, 'uv_index': 0, 'visibility': 16, 'is_day': 'no'}}