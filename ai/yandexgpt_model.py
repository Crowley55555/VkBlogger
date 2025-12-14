import requests
from ai.base_model import IAIModel
import os

class YandexGPTModel(IAIModel):
    def __init__(self, api_key: str = None, folder_id: str = None):
        self.api_key = api_key or os.getenv("YANDEXGPT_API_KEY")
        self.folder_id = folder_id or os.getenv("YANDEX_FOLDER_ID")
        self.base_url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"

    def generate_text(self, prompt: str) -> str:
        if not self.api_key:
            return "YandexGPT API ключ не указан. Используется заглушка."
        print(f"[YandexGPT] Генерация текста: {prompt[:100]}...")
        return f"Сгенерированный пост по теме: {prompt[:50]}... (через YandexGPT)"

    def generate_image(self, prompt: str) -> str:
        print(f"[YandexGPT] Генерация изображения: {prompt[:100]}...")
        return "generated/yandex_image.jpg"