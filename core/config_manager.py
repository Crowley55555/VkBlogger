import json
import os
from typing import Dict, Any

class ConfigManager:
    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.default_config = {
            "blog_topic": "IT новости",
            "ai_model": "gigachat",
            "post_style": "аналитический",
            "group_id": "",
            "access_token": "",
            "generate_images": False,
            "posting_frequency": 24
        }
        self.config = self.load_config()

    def load_config(self) -> Dict[str, Any]:
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return self.default_config.copy()

    def save_config(self):
        with open(self.config_path, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, ensure_ascii=False, indent=4)

    def update_config(self, key: str, value: Any):
        self.config[key] = value
        self.save_config()