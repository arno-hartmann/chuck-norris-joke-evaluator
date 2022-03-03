import requests

url = requests.get("https://api.chucknorris.io/jokes/random")
joke = url.json()

print(joke['value'])

# Gut Schlecht? in Datei schreiben