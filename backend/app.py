from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Celery Configuration
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

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
    
    # Queue report generation using Celery
    generate_report.delay(user_tier, user_industry)

# Scheduled Report Generation
@celery.task
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

if __name__ == '__main__':
    app.run(debug=True)
