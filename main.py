import tkinter as tk
from weatherfetch import *

# Title for GUI and background
root = tk.Tk() # create main window
root.title("WeatherFetch")
root.configure(background="lightblue")

# Size of the window
root.minsize(300, 300)
root.maxsize(300, 300)
root.geometry("300x360+50+50")

# Words within GUI
tk.Label(root, font=("Arial", 14, "bold", "underline"), text="Weather Fetch", bg="lightblue", fg="black").pack(pady=5)

tk.Label(root, font=("Arial", 12), text="Type your city of choice here:", bg="lightblue", fg="black").pack(pady=5)

entry = tk.Entry() # resize
entry.pack(pady=10)

# StringVar to hold the result text
result_text = tk.StringVar()

def submit_location():
    user_input = entry.get()
    print(f"Location submitted, User entered: {user_input}")
    city_name = user_input
    weather_data = fetch_weather(city_name)
    text_box_string = display_weather_info(weather_data)
    result_text.set(text_box_string) # Update StringVar with the result text

# Submit button to submit the location
submit = tk.Button(root, font=("Arial", 12), text="Submit", bg="skyblue", fg="black", command=submit_location)
submit.pack(pady=5)

# Result label to display fetched data
result_label = tk.Label(root, font=("Arial", 12, "bold"), textvariable=result_text, justify="left", bg="lightblue", fg="black", wraplength=300)
result_label.pack()

root.mainloop()