import os
import json
from typing import Dict, Any

class FileManager:
    @staticmethod
    def save_json(data: Dict[Any, Any], path: str):
        os.makedirs(os.path.dirname(path), exist_ok=True) if os.path.dirname(path) else None
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @staticmethod
    def load_json(path: str) -> Dict[Any, Any]:
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    @staticmethod
    def ensure_dir(path: str):
        os.makedirs(path, exist_ok=True)