from flask import Blueprint, request, render_template, session, jsonify
import requests
import os

subscription_bp = Blueprint('subscription_settings', __name__)

BACKEND_URL = os.getenv("BACKEND_URL")

# Subscription Management Page
@subscription_bp.route('/settings', methods=['GET', 'POST'])
def subscription_settings():
    email = session.get('email')
    if not email:
        return render_template("login.html", error="Please log in to manage your subscription.")

    if request.method == 'POST':
        new_tier = request.form.get("new_tier")

        if not new_tier:
            return render_template("subscription.html", error="Please select a valid tier.")

        response = requests.post(f"{BACKEND_URL}/subscription/update", json={"email": email, "new_tier": new_tier})

        if response.status_code == 200:
            return render_template("subscription.html", success="Subscription updated successfully!")
        return render_template("subscription.html", error="Failed to update subscription.")

    # Fetch current subscription details
    response = requests.get(f"{BACKEND_URL}/subscription/details", params={"email": email})

    if response.status_code == 200:
        subscription_data = response.json()
        return render_template("subscription.html", subscription=subscription_data)

    return render_template("subscription.html", error="Subscription details not found.")

# API Endpoint: Fetch Subscription Status
@subscription_bp.route('/api/status', methods=['GET'])
def api_subscription_status():
    email = session.get('email')
    if not email:
        return jsonify(error="User not logged in"), 403

    response = requests.get(f"{BACKEND_URL}/subscription/details", params={"email": email})

    if response.status_code == 200:
        return response.json()
    return jsonify(error="Subscription not found"), 404
