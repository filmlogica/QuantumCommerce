from .registry import AI_MODEL_REGISTRY
from .usage_tracker import can_call

FALLBACK_MODELS = {
    "gpt-4.1": ["claude-3.7-sonnet", "gemini-2.5-pro"],
    "flux-1.1-pro": ["flux-schnell", "claude-3.5-haiku"],
    "stable-diffusion-core": ["dalle-3", "nova-canvas"]
}

def route_prompt(model_key, prompt, temperature=0.7):
    if not can_call(model_key):
        fallbacks = FALLBACK_MODELS.get(model_key, [])
        for backup in fallbacks:
            if can_call(backup):
                model_key = backup
                break
        else:
            return {"error": f"All models throttled for: {model_key}"}
    
    model = AI_MODEL_REGISTRY.get(model_key)
    headers = {
        "Authorization": f"Bearer {os.getenv(f'{model['provider'].upper()}_API_KEY')}",
        "Content-Type": "application/json"
    }

    response = requests.post(model["endpoint"], headers=headers, json={"prompt": prompt, "temperature": temperature})
    return response.json()
