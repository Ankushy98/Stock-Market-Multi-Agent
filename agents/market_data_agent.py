
import yfinance as yf


def get_stock_data(symbol):
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period="1mo")

        if data.empty or len(data) < 2:
            return {
                "symbol": symbol,
                "status": "error",
                "error": f"No valid stock data found for {symbol}"
            }

        latest = data.iloc[-1]
        previous = data.iloc[-2]

        latest_close = float(latest["Close"])
        previous_close = float(previous["Close"])

        change = latest_close - previous_close
        change_percent = (change / previous_close) * 100

        if change_percent > 0:
            direction = "Up"
        elif change_percent < 0:
            direction = "Down"
        else:
            direction = "Stable"

        history_dates = [
            date.strftime("%Y-%m-%d")
            for date in data.index
        ]

        history_prices = [
            round(float(price), 2)
            for price in data["Close"]
        ]

        return {
            "symbol": symbol,
            "status": "success",
            "open": round(float(latest["Open"]), 2),
            "high": round(float(latest["High"]), 2),
            "low": round(float(latest["Low"]), 2),
            "latest_close": round(latest_close, 2),
            "previous_close": round(previous_close, 2),
            "volume": int(latest["Volume"]),
            "change_percent": round(change_percent, 2),
            "direction": direction,
            "history_dates": history_dates,
            "history_prices": history_prices
        }

    except Exception as error:
        return {
            "symbol": symbol,
            "status": "error",
            "error": str(error)
        }