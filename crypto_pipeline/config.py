from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("API_BASE_URL", "")
GLASSNODE_KEY = os.getenv("GLASSNODE_API_KEY", "")
COINGECKO_KEY = os.getenv("COINGECKO_API_KEY", "")
TOKEN = os.getenv("API_TOKEN", "")  # pour health-check

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}
