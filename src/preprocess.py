# src/preprocess.py
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
from pathlib import Path

FEATURES = ["study_hours", "attendance_pct", "prev_grade", "sleep_hours", "extra_help"]

def preprocess(df, test_size=0.2, random_state=42, max_retries=5):
    """
    Splits X/y into train/test with stratification to preserve class ratios.
    If a split ends up with only one class in the training set (rare),
    the function will retry with different random_state values up to max_retries times.
    Returns: X_train_scaled, X_test_scaled, y_train, y_test, scaler
    """
    X = df[FEATURES].values
    y = df["passed"].values

    for attempt in range(max_retries):
        rs = random_state + attempt
        try:
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=test_size, random_state=rs, stratify=y
            )
        except ValueError:
            # stratify=y can raise ValueError if one class has too few samples for the split.
            # Fall back to a non-stratified split (but will still check class presence).
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=test_size, random_state=rs
            )

        # Check that y_train contains at least 2 classes
        if len(np.unique(y_train)) >= 2:
            break
        # otherwise try again with a different seed
    else:
        # After retries, still bad: raise informative error
        raise ValueError(
            "Unable to create a train split that contains at least 2 classes. "
            "Try regenerating the dataset with more samples or enable balancing."
        )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler

