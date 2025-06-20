from fastapi import FastAPI
import asyncio
from background.generator import run_ai_product_generator

# 🔁 Self-ping imports
import threading, time, requests

app = FastAPI()

@app.on_event("startup")
async def load_quantum_engine():
    # Start background AI engine
    asyncio.create_task(run_ai_product_generator())

    # 🔁 Start self-pinging thread
    threading.Thread(target=ping_self, daemon=True).start()

# 🔁 Self-ping function (every 5 minutes)
def ping_self():
    while True:
        try:
            requests.get("https://quantumcommerce.onrender.com/")
        except Exception:
            pass
        time.sleep(300)
