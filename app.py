from flask import Flask, request, jsonify

app = Flask(__name__)

# Store data for demonstration purposes
data_storage = []

@app.route('/data', methods=['POST', 'GET'])
def data():
    if request.method == 'POST':
        data = request.get_json()
        data_storage.append(data)
        return jsonify({'status': 'received'}), 200
    elif request.method == 'GET':
        if data_storage:
            return jsonify(data_storage[-1]), 200
        else:
            return jsonify({'message': 'No data available'}), 200

if __name__ == '__main__':
    app.run()
