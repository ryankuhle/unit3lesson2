import datetime
import requests
from pandas.io.json import json_normalize
import sqlite3 as lite

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
#how to call maximum temperature: df['temperatureMax']


def createStorage():
    con = lite.connect('weather.db')
    cur = con.cursor()
    with con:
        cur.execute('CREATE TABLE max_temps (id INT PRIMARY KEY, city TEXT, date TEXT, highTemp NUMERIC)')
    print "TABLE 'max_temps' created in SQLite3 DB 'weather.db'"

createStorage()

#Write a script that takes each city and queries every day for the past 30 days (Hint: You can use the datetime.timedelta(days=1) to increment the value by day)
#Save the max temperature values to the table, keyed on the date. You can leave the date in Unix time or convert to a string.
