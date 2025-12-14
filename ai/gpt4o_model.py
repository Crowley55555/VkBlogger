import openai
from ai.base_model import IAIModel
import os

class GPT4oModel(IAIModel):
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        openai.api_key = self.api_key

    def generate_text(self, prompt: str) -> str:
        if not self.api_key:
            return "OpenAI API ключ не указан. Используется заглушка."
        print(f"[GPT-4o] Генерация текста: {prompt[:100]}...")
        return f"Сгенерированный пост по теме: {prompt[:50]}... (через GPT-4o)"

    def generate_image(self, prompt: str) -> str:
        print(f"[GPT-4o] Генерация изображения: {prompt[:100]}...")
        return "generated/gpt4o_image.jpg"