class Post:
    def __init__(self, text: str, image_path: str = None, hashtags: list = None):
        self.text = text
        self.image_path = image_path
        self.hashtags = hashtags or []

    def to_dict(self) -> dict:
        return {
            "text": self.text + " " + " ".join(self.hashtags),
            "image_path": self.image_path
        }