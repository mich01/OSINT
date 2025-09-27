import requests

response = requests.get('https://api.publicapis.org/entries')
data = response.json()
for tweet in data['entries']:
    print(tweet['API'])
