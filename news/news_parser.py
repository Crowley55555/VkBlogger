class NewsParser:
    @staticmethod
    def extract_keywords(text: str, n: int = 5) -> List[str]:
        # Simple keyword extraction (placeholder)
        words = text.lower().split()
        # Remove common stop words
        stop_words = {"и", "в", "на", "не", "я", "с", "что", "а", "по", "к", "у", "от", "за", "о", "из", "это", "как", "он", "она"}
        words = [w for w in words if w.isalpha() and w not in stop_words]
        # Simple frequency counting
        freq = {}
        for w in words:
            freq[w] = freq.get(w, 0) + 1
        return sorted(freq.keys(), key=lambda x: freq[x], reverse=True)[:n]