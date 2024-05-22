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
        
        # Check if heart rate is greater than 100
        heart_rate = data.get('heart_rate', 0)
        if heart_rate > 100:
            flag = True
        else:
            flag = False
        
        # Perform any necessary processing with the data here
        
        return jsonify({"status": "received", "data": data, "flag": flag})  # Return the received data and flag in the response
    except Exception as e:
        app.logger.error(f"Error processing request: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/', methods=['GET'])
def index():
    return "Hello, this is your Flask app running on Vercel!"

if __name__ == "__main__":
    app.run(debug=True)
