
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)


DATA_PATH = "data/multi_stock_ml_dataset.csv"

FEATURES = [
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


def get_ml_analysis(symbol=None):

    # Load multi-stock dataset
    data = pd.read_csv(DATA_PATH)

    # Filter selected stock
    if symbol:
        stock_data = data[data["Symbol"] == symbol]

        if len(stock_data) >= 20:
            data = stock_data

    X = data[FEATURES]
    y = data["Target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        shuffle=False
    )

    models = {
        "Random Forest": RandomForestClassifier(
            n_estimators=100,
            random_state=42
        ),

        "Decision Tree": DecisionTreeClassifier(
            random_state=42
        ),

        "Logistic Regression": LogisticRegression(
            max_iter=1000
        )
    }

    model_results = []

    for name, model in models.items():

        model.fit(X_train, y_train)
        prediction = model.predict(X_test)

        model_results.append({
            "model": name,
            "accuracy": round(
                accuracy_score(y_test, prediction) * 100, 2
            ),
            "precision": round(
                precision_score(
                    y_test, prediction, zero_division=0
                ) * 100, 2
            ),
            "recall": round(
                recall_score(
                    y_test, prediction, zero_division=0
                ) * 100, 2
            ),
            "f1_score": round(
                f1_score(
                    y_test, prediction, zero_division=0
                ) * 100, 2
            ),
            "confusion_matrix": confusion_matrix(
                y_test, prediction
            ).tolist()
        })

    # Feature importance for selected stock's Random Forest
    rf_model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    rf_model.fit(X_train, y_train)

    feature_results = []

    for feature, value in zip(
        FEATURES,
        rf_model.feature_importances_
    ):
        feature_results.append({
            "feature": feature,
            "importance": round(float(value), 4)
        })

    feature_results.sort(
        key=lambda x: x["importance"],
        reverse=True
    )

    return {
        "model_comparison": model_results,
        "feature_importance": feature_results,
        "symbol": symbol
    }