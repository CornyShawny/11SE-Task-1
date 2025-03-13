import tkinter as tk
from weatherfetch import *

# title for gui and background
root = tk.Tk() # create main window
root.title("WeatherFetch")
root.configure(background="lightblue")

# size of the window
root.minsize(100, 100)
root.maxsize(500, 500)
root.geometry("300x360+50+50")

# words within gui
tk.Label(root, font=("Lexend"), text="Weather Fetch", bg="lightblue", fg="black").pack()

# frame inside gui
frame = tk.Frame(root, width=250, height=250)
frame.pack(padx=5, pady=5)

# frame inside the frame inside gui
nested_frame = tk.Frame(frame, width=200, height=200, bg="skyblue")
nested_frame.pack(padx=10, pady=10)

tk.Label(root, text="Type your city of choice here:", bg="skyblue", fg="black").pack()

entry = tk.Entry()
entry.pack()

def submit_location():
    user_input = entry.get()
    print(f"Location submitted, User entered: {user_input}")
    city_name = user_input
    weather_data = fetch_weather(city_name)
    display_weather_info(weather_data)

# submit button to submit the location
submit = tk.Button(root, text="Submit", bg="skyblue", fg="black", command=submit_location)
submit.pack()

root.mainloop()