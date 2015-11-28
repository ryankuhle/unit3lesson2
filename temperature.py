import datetime
import requests
from pandas.io.json import json_normalize
import sqlite3 as lite

#API Key for developer.forecast.io
APIKey = 'b5904cff597e966ee9aa0d32e5a0e569'

def createStorage():
    con = lite.connect('weather.db')
    cur = con.cursor()
    with con:
        cur.execute('CREATE TABLE max_temps (id INT PRIMARY KEY, city TEXT, date TEXT, highTemp NUMERIC)')
    print "TABLE 'max_temps' created in SQLite3 DB 'weather.db'"

def getMaxTemp(city, date):
    #Takes city name and date as arguments, runs API query, returns Max temperature
    print city

def injectData(city, date, maxTemp):
    #Takes city name, date, temperature as arguments and injects them into max_temps table


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

if table doesn't exist:
    createStorage()

for city in cities:
    for x in range(0, 30):
        #create date string to use
        maxTemp = getMaxTemp(city, date)
        injectData(city, date, maxTemp)

print "Done!"
