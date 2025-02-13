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
    st.set_page_config(page_title="Weather App", page_icon="🌤", layout="wide")
    st.markdown("""
        <style>
            .main-title {
                text-align: center;
                font-size: 36px;
                font-weight: bold;
                color: #ff5733;
            }
            .weather-box {
                background-color: #f0f2f6;
                padding: 20px;
                border-radius: 15px;
                margin-bottom: 10px;
                text-align: center;
                font-size: 18px;
                font-weight: bold;
            }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<h1 class='main-title'>🌎 Weather App</h1>", unsafe_allow_html=True)
    st.write("Enter the name of a city to get the current weather information.")

    city = st.text_input("🌆 City Name", placeholder="Enter city name...")
    
    if st.button("🔍 Get Weather"):
        if city:
            data = get_weather(city)
            if data["cod"] == 200:
                col1, col2 = st.columns([1, 2])
                with col1:
                    st.image(f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@4x.png", width=150)
                with col2:
                    st.markdown(f"<div class='weather-box'>📍 Location: <b>{data['name']}, {data['sys']['country']}</b></div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='weather-box'>🌡 Temperature: <b>{data['main']['temp']} °C</b></div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='weather-box'>💧 Humidity: <b>{data['main']['humidity']}%</b></div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='weather-box'>🌬 Wind Speed: <b>{data['wind']['speed']} m/s</b></div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='weather-box'>🌡 Feels Like: <b>{data['main']['feels_like']} °C</b></div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='weather-box'>🌤 Weather: <b>{data['weather'][0]['description'].title()}</b></div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='weather-box'>📊 Pressure: <b>{data['main']['pressure']} hPa</b></div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='weather-box'>🌅 Sunrise: <b>{datetime.utcfromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')} UTC</b></div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='weather-box'>🌇 Sunset: <b>{datetime.utcfromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')} UTC</b></div>", unsafe_allow_html=True)
            else:
                st.error("❌ City not found. Please enter a valid city name.")
        else:
            st.warning("⚠ Please enter a city name.")

if __name__ == "__main__":
    main()
