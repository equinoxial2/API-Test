# API-Test

This repository contains a minimal Flask server that proxies a few Binance API endpoints.

## Setup

1. Create and activate a Python virtual environment (optional but recommended).
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the server:
   ```bash
   python server.py
   ```
   The server listens on port `5000` by default.

## Example Endpoints

- `/binance/ping` – Check connectivity with the Binance API.
- `/binance/price/<symbol>` – Get the latest price for a trading pair (e.g. `BTCUSDT`).
- `/binance/depth/<symbol>` – Get order book data. Optional `limit` query param.
- `/binance/trades/<symbol>` – Get recent trades. Optional `limit` query param.
- `/binance/klines/<symbol>` – Get candlestick data. Optional `interval` and `limit` query params.
- `/binance/ticker24hr/<symbol>` – Get 24‑hour ticker statistics.

You can override the Binance base URL by setting the `BINANCE_API_BASE` environment variable.
