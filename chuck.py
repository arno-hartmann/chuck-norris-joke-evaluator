import requests, json

url = requests.get("https://api.chucknorris.io/jokes/random")
text = url.json()

print(type(text))



print(text['value'])

# Gut Schlecht? in Datei schreiben