import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)


# ==============================
# LOAD DATASET
# ==============================

data = pd.read_csv(
    "data/reliance_ml_dataset.csv"
)


# ==============================
# FEATURES
# ==============================

features = [
    "Open",
    "High",
    "Low",
    "Close",
    "Volume",
    "Price_Change",
    "Price_Change_Percent",
    "SMA_5",
    "SMA_10",
    "RSI"
]


X = data[features]
y = data["Target"]


# ==============================
# TRAIN / TEST SPLIT
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    shuffle=False
)


# ==============================
# LOAD TRAINED MODEL
# ==============================

model = joblib.load(
    "models/random_forest_model.pkl"
)


# ==============================
# PREDICTION
# ==============================

y_pred = model.predict(X_test)


# ==============================
# ACCURACY
# ==============================

accuracy = accuracy_score(
    y_test,
    y_pred
)


print("\n================================")
print("MODEL EVALUATION")
print("================================")

print(
    "Model: Random Forest"
)

print(
    "Test Samples:",
    len(X_test)
)

print(
    "Accuracy:",
    round(accuracy * 100, 2),
    "%"
)


# ==============================
# CONFUSION MATRIX
# ==============================

cm = confusion_matrix(
    y_test,
    y_pred
)


print("\n================================")
print("CONFUSION MATRIX")
print("================================")

print(cm)


# ==============================
# CLASSIFICATION REPORT
# ==============================

print("\n================================")
print("CLASSIFICATION REPORT")
print("================================")

print(
    classification_report(
        y_test,
        y_pred
    )
)