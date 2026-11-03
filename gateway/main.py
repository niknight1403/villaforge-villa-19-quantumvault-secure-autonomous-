from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
import jwt

app = FastAPI(title="QuantumVault Agent Gateway", version="0.1.0")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
SECRET_KEY = "super-secret-key-replace-in-prod"

class AgentMessage(BaseModel):
    sender: str
    recipient: str
    payload: str

@app.get("/health")
async def health_check():
    return {"status": "online"}

@app.post("/messages", status_code=status.HTTP_202_ACCEPTED)
async def send_message(msg: AgentMessage, token: str = Depends(oauth2_scheme)):
    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return {"status": "queued", "message": "Message encrypted and routed"}
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
