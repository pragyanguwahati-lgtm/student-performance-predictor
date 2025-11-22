# src/data_generator.py
"""Generate synthetic dataset and save to data/students.csv (guarantees at least two classes)."""
import pandas as pd
import numpy as np
from pathlib import Path

np.random.seed(42)

def generate(n=400, out_path=None, ensure_balance=True, min_frac=0.03):
    """
    Generate synthetic dataset and save to out_path (default: data/students.csv).
    ensure_balance=True will enforce that both classes are present; if one class is missing
    it flips up to min_frac of rows to the minority class to ensure at least some samples.
    """
    out_path = Path(out_path) if out_path else Path(__file__).resolve().parents[1] / "data" / "students.csv"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    hours = np.clip(np.random.normal(5, 2, n), 0, 12)
    attendance = np.clip(np.random.normal(75, 15, n), 30, 100)
    prev_grade = np.clip(np.random.normal(60, 20, n), 0, 100)
    sleep = np.clip(np.random.normal(7, 1.5, n), 3, 10)
    extra_help = np.random.binomial(1, 0.3, n)

    # scoring -> probability -> binary label
    score = 0.4 * hours + 0.3 * (attendance / 10) + 0.3 * (prev_grade / 10) + 0.1 * extra_help
    prob = 1 / (1 + np.exp(- (score - 3)))
    label = (prob > 0.5).astype(int)

    df = pd.DataFrame({
        "study_hours": hours,
        "attendance_pct": attendance,
        "prev_grade": prev_grade,
        "sleep_hours": sleep,
        "extra_help": extra_help,
        "passed": label
    })

    # If only one class exists, flip a small fraction to the other class
    if ensure_balance:
        counts = df['passed'].value_counts()
        if counts.size == 1:
            nflip = max(1, int(min_frac * n))
            flip_idx = df.sample(n=nflip, random_state=42).index
            df.loc[flip_idx, 'passed'] = 1 - df.loc[flip_idx, 'passed']
            print(f"[data_generator] Balanced data by flipping {nflip} rows.")
        else:
            # If extremely imbalanced, you could apply more advanced balancing here
            pass

    df.to_csv(out_path, index=False)
    print(f"Saved {n} rows to {out_path}")
    return out_path

if __name__ == "__main__":
    generate(400)
