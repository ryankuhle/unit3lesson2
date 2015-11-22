import datetime
import requests
from pandas.io.json import json_normalize

#API Key for developer.forecast.io
APIKey = 'b5904cff597e966ee9aa0d32e5a0e569'

#Base API call
BaseAPICall = 'https://api.forecast.io/forecast/' + APIKey

#Dictionary of cities and locations
cities = { "Austin": '30.303936,-97.754355',
           "Chicago": '41.837551,-87.681844',
           "Miami": '25.775163,-80.208615',
           "New York": '40.663619,-73.938589',
           "San Francisco": '37.727239,-123.032229'
         }

#Current time
TimeNow = datetime.datetime.now()
TimeNow = TimeNow.strftime('%Y-%m-%dT%H:%M:%S%z')

URLAPICall = BaseAPICall + '/' + cities['Austin'] + ',' + TimeNow

r = requests.get(URLAPICall)
df = json_normalize(r.json()['daily']['data'])

#print highest temperature today for Austin
print "The high temperature in Austin today will be: %s" % df['temperatureMax']
