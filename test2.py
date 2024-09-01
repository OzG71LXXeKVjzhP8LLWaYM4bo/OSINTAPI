import requests

def startscam():
    # Set the URL to your specific endpoint
    r = requests.get("https://www.vitaglow.fit/newscan")
    print(r.json)
    url = "https://www.vitaglow.fit/startscan"

    # Define the scan parameters as JSON data
    data = {
        "scanname": "testing2",
        "scantarget": "vitaglow.fit",
        "usecase": "Passive",
        "modulelist": "",  # List of modules to use (if required)
        "typelist": ""
    }

    # Send the POST request to start the scan
    response = requests.post(url, json=data)

    # Check the response
    if response.status_code == 200:
        result = response.json()
        print("Scan started successfully")
        print(result)
    else:
        print(f"Failed to start scan: {response.status_code}")
        print(response.text)

startscam()