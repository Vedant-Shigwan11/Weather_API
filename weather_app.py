import streamlit as st
import requests
from datetime import datetime

# OpenWeatherMap API key
API_KEY = '0efff74ba5af8136291968aa32d12a7a'

# Function to get weather data
def get_weather(city):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(base_url)
    return response.json()

# Streamlit app
def main():
    st.set_page_config(page_title="Weather App", page_icon="🌤", layout="centered")
    st.title("🌎 Weather App")
    st.write("Enter the name of a city to get the current weather information.")

    # Input for city name
    city = st.text_input("🌆 City Name", placeholder="Enter city name...")

    # Fetch and display weather information
    if st.button("🔍 Get Weather"):
        if city:
            data = get_weather(city)
            if data["cod"] == 200:
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader(f"📍 {data['name']}, {data['sys']['country']}")
                    st.image(f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png", width=100)
                with col2:
                    st.metric("🌡 Temperature", f"{data['main']['temp']} °C")
                    st.metric("💧 Humidity", f"{data['main']['humidity']}%")
                    st.metric("🌬 Wind Speed", f"{data['wind']['speed']} m/s")

                st.write(f"**Weather:** {data['weather'][0]['description'].title()}")
                st.write(f"**Feels Like:** {data['main']['feels_like']} °C")
                st.write(f"**Pressure:** {data['main']['pressure']} hPa")
                st.write(f"**Sunrise:** {datetime.utcfromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')} UTC")
                st.write(f"**Sunset:** {datetime.utcfromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')} UTC")
            else:
                st.error("❌ City not found. Please enter a valid city name.")
        else:
            st.warning("⚠ Please enter a city name.")

if __name__ == "__main__":
    main()
