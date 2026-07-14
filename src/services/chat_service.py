from core.engine import process_query, stream_query


class ChatService:
    """
    Handles chat-related business logic.
    """

    async def chat(self, query: str) -> str:
        """
        Generate the complete response.
        Used by the REST API.
        """
        return process_query(query)

    def stream_response(self, query: str):
        """
        Stream the response.
        Used by the CLI.
        """
        return stream_query(query)