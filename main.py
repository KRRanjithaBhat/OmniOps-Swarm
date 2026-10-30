from fastapi import FastAPI
from sandbox.runner import prepare_git_sandbox, validate_and_finalize_sandbox

# Initialize FastAPI app instance
app = FastAPI(title="OmniOps-Swarm API", version="1.0.0")

@app.get("/")
def read_root():
    return {
        "status": "online",
        "service": "OmniOps Autonomous SRE Swarm",
        "mode": "simulation / active"
    }

@app.post("/webhook")
def handle_webhook(payload: dict):
    # Prepare sandbox and ingest incident payload
    sandbox_status = prepare_git_sandbox()
    return {
        "status": "success",
        "received_payload": payload,
        "sandbox": sandbox_status
    }