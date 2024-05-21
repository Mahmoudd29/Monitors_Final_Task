from flask import Flask, request, jsonify
from collections import defaultdict
import time

app = Flask(__name__)
data_store = defaultdict(list)

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    client_id = data['client_id']
    data_store[client_id].append(data)
    # Limit the store size if necessary to avoid excessive memory use
    if len(data_store[client_id]) > 100:
        data_store[client_id].pop(0)
    return jsonify({"status": "received"})

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data_store)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
