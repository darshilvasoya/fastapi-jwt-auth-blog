#!/usr/bin/env bash

# Upgrade pip (optional but recommended)
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Start the FastAPI app
uvicorn main:app --host 0.0.0.0 --port $PORT
