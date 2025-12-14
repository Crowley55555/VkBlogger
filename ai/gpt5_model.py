from ai.base_model import IAIModel
import os

class GPT5Model(IAIModel):
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")  # Assume same as GPT-4o for now

    def generate_text(self, prompt: str) -> str:
        if not self.api_key:
            return "GPT-5 API ключ не указан. Используется заглушка. (GPT-5 пока не существует)"
        print(f"[GPT-5] Генерация текста: {prompt[:100]}...")
        return f"Сгенерированный пост по теме: {prompt[:50]}... (через GPT-5 - заглушка)"

    def generate_image(self, prompt: str) -> str:
        print(f"[GPT-5] Генерация изображения: {prompt[:100]}...")
        return "generated/gpt5_image.jpg"