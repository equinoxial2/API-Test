"""APScheduler orchestration for crypto data pipeline."""
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
from pathlib import Path

from apscheduler.schedulers.blocking import BlockingScheduler

from .glassnode_api import fetch_glassnode_metric
from .coingecko_api import fetch_prices
from .sentiment_api import fetch_fear_greed
from .flows_parser import parse_monthly_flows

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(name)s:%(lineno)d %(message)s",
                    handlers=[
                        RotatingFileHandler(
                            "pipeline.log", maxBytes=1000000, backupCount=3
                        ),
                        logging.StreamHandler(),
                    ])

logger = logging.getLogger(__name__)

sched = BlockingScheduler(timezone="Europe/Berlin")
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)


@sched.scheduled_job('cron', hour=1, minute=0)
def job_daily():
    """Daily job to fetch all metrics."""
    today = datetime.utcnow().date().isoformat()
    logger.info("Starting daily job")

    prices = fetch_prices(["bitcoin", "ethereum"], "usd")
    prices.to_csv(DATA_DIR / f"prices_{today}.csv")

    sopr = fetch_glassnode_metric("supply/profit_ratio", "BTC", datetime.utcnow())
    sopr.to_csv(DATA_DIR / f"sopr_{today}.csv")

    sentiment = fetch_fear_greed()
    with open(DATA_DIR / f"sentiment_{today}.json", "w", encoding="utf-8") as f:
        import json
        json.dump(sentiment, f)

    flows_pdf = Path("reports") / "monthly_flows.pdf"
    if flows_pdf.exists():
        flows = parse_monthly_flows(flows_pdf)
        flows.to_csv(DATA_DIR / f"flows_{today}.csv", index=False)
    else:
        logger.warning("Flows PDF %s not found", flows_pdf)

    logger.info("Daily job finished")


if __name__ == "__main__":
    sched.start()
