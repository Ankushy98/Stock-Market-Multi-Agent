
import os
import requests
from dotenv import load_dotenv


load_dotenv()


class NewsCollector:

    def __init__(self):

        self.name = "News Collector Agent"

        self.api_key = os.getenv("NEWS_API_KEY")

        self.company_keywords = [
            "reliance",
            "reliance industries",
            "ril"
        ]

        self.finance_keywords = [
            "stock",
            "share",
            "market",
            "profit",
            "loss",
            "revenue",
            "investment",
            "business",
            "company",
            "bond",
            "finance",
            "earnings",
            "growth",
            "industry"
        ]

    def is_relevant_news(self, title):

        title = title.lower()

        company_found = any(
            keyword in title
            for keyword in self.company_keywords
        )

        finance_found = any(
            keyword in title
            for keyword in self.finance_keywords
        )

        return company_found and finance_found

    def collect_news(self):

        url = "https://newsapi.org/v2/everything"

        headers = {
            "X-Api-Key": self.api_key
        }

        params = {
            "q": '"Reliance Industries"',
            "language": "en",
            "sortBy": "publishedAt",
            "pageSize": 20
        }

        try:

            response = requests.get(
                url,
                headers=headers,
                params=params,
                timeout=15
            )

            print("API Status Code:", response.status_code)

            data = response.json()

            print("API Status:", data.get("status"))

            if data.get("status") != "ok":

                print("News API Error:")
                print(data)

                return []

            news_list = []

            for article in data.get("articles", []):

                title = article.get("title")

                if title and self.is_relevant_news(title):

                    news_list.append(title)

            return news_list[:10]

        except requests.RequestException as error:

            print("Network Error:", error)

            return []


if __name__ == "__main__":

    collector = NewsCollector()

    news_list = collector.collect_news()

    print("\n========== FILTERED REAL NEWS ==========")

    for i, news in enumerate(news_list, start=1):

        print(f"{i}. {news}")