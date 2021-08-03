'''
This is sample code for fetching forecast results from the National Weather Service using their API.

References:
https://weather-gov.github.io/api/general-faqs
https://www.askpython.com/python/examples/pull-data-from-an-api
'''

import requests
import json

# Retrieve the metadata for your location with:  https://api.weather.gov/points/{lat},{lon}

latLon = "38.8894,-77.0352" # Sample from faq
requestURL = "https://api.weather.gov/points/" + latLon

print("Requesting metadata...")

response_API = requests.get(requestURL)
print("Response code:", response_API.status_code)

'''
200 : OK. It means we have a healthy connection with the API on web.
204: It depicts that we can successfully made a connection to the API, but did not return any data from the service.
401 : Authentication failed
403 : Access is forbidden by the API service.
404 : The requested API service is not found on the server/web.
500 : Internal Server Error has occurred.
'''

if response_API.status_code != 200:
    print("API call failed")
else:
    dataRaw: str = response_API.text
    print("Response text: " + dataRaw)

    # Parse the data into JSON format
    dataJSON = json.loads(dataRaw)

    # Get the URL for the general forecast
    requestURL = dataJSON['properties']['forecast']

    print("Forecast URL: " + requestURL)

    print("Requesting forecast data...")



    # Roll through the periods, output detailedForecast for each



