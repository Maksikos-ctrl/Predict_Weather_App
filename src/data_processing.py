import pandas as pd

def process_weather_data(weather_data):
    if weather_data:
        data = {'Dátum': [], 'Teplota (°C)': [], 'Vlhkosť (%)': [], 'Rýchlosť vetra (m/s)': [], 'Popis počasia': []}

        for entry in weather_data['days']:
            date = entry['datetime']
            temperature = entry.get('temp', 'N/A')
            humidity = entry.get('humidity', 'N/A')
            wind_speed = entry.get('wspd', 'N/A')
            weather_description = entry.get('conditions', 'N/A')

            data['Dátum'].append(date)
            data['Teplota (°C)'].append(temperature)
            data['Vlhkosť (%)'].append(humidity)
            data['Rýchlosť vetra (m/s)'].append(wind_speed)
            data['Popis počasia'].append(weather_description)

        df = pd.DataFrame(data)
        df.to_excel('weather_data.xlsx', index=False, sheet_name='Počasie')

        print("Weather data saved successfully to 'weather_data.xlsx'.")

    else:
        print("No weather data available.")
