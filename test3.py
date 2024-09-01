import requests

r = requests.get("http://ip.vitaglow.fit/api/data?ip=138.130.213.22")

print(r.text)