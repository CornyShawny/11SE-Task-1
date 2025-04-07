# **11SE Task 1 2025**

### **By Shawn Fan**

# **Requirements Definition**

## **Functional Requirements**
- **Data Retrieval:** What does the user need to be able to view in the system?

The user needs to be able to access and view all of the data from the API, and be able to view the configured dataset. The user should also be able to view errors due to missing data, it should be able to specify whether there is data or not. For example, for an NBA stats database, if the dataset did not include the date-of-birth, then it should say something like N/A, not displaying an error since the information is only unavailable.

- **User Interface:** What is required for the user to interact with the system?

For the user to interact with the system, there must be at least a command-line interface for the UI, which will allow the user to understand what is happening, and be able to use the application without any bugs or problems. The user should be able to use the UI to connect and interact with the API. The UI should also have the correct formatting, be readable and understandable, and be clear and concise to interact with. The program should also be able to configure the dataset for some sections of the dataset, for example, showing the descending order for a chosen row/column.

- **Data Display:** What information does the user need to obtain from the system?

The user needs to be able to obtain selected data from the database, the original data from the database, and any error messages or outputs from unavailable data or bugs, as well as the configured/formatted dataset. The user should also be able to obtain a dataset that is configured to their desire, with the rows and columns they want to see to take in the information provided.

## **Non-Functional Requirements**
- **Performance:** How well does the system need to perform? 

The system needs to be quick and efficient so the sorting and displaying of the data isn't slow. This isn't really hard to achieve as python is a pretty fast programming language, and with the help of other modules, the speed and efficiency can be optimised.

- **Reliability:** How reliable does the system and data need to be?

The system and data should be always reliable as it is only the API that affects reliability since it's out of my control. Unreliable or undeveloped APIs could cause problems in the system, so it is important to avoid them for the reliability of a system and dataset. You can find the API used in this project or other reliable APIs off https://github.com/public-apis/public-apis as it provides a list of good APIs for many different topics.

- **Usability and Accessibility:** How easy to navigate does the system need to be? What instructions will we need for users to access the system?

The system should be concise and efficient, only providing the information that the user specifies. The instructions can be found in the READ.md file contained in this program, providing a guide for how to use it, and how to install the required dependencies.

# **Determining Specifications**
## **Functional Specifications**
What does the system actually NEED to do?

- **User Requirements**

What does the user need to be able to do? List all specifications here. The user must be able to view the data from the API. There will be an input where the user can enter whatever city they want. If the data can be retrieved from the API, it will display the weather info, otherwise it will return an error.

- **Inputs & Outputs**

What inputs will the system need to accept and what outputs will it need to display? It needs to accept the input and requests from the user and display the weather temperatures in their inputted city, including the temperature and weather condition.

- **Core Features**

At its core, what specifically does the program need to be able to do? The program must communicate with the API, retrieve the data and display it.

- **User Interaction**

How will users interact with the system (e.g. command-line, GUI?) and what information will it need to provide to help users navigate? The program will have a command-line UI and it will provide the commands for the API to get the data and information for the user to view

- **Error Handling**

What possible errors could you face that need to be handled by the system? The most probable error would be one where the location is misspelt, or the data is missing for a city, due to the API not including it. To handle the error, the system should output "Error occurred, make sure to check your spelling and try again, if this error persists, the information on your location is unavailable.".

## **Non-Functional Specifications**
What would improve the system but is ultimately not required?

- **Performance**

How quickly should we try to get the system to perform tasks, what efficiency is required to maintain user engagement? How can we ensure our program remains efficient? The system should be very quick, as there is not a lot of processing going on. It should be quick enough to provide instant information to the user to maintain user engagement. To ensure the program stays efficient, efforts should be made to simplify code.

- **Usability / Accessibility**

How might you make your application more accessible? What could you do with the User Interface to improve usability? The application could be made more accessible by making a more advanced UI system, as it is a bit lacking in detail and some users could not understand how it fully works.

- **Reliability**

What could perhaps not crash the whole system, but could be an issue and needs to be addressed? Data integrity? Duplicate data? API retrieval crash? Most issues would occur on the API's side, like data breaches, missing data, high online traffic or server crashes, but these need to be addressed to the user for them to understand that it's just a API problem, not code or device error.

## **Use Cases**
### **Data Retrieval**
**Use Case:** Retrieve Current Weather Data

**Actors:** User(Meteorologist/Everyday person)

**Preconditions:** Weather API is functional and accessible. User provides a valid location input (e.g., city name).

**Main Flow:** 

- User opens the app and inputs a location (e.g., "Sydney").

- System sends a request to the Weather API with the specified location.

- Weather data (e.g., temperature, weather condition) and location data (e.g. region, country) is retrieved from the API.

- System displays the weather and location data to the user.

**Postconditions:** User views current weather details for the specified location, as well as the location data.

### **User Interface**
**Use Case:** Weather Data UI

