import requests

def get_weather_data(api_key, city, start_date, end_date):
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{start_date}/{end_date}?key={api_key}&unitGroup=metric&include=obs%2Cfcst%2Cstats%2Calerts%2Ccurrent"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch weather data:", response.text)
        return None
