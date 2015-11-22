import datetime

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
print URLAPICall

#You can use the datetime.timedelta() function to subtract or add time to a date. In this case, we'll be subtracting 30 days from the current date to get our start date and then iterating through until the present day. We do that like this start_date = datetime.datetime.now() - datetime.timedelta(days=30). This will subtract 30 days from the current day.
