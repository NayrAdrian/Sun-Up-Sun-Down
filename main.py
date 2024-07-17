import requests
from datetime import datetime, timedelta, date
from tkinter import *

MY_LAT = 14.612034
MY_LONG = 121.086786


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise_utc = data["results"]["sunrise"]
sunset_utc = data["results"]["sunset"]
today = date.today()


# today = datetime.date.today()  # Get today's date object
# formatted_date = today.strftime("%Y-%m-%d")  # Format the date string

# Convert the UTC times to datetime objects
sunrise_time = datetime.fromisoformat(sunrise_utc)
sunset_time = datetime.fromisoformat(sunset_utc)

# Add 8 hours to convert to GMT+8
sunrise_local = sunrise_time + timedelta(hours=8)
sunset_local = sunset_time + timedelta(hours=8)

# Format the times for display
sunrise_local_str = sunrise_local.strftime('%H:%M:%S')
sunset_local_str = sunset_local.strftime('%H:%M:%S')

# Print the times in the local timezone (for testing purposes)
print("Sunrise (GMT+8):", sunrise_local_str)
print("Sunset (GMT+8):", sunset_local_str)

# Create the main window
window = Tk()
window.title("Sun Up, Sun Down")
window.config(padx=10, pady=10)

canvas = Canvas(width=400, height=400)

website_label = Label(text=f"Sunrise and Sunset ({today} PH)", font=("Arial", 15))
website_label.grid(row=0, column=0)

# Create a frame for the sunrise info
sunrise_frame = Frame(window)
sunrise_frame.grid(row=1, column=0, pady=10)

# Load and display the sunrise image
sunrise_img = PhotoImage(file="sunrise.png")
sunrise_label_img = Label(sunrise_frame, image=sunrise_img)
sunrise_label_img.pack(side=LEFT)

# Display the sunrise time
sunrise_label_time = Label(sunrise_frame, text=sunrise_local_str, font=("Arial", 15))
sunrise_label_time.pack(side=RIGHT)

# Create a frame for the sunset info
sunset_frame = Frame(window)
sunset_frame.grid(row=2, column=0, pady=10)

# Load and display the sunset image
sunset_img = PhotoImage(file="sunset.png")
sunset_label_img = Label(sunset_frame, image=sunset_img)
sunset_label_img.pack(side=LEFT)

# Display the sunset time
sunset_label_time = Label(sunset_frame, text=sunset_local_str, font=("Arial", 15))
sunset_label_time.pack(side=RIGHT)

# Keep a reference to the images to prevent them from being garbage collected
window.sunrise_img = sunrise_img
window.sunset_img = sunset_img

# Run the application
window.mainloop()