"""Fetch Fear & Greed index."""
import logging
from typing import Dict

from .utils import request_api

logger = logging.getLogger(__name__)

URL = "https://api.alternative.me/fng/"


def fetch_fear_greed() -> Dict:
    """Return the current Fear & Greed index."""
    logger.info("Fetching Fear & Greed index")
    data = request_api(URL)
    if "data" in data and data["data"]:
        return data["data"][0]
    return data
