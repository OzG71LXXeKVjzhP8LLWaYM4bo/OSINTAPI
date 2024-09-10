import requests
import json

def get_scan_summary(scan_id):
    scan_summary_url = "https://vitaglow.fit/scansummary"
    scan_summary_data = {
        "id": scan_id,
        "by": "type"
    }
    response = requests.post(scan_summary_url, data=scan_summary_data)
    return response.json()  # Assuming the response is in JSON format

def get_individual(id, name):
    url = "https://vitaglow.fit/scaneventresults"
    data = {
        "id": id,
        "eventType": name
    }
    r = requests.post(url, data = data)
    print(r.json())



def main():
    results = []
    stuff = get_scan_summary("5CDEFFBE")
    
    for a in stuff:
        if a[-1] == "RUNNING":
            pass
        else:
            results.append(a[0])
    
    # Print results only once after the loop finishes
    print(results)
    for a in results:
        get_individual("5CDEFFBE", name = a)

if __name__ == "__main__":
    main()
