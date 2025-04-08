# **WeatherFetch**
WeatherFetch is an application which can get weather data (from https://www.weatherapi.com/) all over the world and display it to you with just a click. All you have to do is type your city into the text box and press submit, then you will be provided with the weather data of your chosen city!

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
```
**Note:** If the API key doesn't work, it may be because of the API request limit, so you might have to get your own key and replace the current one. To get an API key, simply go to https://www.weatherapi.com/ and sign up, where you will then be provided your key, which you can use to replace the current one in the code.