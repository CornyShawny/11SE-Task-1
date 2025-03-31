# Import required modules
import tkinter as tk # Import the tkinter library for GUI
from weatherfetch import * # Import all functions from the weatherfetch module to format weather data
import ttkbootstrap # Import ttkbootstrap for themed widgets

# Title for GUI and background/theme
root = ttkbootstrap.Window(themename="superhero") # Create themed main window
root.title("WeatherFetch")

# Size of the window
root.minsize(300, 300)
root.maxsize(300, 300)
root.geometry("300x360+50+50")

# Words within GUI
ttkbootstrap.Label(root, font="Lexend, 14", text="Weather Fetch").pack(pady=5)
ttkbootstrap.Label(root, font="Lexend, 12", text="Type your city of choice here:").pack(pady=5)

# StringVar to hold the result text
result_text = ttkbootstrap.StringVar()

# Define submit_location to submit the location to the API and return the data
def submit_location(event=None):
    """Submits the location entered by the user and fetches formatted weather data."""
    user_input = entry.get()
    print(f"Location submitted, User entered: {user_input}")
    city_name = user_input
    weather_data = fetch_weather(city_name)
    weather_output = display_weather_info(weather_data)
    result_text.set(weather_output) # Update StringVar with the result text

# Entry/text box
entry = ttkbootstrap.Entry(font="Lexend, 14",)
entry.pack(pady=10)

entry.bind("<Return>", submit_location) # Bind the Enter key to submit_location so it can be submitted without pressing the button

# Submit button to submit the location
submit = ttkbootstrap.Button(root, text="Submit", command=submit_location)
submit.pack(pady=5)

# Result label to display fetched data
result_label = ttkbootstrap.Label(root, font="Lexend, 12", textvariable=result_text, justify="left", wraplength=250)
result_label.pack()

root.mainloop() # Start the GUI event loop