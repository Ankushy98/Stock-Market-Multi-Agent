class NewsAgent:
    """
    News Agent analyzes stock market news
    and calculates sentiment scores.
    """

    def __init__(self):
        self.name = "News Agent"

        self.positive_words = {
            "profit": 2,
            "growth": 2,
            "increase": 1,
            "positive": 1,
            "success": 1,
            "strong": 1,
            "revenue": 1,
            "upgrade": 2,
            "surge": 2,
            "rise": 1
        }

        self.negative_words = {
            "loss": 2,
            "decline": 2,
            "decrease": 1,
            "negative": 1,
            "failure": 2,
            "weak": 1,
            "downgrade": 2,
            "fall": 1,
            "drop": 1
        }

    def analyze_news(self, news):

        news = news.lower()

        positive_score = 0
        negative_score = 0

        positive_matches = []
        negative_matches = []

        # Positive analysis
        for word, weight in self.positive_words.items():

            if word in news:

                positive_score += weight
                positive_matches.append(word)

        # Negative analysis
        for word, weight in self.negative_words.items():

            if word in news:

                negative_score += weight
                negative_matches.append(word)

        # Sentiment decision
        if positive_score > negative_score:

            sentiment = "Positive"

        elif negative_score > positive_score:

            sentiment = "Negative"

        else:

            sentiment = "Neutral"

        return {

            "news": news,

            "sentiment": sentiment,

            "positive_score": positive_score,

            "negative_score": negative_score,

            "positive_words_found": positive_matches,

            "negative_words_found": negative_matches
        }


if __name__ == "__main__":

    agent = NewsAgent()

    sample_news = (
        "Reliance reports strong profit growth "
        "and revenue increase"
    )

    result = agent.analyze_news(sample_news)

    print("\n========== NEWS AGENT ==========")

    print(result)