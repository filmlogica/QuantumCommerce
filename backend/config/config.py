import os

class Config:
    """Configuration settings for QuantumCommerce."""
    
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "fallback_secret_key_here")  # Flask security key
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///default.db")  # Database connection
    DEBUG = os.getenv("FLASK_DEBUG", "False") == "True"  # Debug mode toggle
    PORT = int(os.getenv("PORT", 8000))  # Render-assigned port

    # AI Model Paths & Settings
    MISTRAL_MODEL_NAME = os.getenv("MISTRAL_MODEL_NAME", "mistralai/Mistral-7B")

    # Payment Gateway Configs
    STRIPE_API_KEY = os.getenv("STRIPE_API_KEY", "your-stripe-key")
    PAYPAL_CLIENT_ID = os.getenv("PAYPAL_CLIENT_ID", "your-paypal-client-id")

# Initialize config instance
config = Config()
