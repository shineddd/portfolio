import tkinter
import customtkinter
import requests
from PIL import Image

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")
app = customtkinter.CTk()
app.geometry("480x580")
app.resizable(width=False, height=False)

app.logo = customtkinter.CTkImage(dark_image=Image.open("img.png"), size=(64, 64))
app.logo_label = customtkinter.CTkLabel(master=app, text="", image=app.logo)
app.logo_label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)


def get_weather():
    city = CTkentry.get()
    api_key = "29884651917943bb98b73a58f26b914d"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    weather_description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    weather_info.configure(
        text=f"Погода в городе {city}: {weather_description}\nТемпература: {temperature}°C\nВлажность: {humidity}%\nСкорость ветра: {wind_speed} м/с")


def button_function():
    print("Button pressed")


CTkentry = customtkinter.CTkEntry(master=app, width=150, height=20)
CTkentry.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
get_weather_button = customtkinter.CTkButton(master=app, text="Получить погоду", command=get_weather)
get_weather_button.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
weather_info = customtkinter.CTkLabel(master=app, text='')
weather_info.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
sozdali_label = customtkinter.CTkLabel(master=app, text="Сделали Скупков,Корочкин,Кернер")
sozdali_label.place(relx=0.3, rely=0.95, anchor=tkinter.CENTER)

app.mainloop()