import requests_mock

from crypto_pipeline.sentiment_api import fetch_fear_greed


def test_fetch_fear_greed():
    with requests_mock.Mocker() as m:
        m.get("https://api.alternative.me/fng/", json={"data": [{"value": "50"}]})
        data = fetch_fear_greed()
        assert data["value"] == "50"
