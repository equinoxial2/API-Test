"""Utility and minimal API to query the Binance REST endpoints."""

from fastapi import FastAPI, HTTPException, Request
import requests


BASE_URL = "https://api.binance.com"


def query_binance(path: str, params=None):
    """Send a GET request to Binance API and return the JSON response."""
    url = f"{BASE_URL}{path}"
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


app = FastAPI()


@app.get("/{path:path}")
async def proxy_binance(path: str, request: Request):
    """Proxy GET requests to Binance while preserving query parameters."""
    try:
        data = query_binance(f"/{path}", params=request.query_params)
    except requests.RequestException as exc:  # pragma: no cover - network
        raise HTTPException(status_code=502, detail=str(exc)) from exc
    return data


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python question.py /api/path [key=value ...]")
        sys.exit(1)

    endpoint = sys.argv[1]
    query_params = None
    if len(sys.argv) > 2:
        query_params = dict(param.split("=", 1) for param in sys.argv[2:])

    try:
        result = query_binance(endpoint, params=query_params)
        print(result)
    except Exception as exc:  # pragma: no cover - runtime
        print(f"Error querying Binance: {exc}")