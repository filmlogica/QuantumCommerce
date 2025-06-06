AI_MODEL_REGISTRY = {
    "gpt-4.1": {"provider": "openai", "endpoint": "https://api.openai.com/v1/chat/completions"},
    "claude-3.7-sonnet": {"provider": "anthropic", "endpoint": "https://api.anthropic.com/v1/messages"},
    "gemini-2.5-pro": {"provider": "google", "endpoint": "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"},
    "flux-1.1-pro": {"provider": "ninja", "endpoint": "https://api.myninja.ai/flux"},
    # Add others as needed
}
