"""Parse monthly ETF/ETP flows from PDF."""
import logging
from typing import Union

import pandas as pd
import pdfplumber

logger = logging.getLogger(__name__)


def parse_monthly_flows(pdf_path: Union[str, bytes], page: int = 0) -> pd.DataFrame:
    """Extract flows table from PDF and return as DataFrame."""
    logger.info("Parsing flows from %s page %d", pdf_path, page)
    with pdfplumber.open(pdf_path) as pdf:
        table = pdf.pages[page].extract_table()
    df = pd.DataFrame(table[1:], columns=table[0])
    return df
