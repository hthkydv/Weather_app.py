import requests
from tkinter import *
from tkinter import messagebox
from dotenv import load_dotenv
import os

load_dotenv()

Api_key = os.getenv('API_KEY') 
Base_url=os.getenv("Base_URL")

root = Tk()
root.title("WeatherNow")
root.geometry("1500x800")
print("hrk")

city_label = Label(root, text="Enter City:", font=("Helvetica", 12))
city_label.pack(pady=10)

city_entry = Entry(root, font=("Helvetica", 14))
city_entry.pack(pady=10)

fetch_button = Button(root, text="Get Weather", command=lambda: get_weather(city_entry.get()))
fetch_button.pack(pady=20)

weather_label = Label(root, text="", font=("Helvetica", 12))
weather_label.pack(pady=20)

def get_weather(city):
    api_key = Api_key
    base_url = Base_url
    complete_url = base_url + "appid=" + api_key + "&q=" + city + "&units=metric"

    try:
        response = requests.get(complete_url)
        data = response.json()

        if data["cod"] != "404":
            main = data["main"]
            wind = data["wind"]
            weather_desc = data["weather"][0]["description"]

            temperature = main["temp"]
            humidity = main["humidity"]
            pressure = main["pressure"]
            wind_speed = wind["speed"]

            weather_info = f"Temperature: {temperature}°C\n"
            weather_info += f"Humidity: {humidity}%\n"
            weather_info += f"Pressure: {pressure} hPa\n"
            weather_info += f"Wind Speed: {wind_speed} m/s\n"
            weather_info += f"Description: {weather_desc}"

            weather_label.config(text=weather_info)
        else:
            messagebox.showerror("Error", "City Not Found!")
    except Exception as e:
        messagebox.showerror("Error", "Unable to fetch data!")

root.mainloop()
