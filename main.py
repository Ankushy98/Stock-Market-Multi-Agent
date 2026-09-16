from agents.news_agent import NewsAgent
from utils.audit_logger import log_agent_result
from agents.news_collector import NewsCollector
from agents.market_agent import market_agent
from agents.trend_agent import trend_agent
from agents.market_data_agent import get_stock_data
from agents.ml_prediction_agent import predict_stock_direction
from agents.decision_agent import decision_agent


# ==========================================
# STOCK SYMBOL
# ==========================================

symbol = "RELIANCE.NS"


# ==========================================
# STEP 1: GET REAL STOCK DATA
# ==========================================

print("\n========== STOCK DATA ==========")

stock_result = get_stock_data(symbol)

print(stock_result)


# ==========================================
# STEP 2: ML PREDICTION
# ==========================================

print("\n========== ML PREDICTION ==========")

ml_result = predict_stock_direction(stock_result)
log_agent_result("ML Prediction Agent", ml_result)

print(ml_result)


# ==========================================
# STEP 3: COLLECT REAL NEWS
# ==========================================

collector = NewsCollector()

news_list = collector.collect_news()

print("\n========== NEWS COLLECTOR ==========")

for i, news in enumerate(news_list, start=1):
    print(f"{i}. {news}")


# ==========================================
# STEP 4: NEWS ANALYSIS
# ==========================================

news_agent = NewsAgent()


for i, news in enumerate(news_list, start=1):

    print(f"\n\n========== NEWS {i} ==========")

    # News Agent
    news_result = news_agent.analyze_news(news)
    log_agent_result("News Agent", news_result)

    print("\n--- NEWS AGENT ---")
    print(news_result)


    # Market Agent
    market_result = market_agent(news_result)
    log_agent_result("Market Agent", market_result)

    print("\n--- MARKET AGENT ---")
    print(market_result)


    # Trend Agent
    trend_result = trend_agent(market_result,stock_result)
    log_agent_result("Trend Agent", trend_result)

    print("\n--- TREND AGENT ---")
    print(trend_result)


   # Decision Agent
decision_result = decision_agent(news_result,ml_result,market_result)
log_agent_result("Decision Agent", decision_result)

print("\n--- DECISION AGENT ---")
print(decision_result)


print("\n--- FINAL PREDICTION ---")

print(
    "News Sentiment:",
    news_result["sentiment"]
)

print(
    "Market Impact:",
    market_result["market_impact"]
)

print(
    "ML Prediction:",
    ml_result["predicted_direction"]
)

print(
    "Final Trend:",
    trend_result["predicted_trend"]
)

print(
    "Final Decision:",
    decision_result["final_decision"]
)

print(
    "Confidence:",
    str(decision_result["confidence"]) + "%"
)


# ==========================================
# OVERALL NEWS SENTIMENT
# ==========================================

positive_news = 0
negative_news = 0
neutral_news = 0

for news in news_list:

    result = news_agent.analyze_news(news)

    if result["sentiment"] == "Positive":
        positive_news += 1

    elif result["sentiment"] == "Negative":
        negative_news += 1

    else:
        neutral_news += 1


print("\n\n========== OVERALL NEWS SENTIMENT ==========")

print("Positive News:", positive_news)
print("Negative News:", negative_news)
print("Neutral News:", neutral_news)


if positive_news > negative_news:
    overall_sentiment = "Positive"

elif negative_news > positive_news:
    overall_sentiment = "Negative"

else:
    overall_sentiment = "Neutral"


print("Overall Sentiment:", overall_sentiment)