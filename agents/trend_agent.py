def trend_agent(market_result, stock_result):

    market_impact = market_result["market_impact"]
    price_direction = stock_result.get("direction", "Stable")

    # News + Price combination

    if market_impact == "Bullish" and price_direction == "Up":
        trend = "Strong Uptrend"

    elif market_impact == "Bearish" and price_direction == "Down":
        trend = "Strong Downtrend"

    elif market_impact == "Bullish" or price_direction == "Up":
        trend = "Uptrend"

    elif market_impact == "Bearish" or price_direction == "Down":
        trend = "Downtrend"

    else:
        trend = "Sideways"

    return {
        "market_impact": market_impact,
        "price_direction": price_direction,
        "predicted_trend": trend
    }


if __name__ == "__main__":

    market_result = {
        "market_impact": "Bullish"
    }

    stock_result = {
        "direction": "Up"
    }

    result = trend_agent(market_result, stock_result)

    print("Trend Agent Result:")
    print(result)