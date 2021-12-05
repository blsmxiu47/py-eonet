import requests

events_base = 'https://eonet.gsfc.nasa.gov/api/v3/events'
response = requests.get(events_base, params={'category': 'severeStorms'})
print('GET all severeStorms...')
print(response)
print(response.json())
