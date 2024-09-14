import requests

r = requests.post("https://www.vitaglow.fit/api/ipdata", json = {"ip": "138.130.213.22"})
print(r.text)