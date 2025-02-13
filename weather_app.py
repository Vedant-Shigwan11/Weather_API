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
    st.markdown(
        """
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
        </style>
        """, 
        unsafe_allow_html=True
    )
    
    st.markdown("<h1 class='main-title'>🌎 Weather App</h1>", unsafe_allow_html=True)
    st.write("Enter the name of a city to get the current weather information.")

    city = st.text_input("🌆 City Name", placeholder="Enter city name...")
    
    if st.button("🔍 Get Weather"):
        if city:
            data = get_weather(city)
            if data["cod"] == 200:
                st.image(f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@4x.png", width=120)
                st.markdown(f"### 📍 {data['name']}, {data['sys']['country']}")
                st.markdown(f"**🌡 Temperature:** {data['main']['temp']} °C")
                st.markdown(f"**💧 Humidity:** {data['main']['humidity']}%")
                st.markdown(f"**🌬 Wind Speed:** {data['wind']['speed']} m/s")
                st.markdown(f"**🌡 Feels Like:** {data['main']['feels_like']} °C")
                st.markdown(f"**🌤 Condition:** {data['weather'][0]['description'].title()}")
                st.markdown(f"**📊 Pressure:** {data['main']['pressure']} hPa")
                st.markdown(f"**🌅 Sunrise:** {datetime.utcfromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')} UTC")
                st.markdown(f"**🌇 Sunset:** {datetime.utcfromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')} UTC")
            else:
                st.error("❌ City not found. Please enter a valid city name.")
        else:
            st.warning("⚠ Please enter a city name.")

if __name__ == "__main__":
    main()
