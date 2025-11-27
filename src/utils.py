<<<<<<< HEAD
"""Utility helper functions for logging and validation."""
import logging
from pathlib import Path

# Configure a simple logger
=======

"""Utilities: logging and helpers"""
import logging
from pathlib import Path

>>>>>>> b41e797168bc72c94ac4f53bad80c415e98473da
LOG_PATH = Path(__file__).resolve().parents[1] / "project.log"
logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

<<<<<<< HEAD
def log(message: str):
    """Log a message to project.log and print it."""
    logging.info(message)
    print(message)

def validate_numeric(value, name):
    """Ensure input values are numeric."""
    try:
        return float(value)
    except ValueError:
        raise ValueError(f"{name} must be a numeric value.")
=======
def log(msg: str):
    logging.info(msg)
    print(msg)
>>>>>>> b41e797168bc72c94ac4f53bad80c415e98473da
