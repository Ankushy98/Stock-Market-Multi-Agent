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


    # ======================================
    # ML PREDICTION
    # ======================================

    ml_result = predict_stock_direction(
        stock_result
    )


    # ======================================
    # NEWS COLLECTION
    # ======================================

    collector = NewsCollector()

    news_list = collector.collect_news()


    news_agent = NewsAgent()


    # ======================================
    # NEWS SENTIMENT ANALYSIS
    # ======================================

    if news_list:

        positive_news = 0
        negative_news = 0
        neutral_news = 0

        total_positive_score = 0
        total_negative_score = 0


        for news in news_list[:5]:

            result = news_agent.analyze_news(
                news
            )


            total_positive_score += (
                result["positive_score"]
            )


            total_negative_score += (
                result["negative_score"]
            )


            if result["sentiment"] == "Positive":

                positive_news += 1

            elif result["sentiment"] == "Negative":

                negative_news += 1

            else:

                neutral_news += 1


        # Overall sentiment

        if total_positive_score > total_negative_score:

            overall_sentiment = "Positive"

        elif total_negative_score > total_positive_score:

            overall_sentiment = "Negative"

        else:

            overall_sentiment = "Neutral"


        news_result = {

            "sentiment":
                overall_sentiment,

            "positive_score":
                total_positive_score,

            "negative_score":
                total_negative_score

        }


    else:

        positive_news = 0
        negative_news = 0
        neutral_news = 0


        news_result = {

            "sentiment":
                "Neutral",

            "positive_score":
                0,

            "negative_score":
                0

        }


    # ======================================
    # MARKET AGENT
    # ======================================

    market_result = market_agent(
        news_result
    )


    # ======================================
    # TREND AGENT
    # ======================================

    trend_result = trend_agent(
        market_result,
        stock_result
    )


    # ======================================
    # DECISION AGENT
    # ======================================

    decision_result = decision_agent(

        news_result,

        ml_result,

        market_result

    )


    # ======================================
    # ML MODEL ANALYSIS
    # ======================================

    ml_analysis = get_ml_analysis()


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


    # Show latest 10 logs

    audit_logs = audit_logs[-10:]


    # ======================================
    # DATA FOR HTML
    # ======================================

    data = {

        # Stock

        "symbol":
            symbol,

        "price":
            stock_result.get(
                "latest_close",
                0
            ),

        "change_percent":
            stock_result.get(
                "change_percent",
                0
            ),


        # Stock chart

        "chart_dates":
            stock_result.get(
                "history_dates",
                []
            ),

        "chart_prices":
            stock_result.get(
                "history_prices",
                []
            ),


        # ML

        "ml_prediction":
            ml_result.get(
                "predicted_direction",
                "Unknown"
            ),


        # Trend

        "trend":
            trend_result.get(
                "predicted_trend",
                "Unknown"
            ),


        # Decision

        "decision":
            decision_result.get(
                "final_decision",
                "Mixed Signal"
            ),


        "confidence":
            decision_result.get(
                "confidence",
                0
            ),


        "decision_reason":
            decision_result.get(
                "reason",
                "No explanation available."
            ),


        # News

        "news":
            news_list[:5],


        "positive_news":
            positive_news,


        "negative_news":
            negative_news,


        "neutral_news":
            neutral_news,


        "news_sentiment":
            news_result.get(
                "sentiment",
                "Neutral"
            ),


        # Agent results

        "news_agent":
            news_result.get(
                "sentiment",
                "Neutral"
            ),


        "market_agent":
            market_result.get(
                "market_impact",
                "Neutral"
            ),


        "trend_agent":
            trend_result.get(
                "predicted_trend",
                "Unknown"
            ),


        "decision_agent":
            decision_result.get(
                "final_decision",
                "Mixed Signal"
            ),


        # Audit

        "audit_logs":
            audit_logs,


        # ==================================
        # ML ANALYSIS DATA
        # ==================================

        "model_comparison":
            ml_analysis[
                "model_comparison"
            ],


        "feature_importance":
            ml_analysis[
                "feature_importance"
            ]

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