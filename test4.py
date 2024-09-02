import requests
import re
import json

def start_scan(scanname, scantarget, usecase="Passive", modulelist="", typelist=""):
    url = "https://vitaglow.fit/startscan"
    data = {
        "scanname": scanname,
        "scantarget": scantarget,
        "usecase": usecase,
        "modulelist": modulelist,
        "typelist": typelist
    }
    response = requests.post(url, data=data)
    print(response.json())
    return response.text

def extract_scan_id(response_text):
    match = re.search(r'scanSummaryView\("(\d+)"\)', response_text)
    print(match)
    if match:
        return match.group(1)
    return None

def get_scan_summary(scan_id):
    scan_summary_url = "https://vitaglow.fit/scansummary"
    scan_summary_data = {
        "id": scan_id,
        "by": "type"
    }
    response = requests.post(scan_summary_url, data=scan_summary_data)
    return response.text

def main():
    scanname = "testing2"
    scantarget = "vitaglow.fit"
    
    # Step 1: Start the scan
    response_text = start_scan(scanname, scantarget)
    
    # Step 2: Extract the scan ID
    scan_id = extract_scan_id(response_text)
    if scan_id:
        print(f"Scan ID: {scan_id}")
        
        # Step 3: Get the scan summary
        scan_summary = get_scan_summary(scan_id)
        print(scan_summary)
    else:
        print("Scan ID not found")

if __name__ == "__main__":
    main()
