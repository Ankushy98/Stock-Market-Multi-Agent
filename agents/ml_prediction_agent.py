import joblib
import pandas as pd
import yfinance as yf


MODEL_PATH = "models/random_forest_model.pkl"


def calculate_rsi(close_prices, period=14):

    delta = close_prices.diff()

    gain = delta.clip(lower=0)

    loss = -delta.clip(upper=0)

    average_gain = gain.rolling(
        window=period
    ).mean()

    average_loss = loss.rolling(
        window=period
    ).mean()

    rs = average_gain / average_loss

    rsi = 100 - (100 / (1 + rs))

    return rsi


def predict_stock_direction(stock_result):

    # ==============================
    # LOAD MODEL
    # ==============================

    model = joblib.load(MODEL_PATH)


    # ==============================
    # GET STOCK DATA
    # ==============================

    symbol = stock_result["symbol"]

    stock = yf.Ticker(symbol)

    data = stock.history(
        period="1mo"
    )


    if len(data) < 15:

        return {
            "ml_prediction": -1,
            "predicted_direction": "Insufficient Data"
        }


    # ==============================
    # CALCULATE FEATURES
    # ==============================

    close = data["Close"]

    latest = data.iloc[-1]


    price_change = (
        float(latest["Close"])
        - float(latest["Open"])
    )


    price_change_percent = (
        price_change
        / float(latest["Open"])
    ) * 100


    sma_5 = close.rolling(
        window=5
    ).mean().iloc[-1]


    sma_10 = close.rolling(
        window=10
    ).mean().iloc[-1]


    rsi = calculate_rsi(
        close
    ).iloc[-1]


    # ==============================
    # CREATE MODEL INPUT
    # ==============================

    input_data = pd.DataFrame([{

        "Open": float(latest["Open"]),

        "High": float(latest["High"]),

        "Low": float(latest["Low"]),

        "Close": float(latest["Close"]),

        "Volume": int(latest["Volume"]),

        "Price_Change": price_change,

        "Price_Change_Percent":
            price_change_percent,

        "SMA_5": float(sma_5),

        "SMA_10": float(sma_10),

        "RSI": float(rsi)

    }])


    # ==============================
    # PREDICTION
    # ==============================

    prediction = model.predict(
        input_data
    )[0]


    if prediction == 1:

        direction = "Up"

    else:

        direction = "Down"


    return {

        "ml_prediction": int(prediction),

        "predicted_direction": direction,

        "SMA_5": round(float(sma_5), 2),

        "SMA_10": round(float(sma_10), 2),

        "RSI": round(float(rsi), 2)

    }


# ==============================
# TEST
# ==============================

if __name__ == "__main__":

    sample_stock = {

        "symbol": "RELIANCE.NS"

    }


    result = predict_stock_direction(
        sample_stock
    )


    print(
        "\n========== ML PREDICTION =========="
    )

    print(result)