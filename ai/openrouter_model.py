import requests
from ai.base_model import IAIModel
import os

class OpenRouterModel(IAIModel):
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("OPENROUTER_API_KEY")

    def generate_text(self, prompt: str) -> str:
        if not self.api_key:
            return "OpenRouter API ключ не указан. Функция отключена."
        print(f"[OpenRouter] Генерация текста: {prompt[:100]}...")
        return f"Сгенерированный пост по теме: {prompt[:50]}... (через OpenRouter)"

    def generate_image(self, prompt: str) -> str:
        return "OpenRouter не поддерживает генерацию изображений."