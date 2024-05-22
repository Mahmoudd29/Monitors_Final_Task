from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    print(f"Received data: {data}")
    return jsonify({"status": "received"})

@app.route('/', methods=['GET'])
def index():
    return "Hello, this is your Flask app running on Vercel!"

if __name__ == "__main__":
    app.run(debug=True)