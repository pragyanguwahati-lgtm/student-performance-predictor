from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib
from pathlib import Path
MODEL_PATH = Path(__file__).resolve().parents[1] / "model.joblib"
def train(X_train, y_train, model_type="logistic"):
    if model_type == "logistic":
        model = LogisticRegression(max_iter=500)
    else:
        model = DecisionTreeClassifier(max_depth=5)
        model.fit(X_train, y_train)
    joblib.dump(model, MODEL_PATH)
    return model
def load_model(path: str = None):
    p = path or MODEL_PATH
    return joblib.load(p)
def predict(model, X):
    return model.predict(X), model.predict_proba(X)
