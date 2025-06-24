import pandas as pd
import requests
import requests_mock

from crypto_pipeline.coingecko_api import fetch_prices


def test_fetch_prices():
    with requests_mock.Mocker() as m:
        m.get("https://pro-api.coingecko.com/api/v3/simple/price",
              json={"bitcoin": {"usd": 20000}})
        df = fetch_prices(["bitcoin"], "usd")
        assert isinstance(df, pd.DataFrame)
        assert df.iloc[0, 0] == 20000
