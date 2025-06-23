"""Simple FastAPI app exposing a /health endpoint."""
from fastapi import FastAPI, Header, HTTPException

from .config import TOKEN

app = FastAPI()

@app.get("/health")
def health(authorization: str | None = Header(default=None)):
    """Return OK if the provided authorization matches TOKEN."""
    if TOKEN and authorization != f"Bearer {TOKEN}":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"status": "ok"}
