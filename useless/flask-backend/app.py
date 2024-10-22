from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({'message': 'Hello from Flask!'})

@app.route('/api/submit', methods=['POST'])
def submit_data():
    data = request.json
    print("Received data:", data)
    return jsonify({'status': 'success', 'message': 'Data received successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
