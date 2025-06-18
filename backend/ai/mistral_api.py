from fastapi import FastAPI, HTTPException
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load Mistral AI model
model_name = "mistralai/Mistral-7B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Initialize FastAPI
app = FastAPI()

@app.post("/generate")
async def generate_text(prompt: str):
    """Generate text using Mistral AI model."""
    try:
        inputs = tokenizer(prompt, return_tensors="pt")
        outputs = model.generate(**inputs, max_length=200)
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return {"response": generated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "Mistral API is running!"}
