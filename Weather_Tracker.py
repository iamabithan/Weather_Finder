from tkinter import *
import requests
from tkinter.font import Font

def get_weather():
    city = city_text.get()
    api_key = "2110d6649135dd45760cb6a89de40786"  
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(base_url)
    weather_data = response.json()
    
    if weather_data["cod"] == 200:  
        main = weather_data["main"]
        wind = weather_data["wind"]         
        weather = weather_data["weather"][0]
        
        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        wind_speed = wind["speed"]
        description = weather["description"]
        
        
        weather_info = f"Temperature: {temperature}°C\n"
        weather_info += f"Pressure: {pressure} hPa\n"
        weather_info += f"Humidity: {humidity}%\n"
        weather_info += f"Wind Speed: {wind_speed} m/s\n"
        weather_info += f"Description: {description.capitalize()}\n"
        
        label.config(text=weather_info)
        print(weather_info)
    else:
        label.config(text="City not found. Please try again.")

root = Tk()
root.geometry('400x400')
root.resizable(0, 0)
root.title("Weather App")
myfont =Font(weight="bold",size="14")
city_text = StringVar()
city_entry = Entry(root, textvariable=city_text)
city_entry.pack(pady=20)

get_weather_button = Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack(pady=10)

label = Label(root, text="", font=myfont)
label.pack(pady=20)

root.mainloop()
