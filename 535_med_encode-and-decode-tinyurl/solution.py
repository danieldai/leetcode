class Codec:
    def __init__(self):
        self.store = dict()
        self.count = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        ans = self.count
        self.store[str(self.count)] = longUrl
        self.count += 1
        return str(ans)
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.store.get(shortUrl, '')
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))