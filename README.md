# python-weather-api

This is sample code for fetching forecast weather data from the National Weather Service using their API. It parses the results as JSON and outputs some forecast information.

Developed in Pycharm CE 2021 with Python 3.8 on macOS.

Requires the packages:

requests
json

The NWS API information is located at: https://weather-gov.github.io/api/general-faqs

The code uses the sample lat-lon provided by the faq (the location of the Washington Monument); you can change this to any other appropriate location.

Note that once you get back the forecast URL (for the sample it's https://api.weather.gov/gridpoints/LWX/96,70/forecast) you can use this in a browser to see what the actual forecast elements are.
