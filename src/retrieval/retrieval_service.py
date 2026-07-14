from retrieval.models import SearchResponse, SearchResult
from retrieval.tavily_client import TavilyClient


class RetrievalService:
    """
    Converts raw search provider responses into
    application domain models.
    """

    def __init__(self):
        self.client = TavilyClient()

    def search(
        self,
        query: str,
        max_results: int = 5
    ) -> SearchResponse:

        raw_response = self.client.search(
            query=query,
            max_results=max_results,
        )

        results = []

        for item in raw_response.get("results", []):

            result = SearchResult(
                title=item.get("title", ""),
                url=item.get("url", ""),
                content=item.get("content", ""),
            )

            results.append(result)

        return SearchResponse(
            query=query,
            results=results,
        )