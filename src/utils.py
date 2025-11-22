
"""Utilities: logging and helpers"""
import logging
from pathlib import Path

LOG_PATH = Path(__file__).resolve().parents[1] / "project.log"
logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log(msg: str):
    logging.info(msg)
    print(msg)
