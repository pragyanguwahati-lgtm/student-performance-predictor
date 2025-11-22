import pandas as pd
from pathlib import Path
DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "students.csv"
def load_data(path: str = None):
    p = path or DATA_PATH
    df = pd.read_csv(p)
    return df