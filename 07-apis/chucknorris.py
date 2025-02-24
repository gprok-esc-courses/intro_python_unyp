import requests 
import json 

response = requests.get('https://api.chucknorris.io/jokes/random')

data = json.loads(response.text)
print(data['value'])