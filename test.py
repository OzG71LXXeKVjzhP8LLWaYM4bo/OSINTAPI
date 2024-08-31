import requests

#r = requests.post("http://localhost:5001/startscan", json  = {"scanname": "test", "scantarget": "blackhumor.today", "usecase": "Passive", "modulelist": "", "typelist": ""})
r = requests.get("http://localhost:5000/api/v2/scanners", headers = {"content-type": "application/json"})

print(r.text)
