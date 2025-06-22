from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API FastAPI de Frédéric"}

@app.get("/price/{symbol}")
def get_price(symbol: str):
    return JSONResponse(content={
        "symbol": symbol.upper(),
        "price": "12345.67"  # mock value
    })
