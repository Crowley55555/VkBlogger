from abc import ABC, abstractmethod
from typing import Dict, Any

class IAIModel(ABC):
    @abstractmethod
    def generate_text(self, prompt: str) -> str:
        pass

    @abstractmethod
    def generate_image(self, prompt: str) -> str:
        """
        Generate image from prompt and return path to saved image.
        """
        pass