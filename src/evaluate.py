from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]   # project root

def evaluate(model, X_test, y_test, out_dir=BASE_DIR / "report"):

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    report = classification_report(y_test, preds)
    cm = confusion_matrix(y_test, preds)
    # Save simple text report
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "eval.txt", "w") as f:

        f.write(f"Accuracy: {acc}\n\n")
        f.write(report)
    # Confusion matrix plot
    plt.figure()
    plt.imshow(cm, interpolation='nearest')
    plt.title('Confusion matrix')
    plt.colorbar()
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.savefig(out_dir / "confusion_matrix.png")
    plt.close()
    return acc, report, cm