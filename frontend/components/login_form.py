from flask import Blueprint, request, render_template, redirect, url_for, session
import requests
import os

login_bp = Blueprint('login_form', __name__)

BACKEND_URL = os.getenv("BACKEND_URL")

# Login Page
@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')

        if not email:
            return render_template('login.html', error="Email required")

        session['email'] = email
        return redirect(url_for('dashboard_home'))

    return render_template('login.html')

# Logout Functionality
@login_bp.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('login'))

# Fetch Subscription Status
@login_bp.route('/subscription/status', methods=['GET'])
def subscription_status():
    email = session.get('email')
    if not email:
        return {"error": "User not logged in"}, 403

    response = requests.get(f"{BACKEND_URL}/subscription/details", params={"email": email})

    if response.status_code == 200:
        return response.json()
    return {"error": "Subscription not found"}, 404
