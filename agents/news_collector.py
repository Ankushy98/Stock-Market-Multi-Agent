import os
import requests
from dotenv import load_dotenv


load_dotenv()


class NewsCollector:

    def __init__(self):
        self.name = "News Collector Agent"
        self.api_key = os.getenv("NEWS_API_KEY")

    def collect_news(self):

        url = "https://newsapi.org/v2/everything"
        headers = {
            "X-Api-Key": self.api_key
        }

        params = {
    "q": "Reliance Industries OR Reliance",
    "language": "en",
    "sortBy": "publishedAt",
    "pageSize": 10
}

        response = requests.get(
            url,
            headers=headers,
            params=params
        )

        print("API Status Code:", response.status_code)

        data = response.json()

        print("API Status:", data.get("status"))

        if data.get("status") != "ok":
            print("News API Error:")
            print(data)
            return []

        news_list = []

        for article in data["articles"]:

            title = article.get("title")

            if title:
                news_list.append(title)

        return news_list


if __name__ == "__main__":

    collector = NewsCollector()

    news_list = collector.collect_news()

    print("\n========== REAL NEWS ==========")

    for i, news in enumerate(news_list, start=1):

        print(f"{i}. {news}")