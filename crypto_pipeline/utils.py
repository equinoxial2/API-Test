import logging
from typing import Any, Dict, Optional
import requests
from tenacity import retry, stop_after_attempt, wait_exponential
from jsonschema import validate

logger = logging.getLogger(__name__)

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
def request_api(endpoint: str, method: str = "GET", params: Optional[Dict[str, Any]] = None,
                payload: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None,
                schema: Optional[Dict[str, Any]] = None) -> Any:
    """Generic API caller with retry and optional schema validation."""
    logger.debug("Requesting %s %s", method, endpoint)
    response = requests.request(method, endpoint, params=params, json=payload, headers=headers, timeout=30)
    response.raise_for_status()
    data = response.json()
    if schema:
        validate(data, schema)
    return data
