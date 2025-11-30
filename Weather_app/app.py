from tkinter import *
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getWeather():
    city = textfiled.get()
    if not city:
        return

    try:
        # Get location and timezone
        geolocator = Nominatim(user_agent="my_weather_app_12345")
        location = geolocator.geocode(city)
        if not location:
            raise Exception("City not found")
        
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        home = pytz.timezone(result)
        locals_time = datetime.now(home)
        current_time = locals_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # Weather API
        api_key = "84536847961eb0736282139635a62e52"
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        json_data = requests.get(api).json()

        if "weather" not in json_data:
            raise Exception(json_data.get("message", "Weather data not found"))

        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        # Update labels
        t.config(text=f"{temp}°")
        c.config(text=f"{condition} | FEELS LIKE {temp}°")
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception as e:
        # Show error in GUI
        t.config(text="N/A")
        c.config(text="Error")
        w.config(text="...")
        h.config(text="...")
        d.config(text="...")
        p.config(text="...")
        print("Error:", e)

# Search box
Search_image = PhotoImage(file="image4.png")
myimage = Label(image=Search_image)
myimage.place(x=20, y=20)

textfiled = Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfiled.place(x=50, y=40)
textfiled.focus()

Search_icon = PhotoImage(file="search_icon.png")
myimage_icon = Button(root, image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather) 
myimage_icon.place(x=400, y=34)

# Logo image
logo_image = PhotoImage(file="logo.png")
logo = Label(image=logo_image)
logo.place(x=150, y=100)

# Bottom box
Frame_image = PhotoImage(file="box.png")
Frame_myimage = Label(image=Frame_image)
Frame_myimage.pack(padx=5, pady=5, side=BOTTOM)
Frame_myimage.place(x=0, y=350)

# Time
name = Label(root, font=("arial", 15), fg="#fe0202")
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)

# Weather labels
label1 = Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label1.place(x=100, y=400)
label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=220, y=400)
label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=400, y=400)
label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=620, y=400)

t = Label(font=("arial", 70, 'bold'), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("arial", 15, 'bold'))
c.place(x=400, y=250)

# Bottom weather info
w = Label(text="...", font=("arial", 20, 'bold'))
w.place(x=110, y=450)
h = Label(text="...", font=("arial", 20, 'bold'))
h.place(x=270, y=450)
d = Label(text="...", font=("arial", 20, 'bold'))
d.place(x=440, y=450)
p = Label(text="...", font=("arial", 20, 'bold'))
p.place(x=660, y=450)

root.mainloop()
