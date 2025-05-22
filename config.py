import json

data = json.load(open('google-services.json'))

f = open(".env", "x")

for key, value in data.items():
    f.write(f"{key.upper()}={value}\n")