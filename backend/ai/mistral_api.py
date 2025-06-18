from fastapi import FastAPI, HTTPException
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os
import uvicorn

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8001))  # Default to 8001 if PORT isn't set
    uvicorn.run("backend.ai.mistral_api:app", host="0.0.0.0", port=port)

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
