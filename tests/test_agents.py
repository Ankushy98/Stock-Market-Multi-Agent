
import unittest

from agents.news_agent import NewsAgent
from agents.market_agent import market_agent
from agents.trend_agent import trend_agent
from agents.decision_agent import decision_agent


class TestStockAgents(unittest.TestCase):

    def test_news_agent(self):
        agent = NewsAgent()
        result = agent.analyze_news(
            "Company reports strong profit growth"
        )

        self.assertEqual(result["sentiment"], "Positive")

    def test_market_agent(self):
        news_result = {
            "sentiment": "Positive",
            "positive_score": 3,
            "negative_score": 0
        }

        result = market_agent(news_result)

        self.assertEqual(result["market_impact"], "Bullish")

    def test_trend_agent(self):
        market_result = {
            "market_impact": "Bullish"
        }

        stock_result = {
            "direction": "Up"
        }

        result = trend_agent(market_result, stock_result)

        self.assertEqual(
            result["predicted_trend"],
            "Strong Uptrend"
        )

    def test_decision_agent(self):
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

        self.assertEqual(
            result["final_decision"],
            "Positive Signal"
        )


if __name__ == "__main__":
    unittest.main()