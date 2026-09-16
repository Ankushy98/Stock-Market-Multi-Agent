import pandas as pd
import joblib

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


DATA_PATH = "data/reliance_ml_dataset.csv"
MODEL_PATH = "models/random_forest_model.pkl"

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


def get_ml_analysis():

    # Load dataset
    data = pd.read_csv(DATA_PATH)

    X = data[FEATURES]
    y = data["Target"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        shuffle=False
    )

    # Models
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

    model_results = []

    # Evaluate every model
    for name, model in models.items():

        model.fit(X_train, y_train)

        prediction = model.predict(X_test)

        accuracy = accuracy_score(
            y_test,
            prediction
        )

        precision = precision_score(
            y_test,
            prediction,
            zero_division=0
        )

        recall = recall_score(
            y_test,
            prediction,
            zero_division=0
        )

        f1 = f1_score(
            y_test,
            prediction,
            zero_division=0
        )

        matrix = confusion_matrix(
            y_test,
            prediction
        )

        model_results.append({
            "model": name,
            "accuracy": round(accuracy * 100, 2),
            "precision": round(precision * 100, 2),
            "recall": round(recall * 100, 2),
            "f1_score": round(f1 * 100, 2),
            "confusion_matrix": matrix.tolist()
        })

    # Load saved Random Forest
    saved_model = joblib.load(MODEL_PATH)

    # Feature importance
    importance = saved_model.feature_importances_

    feature_results = []

    for feature, value in zip(
        FEATURES,
        importance
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
        "feature_importance": feature_results
    }


if __name__ == "__main__":

    result = get_ml_analysis()

    print("\n========== MODEL PERFORMANCE ==========")

    for item in result["model_comparison"]:

        print("\nModel:", item["model"])
        print("Accuracy:", item["accuracy"], "%")
        print("Precision:", item["precision"], "%")
        print("Recall:", item["recall"], "%")
        print("F1 Score:", item["f1_score"], "%")
        print("Confusion Matrix:")
        print(item["confusion_matrix"])

    print("\n========== FEATURE IMPORTANCE ==========")

    for item in result["feature_importance"]:

        print(
            item["feature"],
            "->",
            item["importance"]
        )