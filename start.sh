#!/usr/bin/env bash
# Install dependencies in Render's Python environment
pip install --upgrade pip
pip install -r requirements.txt

# Start the FastAPI app
uvicorn main:app --host 0.0.0.0 --port $PORT
