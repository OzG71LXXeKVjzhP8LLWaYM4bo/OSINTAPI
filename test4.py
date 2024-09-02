import requests

r = requests.get("https://vitaglow.fit/static/js/spiderfoot.newscan.js")
print(r.text)
print(r.json)

url = "https://vitaglow.fit/startscan"

    # Define the scan parameters as JSON data
data = {
        "scanname": "testing2",
        "scantarget": "vitaglow.fit",
        "usecase": "Passive",
        "modulelist": "",  # List of modules to use (if required)
        "typelist": ""
    }

    # Send the POST request to start the scan
response = requests.post(url, data=data)
print(response.text)