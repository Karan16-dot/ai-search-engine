from search.tavily import TavilyClient


class SearchService:

    def __init__(self):
        self.client = TavilyClient()

    def search(self, query: str):
        return self.client.search(query)