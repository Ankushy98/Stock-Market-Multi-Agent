import pandas as pd
import joblib


# ==============================
# LOAD MODEL
# ==============================

model = joblib.load(
    "models/random_forest_model.pkl"
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


# ==============================
# GET FEATURE IMPORTANCE
# ==============================

importance = model.feature_importances_


feature_importance = pd.DataFrame({
    "Feature": features,
    "Importance": importance
})


# ==============================
# SORT
# ==============================

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)


# ==============================
# DISPLAY
# ==============================

print("\n================================")
print("FEATURE IMPORTANCE")
print("================================")

for _, row in feature_importance.iterrows():

    print(
        f"{row['Feature']}: "
        f"{row['Importance']:.4f}"
    )