from fastapi import FastAPI
import asyncio
from background.generator import run_ai_product_generator

app = FastAPI()

@app.on_event("startup")
async def load_quantum_engine():
    asyncio.create_task(run_ai_product_generator())
