def decision_agent(news_result, ml_result, market_result=None):

    sentiment = news_result.get(
        "sentiment",
        "Neutral"
    )

    ml_prediction = ml_result.get(
        "predicted_direction",
        "Unknown"
    )

    market_impact = "Neutral"

    if market_result:
        market_impact = market_result.get(
            "market_impact",
            "Neutral"
        )

    score = 0
    reasons = []

    # ==============================
    # NEWS SIGNAL
    # ==============================

    if sentiment == "Positive":
        score += 1
        reasons.append(
            "News sentiment is positive."
        )

    elif sentiment == "Negative":
        score -= 1
        reasons.append(
            "News sentiment is negative."
        )


    # ==============================
    # ML SIGNAL
    # ==============================

    if ml_prediction == "Up":
        score += 1
        reasons.append(
            "ML model predicted upward direction."
        )

    elif ml_prediction == "Down":
        score -= 1
        reasons.append(
            "ML model predicted downward direction."
        )


    # ==============================
    # MARKET SIGNAL
    # ==============================

    if market_impact == "Bullish":
        score += 1
        reasons.append(
            "Market agent detected bullish impact."
        )

    elif market_impact == "Bearish":
        score -= 1
        reasons.append(
            "Market agent detected bearish impact."
        )


    # ==============================
    # FINAL MODEL SIGNAL
    # ==============================

    if score >= 2:

        final_decision = "Positive Signal"

    elif score <= -2:

        final_decision = "Negative Signal"

    else:

        final_decision = "Mixed Signal"


    # ==============================
    # CONFIDENCE
    # ==============================

    confidence = min(
        abs(score) / 3 * 100,
        100
    )

    confidence = round(
        confidence,
        2
    )


    # ==============================
    # REASON
    # ==============================

    if reasons:

        reason = " ".join(reasons)

    else:

        reason = (
            "News, ML and market signals "
            "did not provide a strong direction."
        )


    return {

        "final_decision":
            final_decision,

        "confidence":
            confidence,

        "score":
            score,

        "reason":
            reason

    }


# ==============================
# TEST
# ==============================

if __name__ == "__main__":

    news_result = {
        "sentiment": "Positive"
    }

    ml_result = {
        "predicted_direction": "Up"
    }

    market_result = {
        "market_impact": "Bullish"
    }

    result = decision_agent(
        news_result,
        ml_result,
        market_result
    )

    print(
        "\n========== DECISION AGENT =========="
    )

    print(result)