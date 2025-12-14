class VKAuth:
    def __init__(self, access_token: str):
        self.access_token = access_token

    def is_valid(self) -> bool:
        # Placeholder for token validation
        return len(self.access_token.strip()) > 0