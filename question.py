import requests

BASE_URL = "https://api.binance.com"


def query_binance(path: str, params=None):
    """Send a GET request to Binance API and return the JSON response."""
    url = f"{BASE_URL}{path}"
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


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
    except Exception as exc:
        print(f"Error querying Binance: {exc}")
