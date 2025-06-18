from flask import Flask, request, jsonify
import requests
import os
import time
import threading

port = int(os.environ.get("PORT", 8000))  # Default to 8000 if PORT isn't set

app = Flask(__name__)

# Stripe Webhook Handling
@app.route('/stripe/webhook', methods=['POST'])
def stripe_webhook():
    event = request.get_json()
    
    if event['type'] == 'checkout.session.completed':
        process_subscription(event)
    
    return jsonify(success=True)

def process_subscription(event):
    user_tier = event['data']['object']['metadata']['tier']
    user_industry = event['data']['object']['metadata']['industry']

# Scheduled Report Generation
def generate_report(tier, industry):
    google_trends_data = fetch_google_trends(industry)
    yahoo_finance_data = fetch_yahoo_finance(industry)

    report_content = f"Industry: {industry}, Tier: {tier}\n"
    report_content += f"Google Trends: {google_trends_data}\n"
    report_content += f"Yahoo Finance: {yahoo_finance_data}\n"

    store_report(tier, industry, report_content)

def fetch_google_trends(industry):
    return f"Sample trends data for {industry}"

def fetch_yahoo_finance(industry):
    return f"Sample finance data for {industry}"

def store_report(tier, industry, content):
    file_path = f"./reports/{industry}_{tier}.txt"
    with open(file_path, "w") as file:
        file.write(content)

# Dashboard API: Fetch Latest Report
@app.route('/dashboard/report', methods=['GET'])
def get_report():
    industry = request.args.get('industry')
    tier = request.args.get('tier')

    file_path = f"./reports/{industry}_{tier}.txt"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            report = file.read()
        return jsonify(report=report)
    
    return jsonify(error="No report available"), 404

# Render Keep-Alive Endpoint
@app.route('/')
def home():
    return "QuantumCommerce Backend Running!"

@app.route('/ping')
def ping():
    return "Pong!", 200

# Background task to keep Render alive
RENDER_URL = "https://yourappname.onrender.com/ping"  # Replace with actual Render URL
PING_INTERVAL = 840  # Ping every 14 minutes (840 seconds)

def keep_alive():
    while True:
        try:
            response = requests.get(RENDER_URL)
            print(f"Pinged Render at {time.strftime('%Y-%m-%d %H:%M:%S')}: Status {response.status_code}")
        except Exception as e:
            print(f"Error pinging Render: {e}")
        time.sleep(PING_INTERVAL)

# Run pinging script in background
threading.Thread(target=keep_alive, daemon=True).start()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port, debug=True)
