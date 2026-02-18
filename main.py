from fastapi import FastAPI
from datetime import datetime
import socket
import os

app = FastAPI()
@app.get("/")
def root():
    return {"message": "CloudLab Secure Deployment API", "environment": os.getenv("ENVIRONMENT", "development")}

@app.get("/health")
def health():
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat(), "hostname": socket.gethostname()}