"""Generate a small synthetic dataset and save to data/students.csv"""
import pandas as pd
import numpy as np


np.random.seed(42)


def generate(n=400, out_path="../data/students.csv"):
    hours = np.clip(np.random.normal(5, 2, n), 0, 12)
    attendance = np.clip(np.random.normal(75, 15, n), 30, 100)
    prev_grade = np.clip(np.random.normal(60, 20, n), 0, 100)
    sleep = np.clip(np.random.normal(7, 1.5, n), 3, 10)
    extra_help = np.random.binomial(1, 0.3, n)


    # Simple rule to create a label with some noise
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
    df.to_csv(out_path, index=False)
    print(f"Saved {n} rows to {out_path}")


if __name__ == "__main__":
    generate(400, "../data/students.csv")