**Actors:** User(Meteorologist/Everyday person)

**Preconditions:** System is operational, with a functional and responsive UI. There is a submit button to submit the city to the API and retrieve the data.

**Main Flow:**

- User enters a city name into the text box.

- User clicks on the submit button and sends a request to the Weather API with the specified location.

- Weather data (e.g., temperature, weather condition) and location data (e.g. region, country) is retrieved from the API.

- System displays the weather and location data to the user.

**Postconditions:** User views weather and location data.

### **Data Display:**
**Use Case:** View Weather with Error Handling

**Actors:** User(Meteorologist/Everyday person)

**Preconditions:** Weather API is able to provide forecast data. System is equipped to handle cases of missing data or API unavailability.

**Main Flow:**

- User enters a city name into the text box.

- User clicks on the submit button and sends a request to the Weather API with the specified location.

- Weather data (e.g., temperature, weather condition) and location data (e.g. region, country) is retrieved from the API.

- If weather data is missing, return an error message.

- System displays the weather and location data, or the error message to the user.

**Postconditions:** User views weather and location data.

# **Design**
## **Gantt Chart**
![Alt text](images/Gantt%20Chart.png)
## **Structure Chart**
![Alt text](images/Structure%20Chart.png)
## **Algorithms**
### **Pseudocode**
**Main()**
```
BEGIN root.mainloop()
WHILE window open
    INPUT user_input
    IF API Request Valid THEN
        Fetch City Weather 
        Display Weather Info
    ELSE
        OUTPUT "Error retrieving weather data."
    ENDIF
    ENDWHILE
END root.mainloop()
```
```
BEGIN fetch_weather()
fetch weather_data from API
RETURN weather_data
END fetch_weather()
```
```
BEGIN display_weather_info()
IF weather_data exists THEN
    fetch location, region, country, temperature, condition from weather_data
    weather_output = location, region, country, temperature, condition
    RETURN weather_output
ELSE
    RETURN "Error retrieving weather data."
ENDIF
END display_weather_info()
```
### **Flowchart**
**root.mainloop()**
![alt text](<images/Flow Chart root.mainloop().png>)

**fetch_weather()**
![alt text](<images/Flow Chart fetch_weather().png>)

**display_weather_info()**
![alt text](<images/Flow Chart display_weather_info().png>)

## **Data Dictionary**
| Variable | Data Type | Format for Display | Size in Bytes | Size for Display | Description | Example | Validation |
| -------- | --------- | ------------------ | ------------- | ---------------- | ----------- | ------- | ---------- |
| city_name | String | Text | 100 | 100 | City name to fetch weather for | Gosford | Must be a non-empty string |
| weather_data | String | Text | 250 | 250 | Data fetched from API for chosen city | Weather in Gosford, New South Wales, Australia: Temperature: 17.2C Condition: Sunny| Must be a non-empty string|
# **Development**
## **main.py**
```
# Import required modules
import tkinter as tk # Import the tkinter library for GUI
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

# Entry/text box
entry = ttkbootstrap.Entry(font="Lexend, 14",)
entry.pack(pady=10)

root.mainloop() # Start the GUI event loop
```
## **weatherfetch.py**
```
# Import the requests library to handle HTTP requests
import requests

# API key for WeatherAPI (must be filled in to work)
api_key = "3b693e765bc04767924231518250903"

# Base URL for WeatherAPI
base_url = "http://api.weatherapi.com/v1"

def fetch_weather(city_name):
    """
    Fetches the current weather data for a given city using WeatherAPI.
    """
    # Construct the complete API request URL
    complete_url = f"{base_url}/current.json?key={api_key}&q={city_name}"

    # Send an HTTP GET request to the API
    response = requests.get(complete_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Return the JSON response as a Python dictionary
        return response.json()
    else:
        # Return None if there was an error with the request
        return None
    
def display_weather_info(weather_data):
    """
    Displays weather information from the API response.
    """
    if weather_data:
        # Extract relevant data from the API response
        location = weather_data["location"]["name"]  # City name
        region = weather_data["location"]["region"]  # Region/State
        country = weather_data["location"]["country"]  # Country
        temperature = weather_data["current"]["temp_c"]  # Temperature in Celsius
        condition = weather_data["current"]["condition"]["text"]  # Weather condition (e.g., Sunny, Rainy)
        weather_output = (f"Weather in {location}, {region}, {country}: \n"
                          f"Temperature: {temperature}°C \nCondition: {condition}") # Formatted weather information
        return weather_output # Return the formatted weather information
    else:
        # Print an error message if data could not be retrieved
        return("Error retrieving weather data.")
```
# **Integration**
## **main.py**
```
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
```
# **Testing and Debugging**
**Note:** These are just rewrites of the GitHub Commits, please disregard the original ones on GitHub as they aren't really in-depth.

