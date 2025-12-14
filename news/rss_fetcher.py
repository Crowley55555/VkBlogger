import feedparser
from news.news_fetcher import INewsFetcher, NewsItem
from typing import List

class RSSFetcher(INewsFetcher):
    def __init__(self, rss_urls: List[str]):
        self.rss_urls = rss_urls

    def fetch_news(self, topic: str, limit: int = 5) -> List[NewsItem]:
        news = []
        for url in self.rss_urls:
            try:
                feed = feedparser.parse(url)
                for entry in feed.entries[:limit]:
                    news.append(
                        NewsItem(
                            title=entry.title,
                            summary=entry.summary[:200],
                            url=entry.link,
                            source="RSS"
                        )
                    )
            except Exception as e:
                print(f"Error fetching RSS {url}: {e}")
        return news[:limit]