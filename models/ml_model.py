import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


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
print("TRAINING RANDOM FOREST")
print("================================")

print(
    "Training Samples:",
    len(X_train)
)

print(
    "Testing Samples:",
    len(X_test)
)

print(
    "Features:",
    len(features)
)


model.fit(
    X_train,
    y_train
)


# ==============================
# PREDICTION
# ==============================

y_pred = model.predict(
    X_test
)


# ==============================
# ACCURACY
# ==============================

accuracy = accuracy_score(
    y_test,
    y_pred
)


print("\n================================")
print("ML MODEL RESULTS")
print("================================")

print(
    "Model: Random Forest"
)

print(
    "Accuracy:",
    round(accuracy * 100, 2),
    "%"
)


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