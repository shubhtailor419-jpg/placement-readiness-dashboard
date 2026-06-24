import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

df = pd.read_csv(
    "data/placement_dataset.csv"
)

X = df[
    [
        "CGPA",
        "Python",
        "Communication",
        "SQL",
        "Projects",
        "Internship"
    ]
]

y = df["Placement"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

predictions = model.predict(
    X_test
)

print(
    "Accuracy:",
    accuracy_score(
        y_test,
        predictions
    )
)

print(
    "Precision:",
    precision_score(
        y_test,
        predictions
    )
)

print(
    "Recall:",
    recall_score(
        y_test,
        predictions
    )
)

print(
    "F1 Score:",
    f1_score(
        y_test,
        predictions
    )
)

print(
    confusion_matrix(
        y_test,
        predictions
    )
)

joblib.dump(
    model,
    "model/placement_model.pkl"
)

print("Model Saved")