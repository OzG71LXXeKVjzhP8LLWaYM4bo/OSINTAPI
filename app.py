from flask import Flask, jsonify, request
import requests

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

    if not data or 'target' not in data:
        return jsonify({"error": "No target provided"}), 400

    target = data['target']
    # Add your scan logic here
    return jsonify({"message": f"Started scan for {target}"})

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
