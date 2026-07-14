import httpx

from config.settings import settings


class TavilyClient:

    BASE_URL = "https://api.tavily.com/search"

    def search(
        self,
        query: str,
        max_results: int = 5
    ) -> dict:

        payload = {
            "api_key": settings.TAVILY_API_KEY,
            "query": query,
            "max_results": max_results
        }

        response = httpx.post(
            self.BASE_URL,
            json=payload,
            timeout=30
        )

        response.raise_for_status()

        return response.json()