class IATAAirport:
    str url = "https://www.iata.org/en/publications/directories/code-search/?"
    @classmethod
    def getIATAAirportUrl(cls) -> str:
        return cls.url