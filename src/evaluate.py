from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
import os
def evaluate(model, X_test, y_test, out_dir="../report"):
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    report = classification_report(y_test, preds)
    cm = confusion_matrix(y_test, preds)
    # Save simple text report
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "eval.txt"), "w") as f:
        f.write(f"Accuracy: {acc}\n\n")
        f.write(report)
    # Confusion matrix plot
    plt.figure()
    plt.imshow(cm, interpolation='nearest')
    plt.title('Confusion matrix')
    plt.colorbar()
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.savefig(os.path.join(out_dir, "confusion_matrix.png"))
    plt.close()
    return acc, report, cm