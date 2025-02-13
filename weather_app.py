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
    st.markdown("""
        <style>
            body {
                background-color: #1e1e2e;
                color: #ffffff;
            }
            .main-title {
                text-align: center;
                font-size: 36px;
                font-weight: bold;
                color: #ff9800;
            }
            .weather-container {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 15px;
                margin-top: 20px;
            }
            .weather-box {
                background-color: #292b3a;
                padding: 20px;
                border-radius: 12px;
                text-align: center;
                font-size: 18px;
                font-weight: bold;
                width: 200px;
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
                st.image(f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@4x.png", width=120)
                st.markdown("<div class='weather-container'>", unsafe_allow_html=True)
                st.markdown(f"<div class='weather-box'>📍 <b>{data['name']}, {data['sys']['country']}</b></div>", unsafe_allow_html=True)
                st.markdown(f"<div class='weather-box'>🌡 <b>{data['main']['temp']} °C</b></div>", unsafe_allow_html=True)
                st.markdown(f"<div class='weather-box'>💧 <b>{data['main']['humidity']}%</b></div>", unsafe_allow_html=True)
                st.markdown(f"<div class='weather-box'>🌬 <b>{data['wind']['speed']} m/s</b></div>", unsafe_allow_html=True)
                st.markdown(f"<div class='weather-box'>🌡 Feels Like: <b>{data['main']['feels_like']} °C</b></div>", unsafe_allow_html=True)
                st.markdown(f"<div class='weather-box'>🌤 <b>{data['weather'][0]['description'].title()}</b></div>", unsafe_allow_html=True)
                st.markdown(f"<div class='weather-box'>📊 <b>{data['main']['pressure']} hPa</b></div>", unsafe_allow_html=True)
                st.markdown(f"<div class='weather-box'>🌅 <b>{datetime.utcfromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')} UTC</b></div>", unsafe_allow_html=True)
                st.markdown(f"<div class='weather-box'>🌇 <b>{datetime.utcfromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')} UTC</b></div>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.error("❌ City not found. Please enter a valid city name.")
        else:
            st.warning("⚠ Please enter a city name.")

if __name__ == "__main__":
    main()
