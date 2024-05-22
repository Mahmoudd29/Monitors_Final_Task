from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

@app.route('/data', methods=['POST'])
def receive_data():
    try:
        data = request.json
        app.logger.info(f"Received data: {data}")
        
        # Perform any necessary processing with the data here
        
        return jsonify({"status": "received"})
    except Exception as e:
        app.logger.error(f"Error processing request: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/', methods=['GET'])
def index():
    return "Hello, this is your Flask app running on Vercel!"

if __name__ == "__main__":
    app.run(debug=True)
