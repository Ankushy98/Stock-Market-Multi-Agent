import yfinance as yf


symbol = "RELIANCE.NS"

print("Downloading historical stock data...")

data = yf.download(
    symbol,
    period="2y",
    interval="1d",
    auto_adjust=True
)

if data.empty:
    print("No data found.")
else:
    data = data.reset_index()

    print("\n========== STOCK DATA ==========")
    print(data.head())

    print("\nTotal Rows:", len(data))

    data.to_csv("data/reliance_stock_data.csv", index=False)

    print("\nDataset saved successfully!")