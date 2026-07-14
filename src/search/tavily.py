from search.models import SearchResult


class TavilyClient:

    def search(self, query: str) -> list[SearchResult]:
        """
        Temporary implementation.

        Later this will call the Tavily API.
        """

        return [
            SearchResult(
                title="Placeholder Result",
                url="https://example.com",
                content=f"Search results for: {query}"
            )
        ]