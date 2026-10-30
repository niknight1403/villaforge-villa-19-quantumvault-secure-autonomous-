from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

app = FastAPI()

class StorageRequest(BaseModel):
    ciphertext: str
    metadata: str

class AuditRequest(BaseModel):
    prompt: str

@app.get("/")
def read_root():
    return {"status": "running"}

@app.post("/api/v1/storage")
def store_data(request: StorageRequest, x_quantum_key: str = Header(None)):
    if x_quantum_key != "qv_enterprise_secret_key_2026":
        raise HTTPException(status_code=403)
    if not request.ciphertext:
        raise HTTPException(status_code=400)
    return {"status": "stored", "zk_verified": True}

@app.post("/api/v1/audit")
def audit_prompt(request: AuditRequest, x_quantum_key: str = Header(None)):
    if x_quantum_key != "qv_enterprise_secret_key_2026":
        raise HTTPException(status_code=403)
    injection = "Ignore" in request.prompt
    return {"injection_detected": injection, "risk_level": "HIGH" if injection else "LOW"}
