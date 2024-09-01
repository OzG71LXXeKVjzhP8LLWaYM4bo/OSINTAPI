from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask API!"})

@app.route('/api/data', methods=['GET'])
def get_data():
    # Get the IP address from the query parameters
    ip_address = request.args.get('ip')

    # Basic validation for the IP address
    if not ip_address:
        return jsonify({"error": "No IP address provided"}), 400
    
    url = f"https://freeipapi.com/api/json/{ip_address}"


    response = requests.get(url)
    data = response.json()

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
