import os
import logging
import re
from flask import Flask, jsonify, request
import requests

BINANCE_API_BASE = os.environ.get('BINANCE_API_BASE', 'https://api.binance.com')

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

VALID_INTERVALS = {
    "1m", "3m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "8h", "12h", "1d", "3d", "1w", "1M"
}

def validate_symbol(symbol: str) -> str:
    if not re.fullmatch(r"[A-Za-z0-9]{2,}", symbol):
        raise ValueError("Invalid symbol format")
    return symbol.upper()

def validate_limit(value: str, default: int, max_value: int = 1000) -> int:
    if value is None:
        return default
    try:
        ivalue = int(value)
        if ivalue <= 0 or ivalue > max_value:
            raise ValueError
        return ivalue
    except ValueError:
        raise ValueError(f"limit must be between 1 and {max_value}")

def validate_interval(interval: str) -> str:
    if interval not in VALID_INTERVALS:
        raise ValueError("Invalid interval")
    return interval

@app.route('/binance/ping')
def binance_ping():
    url = f"{BINANCE_API_BASE}/api/v3/ping"
    try:
        app.logger.info("Ping Binance")
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        return jsonify(resp.json())
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/binance/price/<symbol>')
def binance_price(symbol):
    url = f"{BINANCE_API_BASE}/api/v3/ticker/price"
    try:
        symbol = validate_symbol(symbol)
        app.logger.info("Price request for %s", symbol)
        resp = requests.get(url, params={'symbol': symbol}, timeout=5)
        resp.raise_for_status()
        return jsonify(resp.json())
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/binance/depth/<symbol>')
def binance_depth(symbol):
    url = f"{BINANCE_API_BASE}/api/v3/depth"
    limit = request.args.get('limit')
    try:
        symbol = validate_symbol(symbol)
        limit_val = validate_limit(limit, 5, 5000)
        app.logger.info("Depth request for %s limit=%s", symbol, limit_val)
        resp = requests.get(
            url,
            params={'symbol': symbol, 'limit': limit_val},
            timeout=5,
        )
        resp.raise_for_status()
        return jsonify(resp.json())
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/binance/trades/<symbol>')
def binance_trades(symbol):
    url = f"{BINANCE_API_BASE}/api/v3/trades"
    limit = request.args.get('limit')
    try:
        symbol = validate_symbol(symbol)
        limit_val = validate_limit(limit, 5, 1000)
        app.logger.info("Trades request for %s limit=%s", symbol, limit_val)
        resp = requests.get(
            url,
            params={'symbol': symbol, 'limit': limit_val},
            timeout=5,
        )
        resp.raise_for_status()
        return jsonify(resp.json())
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/binance/klines/<symbol>')
def binance_klines(symbol):
    url = f"{BINANCE_API_BASE}/api/v3/klines"
    interval = request.args.get('interval', '1h')
    limit = request.args.get('limit')
    try:
        symbol = validate_symbol(symbol)
        interval = validate_interval(interval)
        limit_val = validate_limit(limit, 500, 1000)
        app.logger.info(
            "Klines request for %s interval=%s limit=%s", symbol, interval, limit_val
        )
        resp = requests.get(
            url,
            params={'symbol': symbol, 'interval': interval, 'limit': limit_val},
            timeout=5,
        )
        resp.raise_for_status()
        return jsonify(resp.json())
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/binance/ticker24hr/<symbol>')
def binance_ticker24hr(symbol):
    url = f"{BINANCE_API_BASE}/api/v3/ticker/24hr"
    try:
        symbol = validate_symbol(symbol)
        app.logger.info("24hr ticker request for %s", symbol)
        resp = requests.get(
            url,
            params={'symbol': symbol},
            timeout=5,
        )
        resp.raise_for_status()
        return jsonify(resp.json())
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

