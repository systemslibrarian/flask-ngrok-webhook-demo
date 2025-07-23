# Flask + Ngrok Webhook Demo

This project demonstrates how to create a secure Flask webhook endpoint and expose it publicly using [Ngrok](https://ngrok.com/). It includes:

- ✅ JSON payload validation
- 🔐 Header-based secret key authentication
- 📝 Logging of webhook events to a `.jsonl` file
- 🔁 Local development using Ngrok tunnels

---

## 📁 Project Structure

```
flask_ngrok_demo/
├── app_with_webhook_logging.py       # Main Flask app with webhook endpoint
├── webhook_log.jsonl                 # Log file for incoming requests
├── requirements.txt                  # Python dependencies
├── flask_webhook_complete_guide.pdf # PDF instructions for the full setup
└── .gitignore                        # Ignore venv and log files
```

---

## 🚀 Features

- **Webhook Endpoint:** `/webhook` accepts only `POST` requests
- **Header Authentication:** Requires a custom `X-Webhook-Secret` header
- **Field Validation:** Checks for required fields: `event`, `user`, `status`
- **Logging:** Saves all valid payloads to `webhook_log.jsonl`

---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/systemslibrarian/flask-ngrok-webhook-demo.git
cd flask-ngrok-webhook-demo
```

### 2. Create & activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the Flask app

```bash
python app_with_webhook_logging.py
```

### 5. Start an Ngrok tunnel

```bash
ngrok http 5000
```

Copy the HTTPS URL shown by Ngrok (e.g., `https://08ee2615cc86.ngrok-free.app`)

---

## 📬 Testing the Webhook (Postman)

- Method: `POST`
- URL: `https://<your-ngrok-subdomain>.ngrok-free.app/webhook`
- Headers:
  - `Content-Type: application/json`
  - `X-Webhook-Secret: 123456789123456789`
- Body (raw JSON):
```json
{
  "event": "test_event",
  "user": "john_doe",
  "status": "success"
}
```

You should receive a 200 OK with:
```json
{
  "status": "received",
  "data": {
    "event": "test_event",
    "user": "john_doe",
    "status": "success"
  }
}
```

---

## 🛡️ Security Notes

- The `SECRET_KEY` is hardcoded for demo purposes. Use an environment variable or config file for production.
- All requests must include the correct header to be accepted.
- Logged data is saved in newline-delimited JSON (`.jsonl`) format.

---

## 📄 PDF Guide Included

The full step-by-step PDF guide is included as:
- [`flask_webhook_complete_guide_final_cleaned.pdf`](./flask_webhook_complete_guide_final_cleaned.pdf)

---

## 📬 License

MIT License – feel free to use, modify, and share.
