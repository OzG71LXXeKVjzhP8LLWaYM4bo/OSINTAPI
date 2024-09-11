from flask import Flask, jsonify, request
import requests
import re

app = Flask(__name__)

@app.route('/api/ipdata', methods=['POST'])
def get_data():
    data = request.get_json()

    if not data or 'ip' not in data:
        return jsonify({"error": "No IP address provided"}), 400

    ip_address = data['ip']

    url = f"https://freeipapi.com/api/json/{ip_address}"
    response = requests.get(url)
    api_data = response.json()

    return jsonify(api_data)

@app.route("/api/startscan", methods=["POST"])
def start_scan():
    data = request.get_json()

    # Ensure required fields are provided
    if not data or 'target' not in data:
        return jsonify({"error": "No target provided"}), 400

    target = data['target']
    scanname = data.get('scanname', 'default_scan')  # You can add default values as needed
    scantarget = target
    usecase = data.get('usecase', 'default_usecase')
    modulelist = data.get('modulelist', [])
    typelist = data.get('typelist', [])

    # External scan URL
    url = "https://vitaglow.fit/startscan"
    
    # Prepare the payload for the external request
    payload = {
        "scanname": scanname,
        "scantarget": scantarget,
        "usecase": usecase,
        "modulelist": modulelist,
        "typelist": typelist
    }

    # Send POST request to the external service
    headers = {'Content-Type': 'application/json'}
    r = requests.post(url, json=payload, headers=headers)

    # Try to extract scan ID from the response using regex
    scan_id_match = re.search(r"'id':\s*'([A-F0-9]+)'", r.text)

    if scan_id_match:
        scan_id = scan_id_match.group(1)
        return jsonify({"scanid": scan_id})
    else:
        return jsonify({"message": "There was an error matching IDs"}), 500
    
@app.route("/api/scansummary", methods=["POST"])
def scan_summary():
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
    # Add your event results logic here
    return jsonify({"message": f"Event results for {target}"})

@app.route("/api/get", methods=["GET"])
def home():
    return jsonify({"success": "API is working"})

if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=5002)
