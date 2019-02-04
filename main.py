import requests
import json
import io
import datetime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from urllib.request import urlopen
from module1 import *
from module2 import *

# Binds the canvas to the scroll, and enables mouse scrolling
def onFrameConfigure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))
    canvas.bind_all('<MouseWheel>', lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))

# Creates the GUI window
box = Tk()
box.geometry('410x420')
box.title("Vicky's Weather App")
box["bg"] = "#0000ff"

# Defines and places the notebook widget on the window
nb = ttk.Notebook(box)
nb.grid(row=0, column=0, sticky='NESW')
 
# Adds tab 1 of the notebook and displays location based weather
page1 = ttk.Frame(nb)
nb.add(page1, text='Current City')

# Shows weather based on location
locationFrame = Frame(page1, bg="white")
locationFrame.pack(side="left", fill="both", expand=True)
locationFrame.grid_columnconfigure(1, weight=1)
getLocationWeather("vancouver,ca", locationFrame);

# Below is code for tab 2 content
# Adds tab 2 of the notebook
page2 = ttk.Frame(nb)
nb.add(page2, text='Find a city')
topFrame = Frame(page2, bg='white', pady=10)
topFrame.grid(row=0, column=0, sticky="nsew")
bottomFrame = Frame(page2, bg='white', pady=0)
bottomFrame.grid(row=1, column=0, sticky="nsew")
page2.grid_columnconfigure(0, weight=1)
page2.grid_rowconfigure(0, weight=0)
page2.grid_rowconfigure(1, weight=1)
box.grid_rowconfigure(0, weight=1)
box.grid_columnconfigure(0, weight=1)

# widgets for topFrame
topFrame.grid_rowconfigure(0, weight=0)
topFrame.grid_columnconfigure(0, weight=1)
topFrame.grid_columnconfigure(1, weight=0)
topFrame.grid_columnconfigure(2, weight=0)
topFrame.grid_columnconfigure(3, weight=0)
topFrame.grid_columnconfigure(4, weight=1)
entryLabel = Label(topFrame, text="Enter a city: ")
entryLabel.grid(column=1, row=0)

userEntry = Entry(topFrame, background='white')
userEntry.grid(column=2, row=0)

# when the user hits enter, the getWeather definition will be called
userEntry.bind("<Return>", (lambda event: getWeather(userEntry, resultFrame)))

# when the button is clicked, the getWeather definition will be called
submit = Button(topFrame, text="Submit", command = lambda: getWeather(userEntry, resultFrame))
submit.grid(column=3, row=0)

# widgets for bottomFrame
bottomFrame.grid_propagate(False)

resultContainer = Canvas(bottomFrame, bg="white")
resultContainer.pack(side="left", fill="both", expand=True)

scroll = Scrollbar(bottomFrame, orient="vertical", command=resultContainer.yview)
scroll.pack(side="right", fill="both")
resultContainer.configure(yscrollcommand=scroll.set)
resultFrame = Frame(resultContainer, background="white")

# centers the weather display
resultFrame.grid_columnconfigure(0, weight=1)
resultFrame.grid_columnconfigure(1, weight=0)
resultFrame.grid_columnconfigure(2, weight=0)
resultFrame.grid_columnconfigure(3, weight=1)
resultContainer.create_window((0, 0), window=resultFrame, anchor='center', width=410)
resultFrame.bind("<Configure>", lambda event, canvas=resultContainer: onFrameConfigure(resultContainer))

addCities(resultFrame)

box.update()
box.mainloop()


