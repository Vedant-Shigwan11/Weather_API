import streamlit as st
import requests

# OpenWeatherMap API key
API_KEY = 'your_openweathermap_api_key'

# Function to get weather data
def get_weather(city):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(base_url)
    data = response.json()
    return data

# Streamlit app
def main():
    st.title("Weather App")
    st.write("Enter the name of a city to get the current weather information.")

    # Input for city name
    city = st.text_input("City Name")

    # Fetch and display weather information
    if st.button("Get Weather"):
        if city:
            data = get_weather(city)
            if data["cod"] == 200:
                st.write(f"**City:** {data['name']}, {data['sys']['country']}")
                st.write(f"**Temperature:** {data['main']['temp']} °C")
                st.write(f"**Weather:** {data['weather'][0]['description'].title()}")
                st.write(f"**Humidity:** {data['main']['humidity']}%")
                st.write(f"**Wind Speed:** {data['wind']['speed']} m/s")
            else:
                st.error("City not found. Please enter a valid city name.")
        else:
            st.error("Please enter a city name.")

if __name__ == "__main__":
    main()