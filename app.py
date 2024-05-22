from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Dictionary to store data for each client
client_data = {
    '1': {'client_id': '1', 'heart_rate': 80, 'timestamp': 1234567890},  # Example data for client 1
    '2': {'client_id': '2', 'heart_rate': 75, 'timestamp': 1234567890},  # Example data for client 2
    '3': {'client_id': '3', 'heart_rate': 85, 'timestamp': 1234567890},  # Example data for client 3
}

@app.route('/data', methods=['POST'])
def receive_data():
    try:
        data = request.json
        app.logger.info(f"Received data: {data}")
        
        # Extract client ID from the data
        client_id = data.get('client_id')
        
        # Save data locally for the client
        client_data[client_id] = data
        
        # Perform any necessary processing with the data here
        
        return jsonify({"status": "received", "data": data})
    except Exception as e:
        app.logger.error(f"Error processing request: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/client/<client_id>', methods=['GET'])
def get_client_data(client_id):
    try:
        # Check if data exists for the client
        if client_id in client_data:
            return jsonify({"status": "success", "data": client_data[client_id]})
        else:
            return jsonify({"status": "error", "message": f"No data found for client with ID: {client_id}"}), 404
    except Exception as e:
        app.logger.error(f"Error retrieving client data: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/', methods=['GET'])
def index():
    return "Hello, this is your Flask app running on Vercel!"

if __name__ == "__main__":
    app.run(debug=True)
