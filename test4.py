import requests
import re
from bs4 import BeautifulSoup

def start_scan(scanname, scantarget, usecase="Passive", modulelist="", typelist=""):
    url = "https://vitaglow.fit/startscan"
    data = {
        "scanname": scanname,
        "scantarget": scantarget,
        "usecase": usecase,
        "modulelist": modulelist,
        "typelist": typelist
    }
    r = requests.post(url, data=data)
    print(r.text)
    return r.text

def extract_scan_id(response_text):
    # Use regex to extract the scan ID from sf.fetchData calls
    scan_id_match = re.search(r"'id':\s*'([A-F0-9]+)'", response_text)
    
    if scan_id_match:
        scan_id = scan_id_match.group(1)
        print(f"Scan ID found: {scan_id}")
        return scan_id
    else:
        print("Scan ID not found")
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
