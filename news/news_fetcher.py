from abc import ABC, abstractmethod
from typing import List

class NewsItem:
    def __init__(self, title: str, summary: str, url: str, source: str):
        self.title = title
        self.summary = summary
        self.url = url
        self.source = source

    def __hash__(self):
        return hash(self.url)

    def __eq__(self, other):
        return isinstance(other, NewsItem) and self.url == other.url


class INewsFetcher(ABC):
    @abstractmethod
    def fetch_news(self, topic: str, limit: int = 5) -> List[NewsItem]:
        pass