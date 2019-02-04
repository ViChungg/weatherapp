import requests
import json
import io
import datetime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from urllib.request import urlopen

# gets the url location of the image
def getImage(icon):
    img = "http://openweathermap.org/img/w/"
    img += icon + '.png'
    return img

# gets weather information from the API
def getLocationWeather(location, frame):
    city = location
    api = 'http://api.openweathermap.org/data/2.5/weather?appid=5431043a6fcde69100a7f9f0c48945f2&q='
    data = requests.get(api + city + str('&units=metric')).json()
    cityName = json.dumps(data['name']) + ', ' + json.dumps(data['sys']['country'])
    cityID = json.dumps(data['id'])
    temp = json.dumps(data['main']['temp']) + '°C'
    weather = json.dumps(data['weather'][0]['main'])
    img = getImage(data['weather'][0]['icon'])
    displayLocationWeather(cityName, weather, temp, img, frame)

# displays the weather information
def displayLocationWeather(city, weather, temp, image, frame):
    info = weather.replace('\"', '')
    getCity(city, frame)
    getWeatherImage(image, frame)
    weather = Label(frame, text=info, padx=10, pady=0, bg='white')
    weather.config(font=("Courier", 10))
    weather.grid(column=1, row=2, sticky="nsew")
    temperature = Label(frame, text=temp, padx=10, pady=10, bg='white')
    temperature.config(font=("Courier", 35))
    temperature.grid(column=1, row=4, sticky="nsew")
    getDate(frame)

# gets the city name and creates a label
def getCity(cityName, frame):
    city = Label(frame, text=cityName.replace('\"', ''), pady=20, bg='white')
    city.config(font=("Courier", 25))
    city.grid(column=1, row=0, sticky='nsew')

# adds the image to the label
def getWeatherImage(image, frame):
    imgByte = urlopen(image).read()
    dataStream = io.BytesIO(imgByte)
    imgObj = Image.open(dataStream)
    imgObj = imgObj.resize((150, 150), Image.ANTIALIAS)
    weatherImg = ImageTk.PhotoImage(imgObj)
    img = Label(frame, bg="white")
    img.config(image=weatherImg)
    img.image = weatherImg
    img.grid(column=1, row=3, sticky="nsew")

# gets the date
def getDate(frame):
    now = datetime.datetime.now()
    date = Label(frame, text=now.strftime("%Y-%m-%d"), bg='white')
    date.config(font=('Courier', 12))
    date.grid(column=1, row=1, sticky='nsew')

# enables scrolling
def onFrameConfigure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))
