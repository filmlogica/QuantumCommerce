import json
import logging
import requests

AI_MODELS = {
    "gemma3": "https://ai.google.dev/gemma/generate",
    "gemini_flash": "https://ai.google.dev/gemini_flash/generate",
    "gemini_pro": "https://ai.google.dev/gemini_pro/generate"
}

logging.basicConfig(level=logging.INFO)

def fetch_ai_response(prompt, model):
    """Send prompt to AI models and retrieve responses."""
    headers = {"Authorization": f"Bearer {model}"}
    response = requests.post(AI_MODELS[model], json={"prompt": prompt}, headers=headers)
    return response.json()["text"]

def process_responses():
    """Generate responses for all three tiers and merge them."""
    with open("backend/prompts/latest_prompt.json", "r") as file:
        prompts = json.load(file)

    merged_responses = {}

    for tier, prompt in prompts.items():
        responses = {
            "gemma3": fetch_ai_response(prompt, "gemma3"),
            "gemini_flash": fetch_ai_response(prompt, "gemini_flash"),
            "gemini_pro": fetch_ai_response(prompt, "gemini_pro")
        }
        merged_responses[tier] = " ".join(responses.values())  # Merge responses

    with open("backend/prompts/latest_ai_response.json", "w") as file:
        json.dump(merged_responses, file, indent=4)

    logging.info("AI responses processed and merged successfully!")

if __name__ == "__main__":
    process_responses()
