from datetime import datetime, timezone
import pandas as pd
import requests_mock

from crypto_pipeline.glassnode_api import fetch_glassnode_metric


def test_fetch_glassnode_metric():
    with requests_mock.Mocker() as m:
        url = "https://api.glassnode.com/v1/metrics/supply/profit_ratio"
        m.get(url, json=[{"t": 0, "v": 1}])
        df = fetch_glassnode_metric(
            "supply/profit_ratio",
            "BTC",
            datetime.fromtimestamp(0, timezone.utc),
        )
        assert isinstance(df, pd.DataFrame)
        assert df.index[0].timestamp() == 0
        assert df.iloc[0, 0] == 1
