<<<<<<< HEAD
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib
from pathlib import Path
MODEL_PATH = Path(__file__).resolve().parents[1] / "model.joblib"
=======

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
import joblib
from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parents[1] / "model.joblib"

>>>>>>> b41e797168bc72c94ac4f53bad80c415e98473da
def train(X_train, y_train, model_type="logistic"):
    if model_type == "logistic":
        model = LogisticRegression(max_iter=500)
    else:
        model = DecisionTreeClassifier(max_depth=5)
<<<<<<< HEAD
        model.fit(X_train, y_train)
    joblib.dump(model, MODEL_PATH)
    return model
def load_model(path: str = None):
    p = path or MODEL_PATH
    return joblib.load(p)
=======
    model.fit(X_train, y_train)
    joblib.dump(model, MODEL_PATH)
    return model

def load_model(path: str = None):
    p = Path(path) if path else MODEL_PATH
    return joblib.load(p)

>>>>>>> b41e797168bc72c94ac4f53bad80c415e98473da
def predict(model, X):
    return model.predict(X), model.predict_proba(X)
