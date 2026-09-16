import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


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
# MODELS
# ==============================

models = {

    "Random Forest":
        RandomForestClassifier(
            n_estimators=100,
            random_state=42
        ),

    "Decision Tree":
        DecisionTreeClassifier(
            random_state=42
        ),

    "Logistic Regression":
        LogisticRegression(
            max_iter=1000
        )
}


# ==============================
# TRAIN & COMPARE
# ==============================

results = []


print("\n================================")
print("MODEL COMPARISON")
print("================================")


for name, model in models.items():

    print(
        f"\nTraining {name}..."
    )

    model.fit(
        X_train,
        y_train
    )

    prediction = model.predict(
        X_test
    )

    accuracy = accuracy_score(
        y_test,
        prediction
    )

    results.append({
        "Model": name,
        "Accuracy": round(
            accuracy * 100,
            2
        )
    })

    print(
        "Accuracy:",
        round(accuracy * 100, 2),
        "%"
    )


# ==============================
# COMPARISON TABLE
# ==============================

results_df = pd.DataFrame(
    results
)

results_df = results_df.sort_values(
    by="Accuracy",
    ascending=False
)


print("\n================================")
print("FINAL COMPARISON")
print("================================")

print(
    results_df.to_string(
        index=False
    )
)


# ==============================
# BEST MODEL
# ==============================

best_model = results_df.iloc[0]

print("\n================================")
print("BEST MODEL")
print("================================")

print(
    "Model:",
    best_model["Model"]
)

print(
    "Accuracy:",
    best_model["Accuracy"],
    "%"
)