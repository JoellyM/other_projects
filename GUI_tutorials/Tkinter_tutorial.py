import tkinter as tk
import requests
from PIL import ImageTk, Image

HEIGHT=500
WIDTH=600

#api.openweathermap.org/data/2.5/weather?q={city name}
# fa1f5a22d10041b7400c96aeb391720d

def get_weather(city):
    weather_key = 'fa1f5a22d10041b7400c96aeb391720d'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params ={'APPID': weather_key, 'q': city, 'units': 'Celsius'}
    response = requests.get(url, params=params)
    weather = response.json()
    label['text'] =format_response(weather)


def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str ='City: %s \nConditions: %s \nTemperature (°C): %s' %(name, desc, temp)
    except:
        final_str ='There Was a problem retrieving that information'

    return final_str


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image= ImageTk.PhotoImage(Image.open('landscape.jpg'))
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1,relheight=1)

frame = tk.Frame(root, bg='#ffc266', bd=5)
frame.place(relx= 0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather",font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#ffc266', bd=10)
lower_frame.place(relx= 0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font='Time 15 bold', anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()
