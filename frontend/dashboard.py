from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

BACKEND_URL = os.getenv("BACKEND_URL")

# Dashboard Homepage
@app.route('/')
def dashboard_home():
    return render_template("dashboard.html")

# Fetch Latest Report
@app.route('/report', methods=['GET'])
def get_report():
    industry = request.args.get("industry")
    tier = request.args.get("tier")

    if not industry or not tier:
        return jsonify(error="Industry and tier required"), 400

    response = requests.get(f"{BACKEND_URL}/dashboard/report", params={"industry": industry, "tier": tier})

    if response.status_code == 200:
        return jsonify(response.json())
    return jsonify(error="No report available"), 404

# Subscription Management (Stripe Integration)
@app.route('/subscription', methods=['GET'])
def subscription_details():
    user_email = request.args.get("email")

    if not user_email:
        return jsonify(error="Email required"), 400

    response = requests.get(f"{BACKEND_URL}/subscription/details", params={"email": user_email})

    if response.status_code == 200:
        return jsonify(response.json())
    return jsonify(error="Subscription not found"), 404

# Allow Users to Update Subscription Tier
@app.route('/subscription/update', methods=['POST'])
def update_subscription():
    data = request.get_json()
    email = data.get("email")
    new_tier = data.get("new_tier")

    if not email or not new_tier:
        return jsonify(error="Email and new tier required"), 400

    response = requests.post(f"{BACKEND_URL}/subscription/update", json={"email": email, "new_tier": new_tier})

    if response.status_code == 200:
        return jsonify(response.json())
    return jsonify(error="Failed to update subscription"), 400

if __name__ == '__main__':
    app.run(debug=True)
