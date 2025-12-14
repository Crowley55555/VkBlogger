import requests
from ai.base_model import IAIModel
import os

class GigaChatModel(IAIModel):
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("GIGACHAT_API_KEY")
        self.base_url = "https://api.gigachat.ai/v1"

    def generate_text(self, prompt: str) -> str:
        if not self.api_key:
            return "GigaChat API ключ не указан. Используется заглушка."
        # Placeholder for real API call
        print(f"[GigaChat] Генерация текста: {prompt[:100]}...")
        return f"Сгенерированный пост по теме: {prompt[:50]}... (через GigaChat)"

    def generate_image(self, prompt: str) -> str:
        print(f"[GigaChat] Генерация изображения: {prompt[:100]}...")
        return "generated/gigachat_image.jpg"