def market_agent(news_result, stock_result=None):

    sentiment = news_result.get("sentiment", "Neutral")

    positive_score = news_result.get("positive_score", 0)
    negative_score = news_result.get("negative_score", 0)

    change_percent = 0
    stock_direction = "Unknown"

    if stock_result:

        change_percent = stock_result.get("change_percent", 0)
        stock_direction = stock_result.get("direction", "Unknown")

    # Combined market impact

    if sentiment == "Positive" and stock_direction == "Up":

        market_impact = "Bullish"

    elif sentiment == "Negative" and stock_direction == "Down":

        market_impact = "Bearish"

    elif sentiment == "Positive" and stock_direction == "Down":

        market_impact = "Mixed Signal"

    elif sentiment == "Negative" and stock_direction == "Up":

        market_impact = "Mixed Signal"

    elif stock_direction == "Up":

        market_impact = "Positive Price Movement"

    elif stock_direction == "Down":

        market_impact = "Negative Price Movement"

    else:

        market_impact = "Neutral"


    return {

        "sentiment": sentiment,

        "positive_score": positive_score,

        "negative_score": negative_score,

        "market_impact": market_impact,

        "change_percent": change_percent,

        "stock_direction": stock_direction

    }