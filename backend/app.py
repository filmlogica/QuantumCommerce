from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import pandas as pd

app = FastAPI(title="QuantumCommerce Backend API")

# Allow frontend communication
origins = [
    "http://localhost:3000",
    "https://your-site-name.netlify.app"  # Replace with your Netlify URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dummy product listing
products_db = [
    {
        "id": 1,
        "name": "Luxury Smart Watch",
        "price": 1999.00,
        "recurring": True,
        "description": "AI-powered smart device with wellness automation."
    },
    {
        "id": 2,
        "name": "Ergonomic Zero-Gravity Workstation",
        "price": 3799.00,
        "recurring": False,
        "description": "Ultimate productivity pod with postural AI adjustments."
    },
    {
        "id": 3,
        "name": "Signature Subscription Coffee Kit",
        "price": 79.99,
        "recurring": True,
        "description": "Gourmet bean-to-brew box delivered monthly."
    }
]

@app.get("/")
def health_check():
    return {"status": "QuantumCommerce backend is live."}

@app.get("/products", response_model=List[dict])
def get_products():
    return products_db
