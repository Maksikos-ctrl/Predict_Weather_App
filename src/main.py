from weather_api import get_weather_data
from data_processing import process_weather_data
import datetime

def get_input_date(prompt):
    while True:
        try:
            user_input = input(prompt)
            date = datetime.datetime.strptime(user_input, "%Y-%m-%d").date()
            return date.strftime("%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please enter a date in YYYY-MM-DD format.")

if __name__ == "__main__":
    api_key = "VH9RD96MT7SP53FNYD3NWPHUE"
    city = "Zilina"  
    
 
    start_date = get_input_date("Uveďte začiatočný dátum (YYYY-MM-DD): ")


    end_date = get_input_date("Uveďte koncový dátum (YYYY-MM-DD): ")

    weather_data = get_weather_data(api_key, city, start_date, end_date)
    process_weather_data(weather_data)
