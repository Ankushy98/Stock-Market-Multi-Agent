
import re


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

        self.negation_words = {
            "not",
            "no",
            "never",
            "without"
        }

    def analyze_news(self, news):

        news = news.lower()

        positive_score = 0
        negative_score = 0

        positive_matches = []
        negative_matches = []

        # Tokenize news text
        words = re.findall(r"\b\w+\b", news)

        # Sentiment analysis with negation handling
        for index, word in enumerate(words):

            previous_words = words[max(0, index - 3):index]

            is_negated = any(
                negation in previous_words
                for negation in self.negation_words
            )

            if word in self.positive_words:

                weight = self.positive_words[word]

                if is_negated:
                    negative_score += weight
                    negative_matches.append(
                        f"not_{word}"
                    )
                else:
                    positive_score += weight
                    positive_matches.append(word)

            elif word in self.negative_words:

                weight = self.negative_words[word]

                if is_negated:
                    positive_score += weight
                    positive_matches.append(
                        f"not_{word}"
                    )
                else:
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