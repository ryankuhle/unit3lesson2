import datetime
import requests
import sqlite3 as lite
from pandas.io.json import json_normalize
import json

API_KEY = 'b5904cff597e966ee9aa0d32e5a0e569'
API_CALL = 'https://api.forecast.io/forecast/' + API_KEY + '/'

cities = { "austin": '30.303936,-97.754355',
           "chicago": '41.837551,-87.681844',
           "miami": '25.775163,-80.208615',
           "new_york": '40.663619,-73.938589',
           "san_francisco": '37.727239,-123.032229'
         }

END_DATE = datetime.datetime.now()
QUERY_DATE = END_DATE - datetime.timedelta(days=30)

con = lite.connect('weather.db')
cur = con.cursor()
cities.keys()

#with con:
#    cur.execute('CREATE TABLE daily_temp ( day_of_reading INT, austin REAL, chicago REAL, miami REAL, new_york REAL, san_francisco REAL);')

#with con:
#    while QUERY_DATE < END_DATE:
#        cur.execute("INSERT INTO daily_temp(day_of_reading) VALUES (?)", (int(QUERY_DATE.strftime('%s')),))
#        QUERY_DATE += datetime.timedelta(days=1)

for k,v in cities.iteritems():
    QUERY_DATE = END_DATE - datetime.timedelta(days=30)
    while QUERY_DATE < END_DATE:
        r = requests.get(API_CALL + v + ',' +  QUERY_DATE.strftime('%Y-%m-%dT12:00:00'))
        with con:
            cur.execute('UPDATE daily_temp SET ' + k + ' = ' + str(r.json()['daily']['data'][0]['temperatureMax']) + ' WHERE day_of_reading = ' + QUERY_DATE.strftime('%s'))
        QUERY_DATE += datetime.timedelta(days=1)

con.close()
