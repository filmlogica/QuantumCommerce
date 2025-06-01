import time
import random

# Simulated performance metrics
metrics = {
    "SEO Traffic": 0,
    "Email Conversions": 0,
    "Affiliate Sign-Ups": 0,
    "Forum Engagements": 0
}

def update_metrics():
    """Randomly updates marketing performance metrics in real time."""
    metrics["SEO Traffic"] += random.randint(50, 200)
    metrics["Email Conversions"] += random.randint(10, 50)
    metrics["Affiliate Sign-Ups"] += random.randint(5, 30)
    metrics["Forum Engagements"] += random.randint(15, 60)

def display_dashboard():
    """Displays live marketing performance summary."""
    print("\n📊 QuantumCommerce.ai Marketing Performance Dashboard")
    print("=" * 50)
    for key, value in metrics.items():
        print(f"{key}: {value}")
    print("=" * 50)

if __name__ == "__main__":
    print("🚀 AI Marketing Dashboard Running... (Live Updates)")
    
    try:
        while True:
            update_metrics()
            display_dashboard()
            time.sleep(10)  # Refresh every 10 seconds
    except KeyboardInterrupt:
        print("\n🛑 AI Marketing Dashboard Stopped.")
