<<<<<<< HEAD
import argparse
=======

import argparse
from pathlib import Path
import joblib
import numpy as np

>>>>>>> b41e797168bc72c94ac4f53bad80c415e98473da
from src.data_generator import generate
from src.data_loader import load_data
from src.preprocess import preprocess
from src.model import train, load_model, predict
from src.evaluate import evaluate
<<<<<<< HEAD
def run_train(args):
    generate(400, "data/students.csv")
    df = load_data("data/students.csv")
    X_train, X_test, y_train, y_test, scaler = preprocess(df)
=======

SCALER_PATH = Path(__file__).resolve().parents[1] / "scaler.joblib"

def run_train(args):
    # generate dataset and ensure directories
    data_path = generate(400)
    df = load_data(str(data_path))
    X_train, X_test, y_train, y_test, scaler = preprocess(df)
    joblib.dump(scaler, SCALER_PATH)
>>>>>>> b41e797168bc72c94ac4f53bad80c415e98473da
    model = train(X_train, y_train, model_type=args.model)
    acc, report, cm = evaluate(model, X_test, y_test)
    print("Training complete. Accuracy:", acc)

def run_evaluate(args):
<<<<<<< HEAD
    df = load_data("data/students.csv")
    _, X_test, _, y_test, _ = preprocess(df)
=======
    df = load_data()
    X_train, X_test, y_train, y_test, scaler = preprocess(df)
>>>>>>> b41e797168bc72c94ac4f53bad80c415e98473da
    model = load_model()
    acc, report, cm = evaluate(model, X_test, y_test)
    print("Evaluation complete. Accuracy:", acc)

def run_predict(args):
<<<<<<< HEAD
    import numpy as np
    model = load_model()
    # Build a single-row feature vector
    feat = np.array([[args.hours, args.attendance, args.prev_grade, args.sleep,
    args.extra_help]])
    # Note: in a full pipeline you must scale features the same way as training; for simplicity we'll skip scaling here
    pred, prob = predict(model, feat)
    label = 'Pass' if pred[0] == 1 else 'Fail'
    print(f"Prediction: {label} (prob: {prob[0].max():.2f})")
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest='cmd')
    t = sub.add_parser('train')
    t.add_argument('--model', choices=['logistic','tree'], default='logistic')
    e = sub.add_parser('evaluate')
=======
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

>>>>>>> b41e797168bc72c94ac4f53bad80c415e98473da
    p = sub.add_parser('predict')
    p.add_argument('--hours', type=float, required=True)
    p.add_argument('--attendance', type=float, required=True)
    p.add_argument('--prev_grade', type=float, required=True)
    p.add_argument('--sleep', type=float, default=7)
<<<<<<< HEAD
    # fixed: use --extra-help (or --extra_help) and dest extra_help
    p.add_argument('--extra-help', '--extra_help', dest='extra_help', type=int, choices=[0,1], default=0, help="0 = no extra help, 1 = used extra help")
=======
    p.add_argument('--extra-help', '--extra_help', dest='extra_help', type=int, choices=[0,1], default=0)
>>>>>>> b41e797168bc72c94ac4f53bad80c415e98473da

    args = parser.parse_args()
    if args.cmd == 'train':
        run_train(args)
    elif args.cmd == 'evaluate':
        run_evaluate(args)
    elif args.cmd == 'predict':
        run_predict(args)
    else:
<<<<<<< HEAD
        parser.print_help()
=======
        parser.print_help()
>>>>>>> b41e797168bc72c94ac4f53bad80c415e98473da
