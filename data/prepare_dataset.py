
import pandas as pd
import yfinance as yf
import sys


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



def prepare_stock_data(symbol):

    print(f"\nDownloading data for {symbol}...")

    try:

        data = yf.download(
            symbol,
            period="2y",
            auto_adjust=False,
            progress=False
        )

        if data.empty:
            print(f"⚠️ No data found for {symbol}")
            return None

        # Handle MultiIndex columns
        if isinstance(data.columns, pd.MultiIndex):
            data = data.xs(
                symbol,
                axis=1,
                level="Ticker"
            )

        data = data.reset_index()

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

        data = data.dropna(
            subset=numeric_columns
        )

        data["Price_Change"] = (
            data["Close"] - data["Open"]
        )

        data["Price_Change_Percent"] = (
            data["Price_Change"] / data["Open"]
        ) * 100

        data["SMA_5"] = (
            data["Close"].rolling(5).mean()
        )

        data["SMA_10"] = (
            data["Close"].rolling(10).mean()
        )

        delta = data["Close"].diff()

        gain = delta.clip(lower=0)
        loss = -delta.clip(upper=0)

        average_gain = gain.rolling(14).mean()
        average_loss = loss.rolling(14).mean()

        rs = average_gain / average_loss

        data["RSI"] = 100 - (
            100 / (1 + rs)
        )

        data["Target"] = (
            data["Close"].shift(-1) > data["Close"]
        ).astype(int)

        data = data.dropna()

        data = data.iloc[:-1]

        data["Symbol"] = symbol

        print(
            f"✅ Processed {len(data)} rows for {symbol}"
        )

        return data[FEATURES + ["Target", "Symbol"]]

    except Exception as error:

        print(
            f"❌ Error processing {symbol}: {error}"
        )

        return None

    
        print(
            f"❌ Error processing {symbol}: {error}"
        )

        return None


# Dynamic symbol input
if len(sys.argv) > 1:

    symbols = sys.argv[1:]

else:

    symbols = ["RELIANCE.NS"]


all_data = []

for symbol in symbols:

    stock_data = prepare_stock_data(symbol)

    if stock_data is not None:
        all_data.append(stock_data)


if not all_data:

    raise ValueError("No valid stock data found")


combined_data = pd.concat(
    all_data,
    ignore_index=True
)


output_file = "data/multi_stock_ml_dataset.csv"

combined_data.to_csv(
    output_file,
    index=False
)


print("\n================================")
print("DATASET PREPARED SUCCESSFULLY")
print("================================")

print("Total Rows:", len(combined_data))

print(
    "Successful Symbols:",
    combined_data["Symbol"].unique().tolist()
)

print("\nRows by Symbol:")

print(
    combined_data["Symbol"].value_counts()
)

print("\nSaved:", output_file)