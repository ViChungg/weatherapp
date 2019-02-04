import requests
import json
import io
import datetime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from urllib.request import urlopen

row = 0
citiesIds = {""}

# reads city IDs from weather.txt and adds the weather for each city in the file.
def addCities(frame):
    with open("weather.txt") as file:
        for line in file:
            citiesIds.add(line.replace("\n", ""))
            print(citiesIds)
    iterCity = iter(citiesIds)
    next(iterCity)
    for city in iterCity:
        getSavedWeather(city, frame)

# displays the weather box on the app
def getWeather(entry, frame):
    api = 'http://api.openweathermap.org/data/2.5/weather?appid=5431043a6fcde69100a7f9f0c48945f2&q='
    city = entry.get()
    data = requests.get(api + str(city) + str('&units=metric')).json()
    try: 
        cityName = json.dumps(data['name']) + ', ' + json.dumps(data['sys']['country'])
        cityID = json.dumps(data['id'])
        temp = 'Temperature: ' + json.dumps(data['main']['temp']) + '°C'
        weather = json.dumps(data['weather'][0]['main'])
        if (cityID in citiesIds):
            messagebox.showinfo('Message', 'City already displayed.')
        else:
            addToFile(cityID)
            citiesIds.add(cityID)
            img = getImage(data['weather'][0]['icon'])
            createNewText(cityName, weather, temp, img, frame)
    except:
        messagebox.showerror("Error", "Could not find city.")

# displays saved weather
def getSavedWeather(cityid, frame):
    api = 'http://api.openweathermap.org/data/2.5/weather?appid=5431043a6fcde69100a7f9f0c48945f2&id='
    data = requests.get(api + str(cityid) + str('&units=metric')).json()
    cityName = json.dumps(data['name']) + ', ' + json.dumps(data['sys']['country'])
    temp = 'Temperature: ' + json.dumps(data['main']['temp']) + '°C'
    weather = json.dumps(data['weather'][0]['main'])
    img = getImage(data['weather'][0]['icon'])
    createNewText(cityName, weather, temp, img, frame)

# creates a new text widget with weather information
def createNewText(name, weather, temp, image, frame):
    global row
    string = name.replace('\"', '') + '\n' + weather.replace('\"', '') + '\n' + temp + '\n'
    try: 
        imgByte = urlopen(image).read()
        dataStream = io.BytesIO(imgByte)
        imgObj = Image.open(dataStream)
        weatherImg = ImageTk.PhotoImage(imgObj)
        img = Label(frame)
        img.config(image=weatherImg)
        img.image = weatherImg
        img.grid(column=1, row=row, sticky="nsew", pady=10)
    except:
        messagebox.showerror("Error", "Could not open image file.")
    result = Label(frame, text=string, padx=10, pady=10, bg="white")
    result.config(font=("Courier", 15))
    result.grid(column=2, row=row, sticky="nsew", pady=10)
    row = row + 2

# gets the icon for the weather
def getImage(icon):
    img = "http://openweathermap.org/img/w/"
    img += icon + '.png'
    return img

def addToFile(cityID):
    f = open("weather.txt", "a")
    f.write(cityID + "\n")

