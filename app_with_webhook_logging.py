from flask import Flask, request, jsonify
from datetime import datetime
import json

app = Flask(__name__)

# Set your secret key here
SECRET_KEY = "123456789123456789"
LOG_FILE = "webhook_log.jsonl"

# Simple expected payload schema (can be extended)
REQUIRED_FIELDS = {"event", "user", "status"}

@app.route("/")
def home():
    return "Hello from Flask via Ngrok!"

@app.route("/webhook", methods=["POST"])
def webhook():
    # Step 1: Authenticate using custom header
    auth_header = request.headers.get("X-Webhook-Secret")
    if auth_header != SECRET_KEY:
        return jsonify({"error": "Unauthorized"}), 401

    # Step 2: Parse JSON
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    # Step 3: Validate required fields
    missing_fields = REQUIRED_FIELDS - data.keys()
    if missing_fields:
        return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

    # Step 4: Log the payload
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "data": data
    }
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log_entry) + "\n")

    # Step 5: Respond to sender
    print("✅ Webhook received:", data)
    return jsonify({"status": "received", "data": data}), 200

if __name__ == "__main__":
    app.run(port=5000)
