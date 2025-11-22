
from src.data_generator import generate
from src.data_loader import load_data
from src.preprocess import preprocess
from src.model import train
import tempfile
from pathlib import Path

def test_training_runs():
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        csv_path = tmp_path / "students.csv"
        generate(50, out_path=str(csv_path))
        df = load_data(str(csv_path))
        X_train, X_test, y_train, y_test, scaler = preprocess(df)
        model = train(X_train, y_train)
        assert model is not None
        assert len(X_train) > 0
