import os
from flask import Flask, jsonify, request
import requests

BINANCE_API_BASE = os.environ.get('BINANCE_API_BASE', 'https://api.binance.com')

app = Flask(__name__)

@app.route('/binance/ping')
def binance_ping():
    url = f"{BINANCE_API_BASE}/api/v3/ping"
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        return jsonify(resp.json())
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/binance/price/<symbol>')
def binance_price(symbol):
    url = f"{BINANCE_API_BASE}/api/v3/ticker/price"
    try:
        resp = requests.get(url, params={'symbol': symbol.upper()}, timeout=5)
        resp.raise_for_status()
        return jsonify(resp.json())
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/binance/depth/<symbol>')
def binance_depth(symbol):
    url = f"{BINANCE_API_BASE}/api/v3/depth"
    limit = request.args.get('limit', '5')
    try:
        resp = requests.get(
            url,
            params={'symbol': symbol.upper(), 'limit': limit},
            timeout=5,
        )
        resp.raise_for_status()
        return jsonify(resp.json())
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/binance/trades/<symbol>')
def binance_trades(symbol):
    url = f"{BINANCE_API_BASE}/api/v3/trades"
    limit = request.args.get('limit', '5')
    try:
        resp = requests.get(
            url,
            params={'symbol': symbol.upper(), 'limit': limit},
            timeout=5,
        )
        resp.raise_for_status()
        return jsonify(resp.json())
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/binance/klines/<symbol>')
def binance_klines(symbol):
    url = f"{BINANCE_API_BASE}/api/v3/klines"
    interval = request.args.get('interval', '1h')
    limit = request.args.get('limit', '500')
    try:
        resp = requests.get(
            url,
            params={'symbol': symbol.upper(), 'interval': interval, 'limit': limit},
            timeout=5,
        )
        resp.raise_for_status()
        return jsonify(resp.json())
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/binance/ticker24hr/<symbol>')
def binance_ticker24hr(symbol):
    url = f"{BINANCE_API_BASE}/api/v3/ticker/24hr"
    try:
        resp = requests.get(
            url,
            params={'symbol': symbol.upper()},
            timeout=5,
        )
        resp.raise_for_status()
        return jsonify(resp.json())
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

