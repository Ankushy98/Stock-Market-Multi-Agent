
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# ==============================
# LOAD MULTI-STOCK DATASET
# ==============================

data = pd.read_csv(
    "data/multi_stock_ml_dataset.csv"
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
# TRAIN TEST SPLIT
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    shuffle=False
)


# ==============================
# RANDOM FOREST
# ==============================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


print("\n================================")
print("TRAINING MULTI-STOCK RANDOM FOREST")
print("================================")

print("Stocks:", data["Symbol"].unique())
print("Training Samples:", len(X_train))
print("Testing Samples:", len(X_test))
print("Total Features:", len(features))


model.fit(X_train, y_train)


# ==============================
# MODEL EVALUATION
# ==============================

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print("Model Accuracy:", round(accuracy * 100, 2), "%")


# ==============================
# SAVE MODEL
# ==============================

model_path = "models/random_forest_model.pkl"

joblib.dump(
    model,
    model_path
)


print("\n================================")
print("MODEL SAVED SUCCESSFULLY")
print("================================")

print("Model:", model_path)
print("Features used:", len(features))