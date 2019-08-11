### Python-Weather-Application

This Application uses API service from OpenWeatherMap and ipinfo. It displays current temperature and weather conditions of any city.


Here Python Library PyQt5 is used to Create the GUI. 
OpenWeatherMap API has been used to get the weather Info.

OpenWeatherMap: https://openweathermap.org/
You can also get your free API Key. Just go to the site, register for API services and get The API key. Add API Key next to '&APPID='.


For Finding the Location of the device, We used IPInfo API to get location from our IP Address.

IPInfo: https://ipinfo.io/
Here also you can get Free API key. Just go to this site and get your API key. Put that next to 'token='.

Then we made use of the gmplot Library to plot the received co-ordinates and plot it on the map. Map is provided by google API although Google API has not been used.

Some Glimpse of GUI have been given in the screenshots folder for the GUI's.

There are Two Sets of UI here. So to run 1st Set of GUI, run the WeatherApp_1.py file. The Screenshots for the same are in Screenshots_1 folder. Another Set of GUI  can be run with WeatherApp_2.py file. The Screenshots for the same are in Screenshots_2 folder.

For running these, you would need to import following libraries:
PyQt5
requests
gmplot
json

If these are not there, this application won't run
