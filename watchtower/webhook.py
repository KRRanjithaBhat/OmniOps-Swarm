# watchtower/webhook.py
from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel
import uvicorn
import logging

app = FastAPI(title="OmniOps Watchtower Ingestor")

class IncidentTelemetry(BaseModel):
    event_id: str
    source: str  # e.g., "code_healer", "finops", "repomorph"
    severity: str  # "CRITICAL", "WARNING"
    error_message: str
    stack_trace: str
    target_files: dict  # {"code": "app/api.py", "sql": "migrations/optimize.sql", "infra": "infra/k8s_cluster.tf"}

def trigger_remediation_pipeline(payload: dict):
    """Background task to trigger the Brain & Executor without blocking the API response."""
    from brain.nemotron_engine import query_omniops_brain
    from executor.writer import apply_multi_domain_patches
    from sandbox.runner import prepare_git_sandbox, validate_and_finalize_sandbox

    logging.info(f"🚨 Processing incident {payload['event_id']}...")
    
    # 1. Fetch live AI multi-domain patches
    patches = query_omniops_brain(payload)
    
    # 2. Stage Git sandbox
    prepare_git_sandbox()
    
    # 3. Apply file fixes
    apply_multi_domain_patches(patches, payload.get("target_files", {}))
    
    # 4. Run real validation & rollback if needed
    success = validate_and_finalize_sandbox()
    if success:
        logging.info(f"✅ Incident {payload['event_id']} resolved successfully.")
    else:
        logging.error(f"❌ Incident {payload['event_id']} remediation failed validation. Rolled back.")

@app.post("/api/v1/telemetry")
async def receive_incident(telemetry: IncidentTelemetry, background_tasks: BackgroundTasks):
    """Production endpoint receiving incoming incident payloads."""
    payload = telemetry.dict()
    background_tasks.add_task(trigger_remediation_pipeline, payload)
    return {"status": "accepted", "event_id": telemetry.event_id, "message": "OmniOps agent swarm dispatched."}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)