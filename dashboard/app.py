
import json
import os

from flask import Flask, render_template, request

from agents.news_agent import NewsAgent
from agents.news_collector import NewsCollector
from agents.market_agent import market_agent
from agents.trend_agent import trend_agent
from agents.market_data_agent import get_stock_data
from agents.ml_prediction_agent import predict_stock_direction
from agents.decision_agent import decision_agent
from utils.audit_logger import log_agent_result

from models.ml_analysis import get_ml_analysis


app = Flask(__name__)


@app.route("/")
def home():

    # ======================================
    # STOCK SYMBOL
    # ======================================

    symbol = request.args.get(
        "symbol",
        "RELIANCE.NS"
    ).upper()


    # ======================================
    # STOCK DATA
    # ======================================

    stock_result = get_stock_data(symbol)

    if stock_result.get("status") == "error":

        return render_template(
            "error.html",
            symbol=symbol,
            error=stock_result.get(
                "error",
                "Invalid stock symbol or data unavailable."
            )
        )


    # ======================================
    # ML PREDICTION
    # ======================================

    ml_result = predict_stock_direction(
        stock_result
    )
    log_agent_result(
    "ML Prediction Agent",
    ml_result,
    symbol
)


    # ======================================
    # NEWS COLLECTION
    # ======================================

    collector = NewsCollector(symbol)

    news_list = collector.collect_news(symbol)

    news_agent = NewsAgent()


    # ======================================
    # NEWS SENTIMENT ANALYSIS
    # ======================================

    positive_news = 0
    negative_news = 0
    neutral_news = 0

    total_positive_score = 0
    total_negative_score = 0
    confidence_score = 0


    for news in news_list[:5]:

        result = news_agent.analyze_news(news)
        log_agent_result(
    "News Agent",
    result,
    symbol
)

        total_positive_score += result.get(
            "positive_score",
            0
        )

        total_negative_score += result.get(
            "negative_score",
            0
        )


        if result["sentiment"] == "Positive":

            positive_news += 1

        elif result["sentiment"] == "Negative":

            negative_news += 1

        else:

            neutral_news += 1


    # ======================================
    # OVERALL SENTIMENT
    # ======================================

    if total_positive_score > total_negative_score:

        overall_sentiment = "Positive"

    elif total_negative_score > total_positive_score:

        overall_sentiment = "Negative"

    else:

        overall_sentiment = "Neutral"


    # ======================================
    # CONFIDENCE SCORE
    # ======================================

    total_score = (
        total_positive_score
        + total_negative_score
    )


    if total_score == 0:

        confidence_score = 0

    else:

        confidence_score = round(
            (
                abs(
                    total_positive_score
                    - total_negative_score
                )
                / total_score
            ) * 100,
            2
        )


    news_result = {

        "sentiment": overall_sentiment,

        "positive_score": total_positive_score,

        "negative_score": total_negative_score,

        "confidence_score": confidence_score

    }


    # ======================================
    # MARKET AGENT
    # ======================================

    market_result = market_agent(
        news_result,
        stock_result
    )
    log_agent_result(
    "Market Agent",
    market_result,
    symbol
)


    # ======================================
    # TREND AGENT
    # ======================================

    trend_result = trend_agent(
        market_result,
        stock_result
    )
    log_agent_result(
    "Trend Agent",
    trend_result,
    symbol
)


    # ======================================
    # DECISION AGENT
    # ======================================

    decision_result = decision_agent(

        news_result,

        ml_result,

        market_result

    )
    log_agent_result(
    "Decision Agent",
    decision_result,
    symbol
)


    # ======================================
    # ML MODEL ANALYSIS
    # ======================================

    ml_analysis = get_ml_analysis(symbol)


    # ======================================
    # AUDIT LOG
    # ======================================

    audit_logs = []

    log_file = "utils/audit_log.json"


    if os.path.exists(log_file):

        with open(
            log_file,
            "r",
            encoding="utf-8"
        ) as file:

            try:

                audit_logs = json.load(file)

            except json.JSONDecodeError:

                audit_logs = []


    # Filter logs for selected stock symbol

    audit_logs = [

        log for log in audit_logs

        if log.get("symbol") == symbol

    ]


    # Show latest 10 logs

    audit_logs = audit_logs[-10:]


    # ======================================
    # DATA FOR HTML
    # ======================================

    data = {

        # Stock

        "symbol": symbol,

        "price": stock_result.get(
            "latest_close",
            0
        ),

        "change_percent": stock_result.get(
            "change_percent",
            0
        ),


        # Stock chart

        "chart_dates": stock_result.get(
            "history_dates",
            []
        ),

        "chart_prices": stock_result.get(
            "history_prices",
            []
        ),


        # ML

        "ml_prediction": ml_result.get(
            "predicted_direction",
            "Unknown"
        ),


        # Trend

        "trend": trend_result.get(
            "predicted_trend",
            "Unknown"
        ),


        # Decision

        "decision": decision_result.get(
            "final_decision",
            "Mixed Signal"
        ),


        "confidence": decision_result.get(
            "confidence",
            0
        ),


        "decision_reason": decision_result.get(
            "reason",
            "No explanation available."
        ),


        # News

        "news": news_list[:5],

        "positive_news": positive_news,

        "negative_news": negative_news,

        "neutral_news": neutral_news,

        "news_sentiment": news_result.get(
            "sentiment",
            "Neutral"
        ),


        # Agent results

        "news_agent": news_result,

        "market_agent": market_result,

        "trend_agent": trend_result.get(
            "predicted_trend",
            "Unknown"
        ),

        "decision_agent": decision_result.get(
            "final_decision",
            "Mixed Signal"
        ),


        # Audit

        "audit_logs": audit_logs,


        # ML Analysis Data

        "model_comparison": ml_analysis.get(
            "model_comparison",
            []
        ),

        "feature_importance": ml_analysis.get(
            "feature_importance",
            []
        )

    }


    # ======================================
    # SEND DATA TO HTML
    # ======================================

    return render_template(
        "index.html",
        data=data
    )


# ==========================================
# START FLASK SERVER
# ==========================================

if __name__ == "__main__":

    app.run(
        debug=True
    )