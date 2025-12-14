from ai.base_model import IAIModel
import os
from PIL import Image
import numpy as np

# Simple mock image generator
def generate_mock_image(path: str, prompt: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # Create a simple colored image based on hash of prompt
    color_hash = hash(prompt) % 0xFFFFFF
    r, g, b = (color_hash >> 16) & 0xFF, (color_hash >> 8) & 0xFF, color_hash & 0xFF
    
    img = np.zeros((256, 256, 3), dtype=np.uint8)
    img[:, :] = [r, g, b]
    
    pil_img = Image.fromarray(img)
    pil_img.save(path)
    return path

class ImageGenerator:
    def __init__(self, model: IAIModel):
        self.model = model

    def generate(self, prompt: str, output_path: str = None) -> str:
        if not output_path:
            output_path = f"generated/image_{hash(prompt) % 10000}.jpg"
        
        # In real app, use self.model.generate_image(prompt)
        # For now, use mock
        return generate_mock_image(output_path, prompt)