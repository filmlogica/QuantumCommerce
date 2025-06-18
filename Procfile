web: gunicorn backend.app:app --bind 0.0.0.0:$PORT
ai: uvicorn backend.ai.mistral_api:app --host 0.0.0.0 --port 8001
