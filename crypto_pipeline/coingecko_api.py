"""Fetch prices from CoinGecko API."""
import logging
from typing import Iterable

import pandas as pd

from crypto_pipeline.config import COINGECKO_KEY
from crypto_pipeline.utils import request_api

logger = logging.getLogger(__name__)

BASE_URL = "https://pro-api.coingecko.com/api/v3/simple/price"


def fetch_prices(ids: Iterable[str], vs_currency: str = "usd") -> pd.DataFrame:
    """Fetch spot prices for given ids."""
    ids_param = ",".join(ids)
    params = {
        "ids": ids_param,
        "vs_currencies": vs_currency,
        "x_cg_pro_api_key": COINGECKO_KEY,
    }
    logger.info("Fetching CoinGecko prices for %s", ids_param)
    data = request_api(BASE_URL, params=params)
    df = pd.DataFrame(data).T
    df.columns = [f"price_{vs_currency}"]
    return df
