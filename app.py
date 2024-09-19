from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import re

app = Flask(__name__)
CORS(app)

@app.route('/api/ipdata', methods=['POST'])
def get_data():
    data = request.get_json()

    if not data or 'ip' not in data:
        return jsonify({"error": "No IP address provided"}), 400

    ip_address = data['ip']

    url = f"https://freeipapi.com/api/json/{ip_address}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        api_data = response.json()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to fetch IP data: {e}"}), 500

    return jsonify(api_data)

@app.route("/api/startscan", methods=["POST"])
def start_scan():
    data = request.get_json()

    if not data or 'target' not in data:
        return jsonify({"error": "No target provided"}), 400

    target = data['target']
    scanname = data.get('scanname', 'default_scan')
    scantarget = target
    usecase = data.get('usecase', 'default_usecase')
    modulelist = data.get('modulelist', [])
    typelist = data.get('typelist', [])

    url = "https://vitaglow.fit/startscan"
    payload = {
        "scanname": scanname,
        "scantarget": scantarget,
        "usecase": usecase,
        "modulelist": modulelist,
        "typelist": typelist
    }

    try:
        r = requests.post(url, json=payload, headers={'Content-Type': 'application/json'})
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to start scan: {e}"}), 500

    scan_id_match = re.search(r"'id':\s*'([A-F0-9]+)'", r.text)
    if scan_id_match:
        scan_id = scan_id_match.group(1)
        return jsonify({"scanid": scan_id})
    else:
        return jsonify({"message": "There was an error matching IDs"}), 500

@app.route("/api/graph", methods=["POST"])
def graph():
    data = request.get_json()

    if not data or 'target' not in data:
        return jsonify({"error": "No target provided"}), 400

    target = data['target']
    # Add your summary logic here
    return jsonify({"message": f"Summary for {target}"})

@app.route("/api/scaneventresults", methods=["POST"])
def scan_event_results():
    data = request.get_json()

    if not data or 'target' not in data:
        return jsonify({"error": "No target provided"}), 400

    target = data['target']
    scan_summary_url = "https://vitaglow.fit/scansummary"
    scan_summary_data = {
        "id": target,
        "by": "type"
    }

    try:
        response = requests.post(scan_summary_url, json=scan_summary_data)
        response.raise_for_status()
        stuff = response.json()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to get scan summary: {e}"}), 500

    results = []

    for a in stuff:
        if a[-1] == "RUNNING":
            continue
        else:
            results.append(a[0])

    final = []
    for name in results:
        try:
            r = requests.post("https://vitaglow.fit/scaneventresults", json={"id": target, "eventType": name})
            r.raise_for_status()
            final.append(r.json())
        except requests.exceptions.RequestException as e:
            return jsonify({"error": f"Failed to fetch event results: {e}"}), 500

    return jsonify({"Results": final})

@app.route("/api/get", methods=["GET"])
def home():
    return jsonify({"success": "API is working"})

if __name__ == '__main__':
    app.run()
