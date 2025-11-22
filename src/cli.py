
import argparse
from pathlib import Path
import joblib
import numpy as np

from src.data_generator import generate
from src.data_loader import load_data
from src.preprocess import preprocess
from src.model import train, load_model, predict
from src.evaluate import evaluate

SCALER_PATH = Path(__file__).resolve().parents[1] / "scaler.joblib"

def run_train(args):
    # generate dataset and ensure directories
    data_path = generate(400)
    df = load_data(str(data_path))
    X_train, X_test, y_train, y_test, scaler = preprocess(df)
    joblib.dump(scaler, SCALER_PATH)
    model = train(X_train, y_train, model_type=args.model)
    acc, report, cm = evaluate(model, X_test, y_test)
    print("Training complete. Accuracy:", acc)

def run_evaluate(args):
    df = load_data()
    X_train, X_test, y_train, y_test, scaler = preprocess(df)
    model = load_model()
    acc, report, cm = evaluate(model, X_test, y_test)
    print("Evaluation complete. Accuracy:", acc)

def run_predict(args):
    model = load_model()
    scaler = None
    try:
        scaler = joblib.load(SCALER_PATH)
    except Exception:
        pass
    feat = np.array([[args.hours, args.attendance, args.prev_grade, args.sleep, args.extra_help]])
    if scaler is not None:
        feat = scaler.transform(feat)
    pred, prob = predict(model, feat)
    label = 'Pass' if pred[0] == 1 else 'Fail'
    print(f"Prediction: {label} (prob: {prob[0].max():.2f})")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest='cmd')

    t = sub.add_parser('train')
    t.add_argument('--model', choices=['logistic','tree'], default='logistic')

    e = sub.add_parser('evaluate')

    p = sub.add_parser('predict')
    p.add_argument('--hours', type=float, required=True)
    p.add_argument('--attendance', type=float, required=True)
    p.add_argument('--prev_grade', type=float, required=True)
    p.add_argument('--sleep', type=float, default=7)
    p.add_argument('--extra-help', '--extra_help', dest='extra_help', type=int, choices=[0,1], default=0)

    args = parser.parse_args()
    if args.cmd == 'train':
        run_train(args)
    elif args.cmd == 'evaluate':
        run_evaluate(args)
    elif args.cmd == 'predict':
        run_predict(args)
    else:
        parser.print_help()
