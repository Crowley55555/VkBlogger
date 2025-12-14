from post.post import Post
from ai.base_model import IAIModel
from news.news_fetcher import NewsItem
from post.style_presets import STYLE_PROMPTS
import re

class PostGenerator:
    def __init__(self, ai_model: IAIModel):
        self.ai_model = ai_model

    def generate_post(self, news_item: NewsItem, topic: str, style: str) -> Post:
        style_prompt = STYLE_PROMPTS.get(style, "Напиши пост в нейтральном стиле.")
        prompt = f"""{style_prompt} Напиши короткий, но содержательный пост (не более 800 символов) на тему: "{topic}". 
Используй стиль: {style}. Основывайся на следующей новости: 
Заголовок: {news_item.title}.
Краткое содержание: {news_item.summary}.
Добавь 1–2 хештега в конце. Не используй markdown."""

        text = self.ai_model.generate_text(prompt)
        
        # Extract hashtags if any
        hashtags = re.findall(r'#\w+', text)
        # Limit text to 800 chars
        if len(text) > 800:
            # Try to preserve hashtags
            text = text[:780]
            if hashtags:
                last_hashtag = hashtags[-1]
                if last_hashtag not in text:
                    text = text[:750] + "... " + last_hashtag
            else:
                text = text.rstrip() + "..."
        
        return Post(text=text, hashtags=hashtags)