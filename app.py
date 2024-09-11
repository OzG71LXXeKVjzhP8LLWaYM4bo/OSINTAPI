from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/api/ipdata', methods=['GET'])

def get_data():
    ip_address = request.args.get('ip')

    if not ip_address:
        return jsonify({"error": "No IP address provided"}), 400
    
    url = f"https://freeipapi.com/api/json/{ip_address}"
    response = requests.get(url)
    data = response.json()

    return jsonify(data)

@app.route("/api/startscan", methods = ["POST"])
def start():
    target = requests.args.get("")

    if not target:
        return jsonify({"error": "No target provided"}), 400
    
@app.route("/api/scansummary", methods = ["POST"])
def summary():
    target = requests.args.get("")

    if not target:
        return jsonify({"error": "No IP address provided"}), 400
    
@app.route("/api/scaneventresults", methods = ["POST"])
def eventresults():
    target = requests.args.get("")

    if not target:
        return jsonify({"error": "No IP address provided"}), 400
    
@app.route("/api/get", methods = ["GET"])
def home():
    return jsonify({"success": "api is working"})
    

if __name__ == '__main__':
    app.run(debug=True, host = "localhost", port=5002)