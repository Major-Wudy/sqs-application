class IATAAirport:
    url = "https://www.iata.org/en/publications/directories/code-search/?"
    @classmethod
    def get_iata_airport_url(cls) -> str:
        return cls.url