import httpx

from config.settings import settings
from utils.logger import logger


class TavilyClient:
    """
    Client responsible for communicating with the Tavily Search API.
    """

    BASE_URL = "https://api.tavily.com/search"

    def __init__(self):

        self.client = httpx.Client(
            timeout=30.0
        )

    def search(
        self,
        query: str,
        max_results: int = 5,
    ) -> dict:

        payload = {
            "api_key": settings.TAVILY_API_KEY,
            "query": query,
            "max_results": max_results,
            "search_depth": "advanced",
            "include_answer": False,
            "include_images": False,
            "include_raw_content": False,
        }

        logger.info("Searching Tavily for: %s", query)

        response = self.client.post(
            self.BASE_URL,
            json=payload,
        )

        response.raise_for_status()

        return response.json()