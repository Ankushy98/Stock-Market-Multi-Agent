import pandas as pd


# ==============================
# LOAD STOCK DATA
# ==============================

data = pd.read_csv(
    "data/reliance_stock_data.csv"
)


# ==============================
# CONVERT NUMERIC COLUMNS
# ==============================

numeric_columns = [
    "Open",
    "High",
    "Low",
    "Close",
    "Volume"
]

for column in numeric_columns:

    data[column] = pd.to_numeric(
        data[column],
        errors="coerce"
    )


data = data.dropna()


# ==============================
# PRICE FEATURES
# ==============================

data["Price_Change"] = (
    data["Close"] - data["Open"]
)

data["Price_Change_Percent"] = (
    data["Price_Change"]
    / data["Open"]
) * 100


# ==============================
# TECHNICAL INDICATORS
# ==============================

# 5-day Simple Moving Average

data["SMA_5"] = (
    data["Close"]
    .rolling(window=5)
    .mean()
)


# 10-day Simple Moving Average

data["SMA_10"] = (
    data["Close"]
    .rolling(window=10)
    .mean()
)


# ==============================
# RSI
# ==============================

delta = data["Close"].diff()

gain = delta.clip(lower=0)

loss = -delta.clip(upper=0)

average_gain = (
    gain
    .rolling(window=14)
    .mean()
)

average_loss = (
    loss
    .rolling(window=14)
    .mean()
)

rs = average_gain / average_loss

data["RSI"] = (
    100 - (100 / (1 + rs))
)


# ==============================
# TARGET
# ==============================

data["Target"] = (
    data["Close"].shift(-1)
    > data["Close"]
).astype(int)


# Remove rows created by indicators
# and final row without next-day target

data = data.dropna()

data = data.iloc[:-1]


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
# SAVE DATASET
# ==============================

prepared_data = data[
    features + ["Target"]
]


prepared_data.to_csv(
    "data/reliance_ml_dataset.csv",
    index=False
)


print("================================")
print("ML DATASET PREPARED")
print("================================")

print(
    "Total Rows:",
    len(prepared_data)
)

print(
    "Total Features:",
    len(features)
)

print("\nFeatures:")

for feature in features:
    print("-", feature)

print(
    "\nDataset saved successfully!"
)

print(
    "data/reliance_ml_dataset.csv"
)