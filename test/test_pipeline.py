from src.data_generator import generate
from src.data_loader import load_data
from src.preprocess import preprocess
from src.model import train
import tempfile
from pathlib import Path
def test_training_runs():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)

        # Generate small temporary dataset
        csv_path = tmp_path / "students.csv"
        generate(50, out_path=str(csv_path))
        # Load
        df = load_data(str(csv_path))
        # Preprocess
        X_train, X_test, y_train, y_test, scaler = preprocess(df)
        # Train
        model = train(X_train, y_train)
        # Basic expected check
        assert model is not None
        assert len(X_train) > 0