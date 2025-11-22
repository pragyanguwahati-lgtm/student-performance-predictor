
import pandas as pd
from pathlib import Path

def load_data(path: str = None):
    p = Path(path) if path else Path(__file__).resolve().parents[1] / "data" / "students.csv"
    return pd.read_csv(p)
