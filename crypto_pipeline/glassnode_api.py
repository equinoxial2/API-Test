"""Wrapper around Glassnode API."""
import logging
from datetime import datetime
from typing import Any

import pandas as pd

from .config import GLASSNODE_KEY
from .utils import request_api

logger = logging.getLogger(__name__)

BASE_URL = "https://api.glassnode.com/v1/metrics"


def fetch_glassnode_metric(metric: str, asset: str, start: datetime, interval: str = "24h") -> pd.DataFrame:
    """Fetch a Glassnode metric and return as DataFrame."""
    endpoint = f"{BASE_URL}/{metric}"
    params = {
        "a": asset,
        "api_key": GLASSNODE_KEY,
        "i": interval,
        "s": int(start.timestamp())
    }
    logger.info("Fetching Glassnode metric %s for %s", metric, asset)
    data = request_api(endpoint, params=params)
    df = pd.DataFrame(data)
    if not df.empty:
        df["t"] = pd.to_datetime(df["t"], unit="s")
        df.set_index("t", inplace=True)
    return df
