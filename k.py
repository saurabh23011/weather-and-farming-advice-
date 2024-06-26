import streamlit as st
import requests

# Function to get weather data
def get_weather_data(city):
    api_key = 'e7816266b7fb1b25d3126f54fbc2b91a'
  # Replace  OpenWeatherMap API key
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(base_url)
    return response.json()

# Function to provide farming advice
def farming_advice(rain, temperature):
    if rain:
        return "Rain is expected. Ensure proper drainage for your fields to avoid waterlogging."
    else:
        if temperature > 30:
            return "High temperatures expected. Ensure adequate irrigation to keep crops hydrated."
        elif temperature < 10:
            return "Cold weather expected. Protect your crops from frost."
        else:
            return "Moderate weather expected. Continue regular farming practices."

st.title("Weather and Farming Advice")

# Input for city name
city = st.text_input("Enter your city:", "YourCity")

if city:
    weather_data = get_weather_data(city)
    
    if weather_data.get('cod') != 200:
        st.error("City not found.")
    else:
        temperature = weather_data['main']['temp']
        weather_description = weather_data['weather'][0]['description']
        rain = "rain" in weather_description.lower()

        st.write(f"Current Temperature: {temperature}°C")
        st.write(f"Weather Description: {weather_description.capitalize()}")
        
        advice = farming_advice(rain, temperature)
        st.write(f"Farming Advice: {advice}")

        # Extra: Estimate water needs based on temperature
        if not rain:
            water_needs = 5 if temperature > 30 else 3 if temperature > 20 else 2
            st.write(f"Estimated Water Needs: {water_needs} liters per square meter")
