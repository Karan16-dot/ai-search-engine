from core.engine import process_query, stream_query
from retrieval.prompt_builder import PromptBuilder
from retrieval.retrieval_service import RetrievalService


class ChatService:
    """
    Handles chat-related business logic.
    """

    def __init__(self):
        self.retrieval = RetrievalService()
        self.prompt_builder = PromptBuilder()

    async def chat(self, query: str) -> str:
        """
        Search the web, build a prompt, and generate a grounded response.
        """

        search_response = self.retrieval.search(query)

        prompt = self.prompt_builder.build(
            search_response
        )

        return process_query(prompt)

    def stream_response(self, query: str):
        """
        Stream grounded responses.
        """

        search_response = self.retrieval.search(query)

        prompt = self.prompt_builder.build(
            search_response
        )

        return stream_query(prompt)