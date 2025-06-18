from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class MistralModel:
    def __init__(self, model_name="mistralai/Mistral-7B"):
        """Initialize the Mistral AI model and tokenizer."""
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def generate_text(self, prompt, max_length=200):
        """Generate AI-powered text response."""
        inputs = self.tokenizer(prompt, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model.generate(**inputs, max_length=max_length)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

# Initialize the model for API use
mistral = MistralModel()
