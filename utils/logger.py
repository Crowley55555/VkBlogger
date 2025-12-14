import logging
import os
from datetime import datetime

class Logger:
    def __init__(self, log_file: str = "app.log"):
        self.logger = logging.getLogger("AutoBlogVK")
        self.logger.setLevel(logging.INFO)

        if not self.logger.handlers:
            os.makedirs(os.path.dirname(log_file), exist_ok=True) if os.path.dirname(log_file) else None
            
            handler = logging.FileHandler(log_file, encoding='utf-8')
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def info(self, message: str):
        self.logger.info(message)

    def error(self, message: str):
        self.logger.error(message)

    def debug(self, message: str):
        self.logger.debug(message)