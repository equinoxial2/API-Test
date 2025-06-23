from unittest import mock
import pandas as pd

from crypto_pipeline.flows_parser import parse_monthly_flows


def test_parse_monthly_flows():
    fake_table = [["col1", "col2"], ["a", "b"]]
    with mock.patch("pdfplumber.open") as m:
        mock_pdf = mock.MagicMock()
        mock_pdf.pages = [mock.MagicMock(extract_table=mock.MagicMock(return_value=fake_table))]
        m.return_value.__enter__.return_value = mock_pdf
        df = parse_monthly_flows("dummy.pdf")
        assert isinstance(df, pd.DataFrame)
        assert list(df.columns) == ["col1", "col2"]
        assert df.iloc[0, 0] == "a"
