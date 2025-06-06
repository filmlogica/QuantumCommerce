import time

usage_counts = {}
RATE_LIMITS = {
    "gpt-4.1": 500,
    "claude-3.7-sonnet": 800,
    "flux-1.1-pro": 1000,
    "deep-research-2.0": 200,
    # ...add others
}

def can_call(model_key):
    now = int(time.time())
    usage = usage_counts.get(model_key, {"count": 0, "timestamp": now})
    
    # Reset every hour
    if now - usage["timestamp"] > 3600:
        usage_counts[model_key] = {"count": 1, "timestamp": now}
        return True
    
    if usage["count"] < RATE_LIMITS.get(model_key, 100):
        usage_counts[model_key]["count"] += 1
        return True
    return False
