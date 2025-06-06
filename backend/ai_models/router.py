from .registry import AI_MODEL_REGISTRY
import os, requests

def route_prompt(model_key, prompt, temperature=0.7):
    model = AI_MODEL_REGISTRY.get(model_key)
    if not model:
        raise ValueError(f"Model {model_key} not found.")

    headers = {
        "Authorization": f"Bearer {os.getenv(f'{model['provider'].upper()}_API_KEY')}",
        "Content-Type": "application/json"
    }

    payload = {
        "prompt": prompt,
        "temperature": temperature
    }

    response = requests.post(model["endpoint"], headers=headers, json=payload)
    return response.json()
