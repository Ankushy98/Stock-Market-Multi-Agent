def market_agent(news_result):
    sentiment = news_result["sentiment"]
    positive_score = news_result["positive_score"]
    negative_score = news_result["negative_score"]

    if sentiment == "Positive":
        if positive_score > negative_score:
            market_impact = "Bullish"
        else:
            market_impact = "Neutral"

    elif sentiment == "Negative":
        if negative_score > positive_score:
            market_impact = "Bearish"
        else:
            market_impact = "Neutral"

    else:
        market_impact = "Neutral"

    return {
        "sentiment": sentiment,
        "positive_score": positive_score,
        "negative_score": negative_score,
        "market_impact": market_impact
    }


# Test only when this file is run directly
if __name__ == "__main__":

    news_result = {
        "sentiment": "Positive",
        "positive_score": 3,
        "negative_score": 0
    }

    result = market_agent(news_result)

    print("Market Agent Result:")
    print(result)