import stripe
from flask import Blueprint, request, jsonify
from backend.database.models import Subscription, User, db
import os

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
webhook_secret = os.getenv("STRIPE_WEBHOOK_SECRET")

stripe_bp = Blueprint('stripe_webhooks', __name__)

# Stripe Webhook Listener
@stripe_bp.route('/webhook', methods=['POST'])
def stripe_webhook():
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get('Stripe-Signature')

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, webhook_secret)
    except ValueError:
        return jsonify(error="Invalid payload"), 400
    except stripe.error.SignatureVerificationError:
        return jsonify(error="Invalid signature"), 400

    handle_event(event)

    return jsonify(success=True)

# Event Handling Logic
def handle_event(event):
    data = event.get("data", {}).get("object", {})
    event_type = event.get("type")

    if event_type == "customer.subscription.created":
        create_subscription(data)

    elif event_type == "customer.subscription.updated":
        update_subscription(data)

    elif event_type == "customer.subscription.deleted":
        cancel_subscription(data)

# Create New Subscription
def create_subscription(data):
    user = User.query.filter_by(email=data["customer_email"]).first()
    if not user:
        return

    subscription = Subscription(
        user_id=user.id,
        stripe_subscription_id=data["id"],
        status=data["status"]
    )

    db.session.add(subscription)
    db.session.commit()

# Update Subscription Details
def update_subscription(data):
    subscription = Subscription.query.filter_by(stripe_subscription_id=data["id"]).first()
    if subscription:
        subscription.status = data["status"]
        db.session.commit()

# Handle Subscription Cancellation
def cancel_subscription(data):
    subscription = Subscription.query.filter_by(stripe_subscription_id=data["id"]).first()
    if subscription:
        subscription.status = "canceled"
        db.session.commit()