## **March 10 - Import Module and Base GUI**
Created a simple base for the GUI using tkinter in main.py, and created a module for the weather fetch app (`weatherfetch.py`). Both the module and main code work well and had no problems while testing. Hopefully the module can be integrated into the GUI next lesson, and the GUI could also be improved on.

## **March 11 - Tweak GUI**
Imported the weatherfetch module, changed up the colours and font as well as the size of the GUI, also integrated the module into main.py through the function `submit_location()` and added an entry box into the GUI. Everything other than the font works in the code, but improvements need to be made to `submit_location()` so that it displays on the GUI (because it currently displays in the console/terminal).

## **March 17 - Experimenting with Code**
Changed up the `submit_location()` function (from `main.py`) and the `display_weather_info()` function (from `weatherfetch.py`) to integrate the output into the GUI through a string variable. This change was successful and had no problems while running it. Though, improvements need to be made on the look/aesthetic on the GUI.

## **March 19 - Touch Up**
Touched up on the code comments, messed with the font and colours for some labels (text) within the GUI, formatted the output info, and uncommented + changed a piece of code to display the output. Overall no problems were faced while running the code, but the colours and font did look a bit ugly, therefore improvements need to be made on the aesthetics of this program.

## **March 24 - Ttkbootstrap**
Implemented `ttkbootstrap`, which adds themes for `tkinter`, changed up most of the text and colours to fit the theme, changed up font as well, also added the ability to submit the text input by pressing enter, instead of clicking on the submit button. The themes work well, and looks great, the submit works, but the fonts still don't work, so maybe it shouldn't be included. Not many things need to be changed as the code is mostly finished now, maybe some touch up.

## **March 31 - Code Comments + DocStrings**
Added and changed some code comments and docstrings for both `main.py` and `weatherfetch.py` as final small touches. Overall everything works and looks well, nothing much to change now that its finished.

# **Installation**
### **requirements.txt**
```
requests
ttkbootstrap
```
### **README.md**
```
# **WeatherFetch**
WeatherFetch is an application which can get weather data from all over the world and display it to you with just a click. All you have to do is type your city into the text box and press submit, then you will be provided with the weather data of your chosen city!

## **Features**
- Fetch weather data based on the user's location or a specified city.
- Display current weather conditions, including temperature and weather description.

## **Requirements**
To run this program, you need to install the following dependencies:
- `requests` to make HTTP requests to the weather API
- `ttkbootstrap` to install tkinter themes

### **Install dependencies**
To install the required dependencies, you can run:
1.  Clone the repository
2.  Install requirements.txt which can be done by typing ``pip install -r requirements.txt`` into the python terminal, which will install all the things you will need to run this program. Also, make sure to check for updates!

```bash
pip install -r requirements.txt

**Note:** If the API key doesn't work, it may be because of the API request limit, so you might have to get your own key and replace the current one. To get an API key, simply go to https://www.weatherapi.com/ and sign up, where you will then be provided your key, which you can use to replace the current one in the code.
```
# **Maintenance**
## **Maintenance Questions**
1. **Explain** how you would handle issues caused by changes to the weather API over time.

The weather API will change over time. This could include changes to where they get their data from, the format of the data, or how the data is processed. If these changes do occur, I will update the code if needed. The API key might expire, so there are instructions in `README.md` where it explains how to get a new API key to replace the current one. If issues persist, this project may need a full rewrite or small changes based on the size of the problem.

2. **Explain** how you would ensure the program remains compatible with new versions of Python and libraries like `requests` and `matplotlib`.

Problems wouldn't happen with python updating as the program should run on all. For `ttkbootstrap`, there shouldn't be the need to update it as it is just themes, but it may have to for compatibility. If any library is outdated, the user can just run `pip install -r requirements.txt` again. If this program is incompatible, changes need to be made to ensure it's compatibility with newer versions.

3. **Describe** the steps you would take to fix a bug found in the program after deployment.

If there is a bug, the steps I would take to fix it is first, test if the bug is a result of the code or the device running it. For device bugs, I would troubleshoot and then try to fix it by changing code to make it compatible with a variety of devices (through testing), and if it was a code bug then I would troubleshoot, and then change what is needed to fix/prevent the bug, and then vigorously test it to ensure that it works well. Lasty, I would release these changes as an update/fix to the code.

4. **Outline** how you would maintain clear documentation and ensure the program remains easy to update in the future.

I would maintain clear documentation of the code through code comments and docstrings as well as GitHub commits to ensure the program is easy to reflect on which results in easier problem-solving/bug-fixing for updates in the future. There is also a READ.ME file which will guide users on how to use the program.

## **Final Evaluation**
1. **Evaluate** the current functionality of the program in terms of how well it addresses the functional and non-functional requirements.


2. **Discuss** areas for improvement or new features that could be added.


3. **Evaluate** how the project was managed throughout its development and maintenance, including your time management and how challenges were addressed during the software development lifecycle.

