from flask import Flask, request, jsonify
from flask_redis import FlaskRedis
import logging
import json

app = Flask(__name__)
app.config['REDIS_URL'] = "redis-13848.c15.us-east-1-4.ec2.redns.redis-cloud.com:13848"  # Update with your Redis configuration if needed
redis_client = FlaskRedis(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

@app.route('/data', methods=['POST'])
def receive_data():
    try:
        data = request.json
        app.logger.info(f"Received data: {data}")
        
        # Save data to Redis
        client_id = data['client_id']
        redis_client.lpush(f"client:{client_id}:data", json.dumps(data))
        
        return jsonify({"status": "received"})
    except Exception as e:
        app.logger.error(f"Error processing request: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/data/<client_id>', methods=['GET'])
def get_data(client_id):
    try:
        data_list = redis_client.lrange(f"client:{client_id}:data", 0, -1)
        data = [json.loads(item) for item in data_list]
        return jsonify(data)
    except Exception as e:
        app.logger.error(f"Error fetching data: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/', methods=['GET'])
def index():
    return "Hello, this is your Flask app running on Vercel!"

if __name__ == "__main__":
    app.run(debug=True)
