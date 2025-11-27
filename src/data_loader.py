<<<<<<< HEAD
import pandas as pd
from pathlib import Path
DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "students.csv"
def load_data(path: str = None):
    p = path or DATA_PATH
    df = pd.read_csv(p)
    return df
=======

import pandas as pd
from pathlib import Path

def load_data(path: str = None):
    p = Path(path) if path else Path(__file__).resolve().parents[1] / "data" / "students.csv"
    return pd.read_csv(p)
>>>>>>> b41e797168bc72c94ac4f53bad80c415e98473da
