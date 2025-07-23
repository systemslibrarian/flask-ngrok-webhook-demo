from flask import Flask, request, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)

# ✅ Use environment variable for security; never hardcode secrets in code
SECRET_KEY = os.getenv("WEBHOOK_SECRET_KEY", "changeme")  # Default fallback for dev only
LOG_FILE = "webhook_log.jsonl"

# ✅ Define required fields for webhook validation
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

    # Step 2: Parse JSON from request body
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    # Step 3: Check for any missing required fields
    missing_fields = REQUIRED_FIELDS - data.keys()
    if missing_fields:
        return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

    # Step 4: Log the incoming payload to a local JSONL file
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "data": data
    }
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log_entry) + "\n")

    # Step 5: Return success response to the sender
    print("✅ Webhook received:", data)
    return jsonify({"status": "received", "data": data}), 200

if __name__ == "__main__":
    # Run the Flask server on port 5000
    app.run(port=5000)
