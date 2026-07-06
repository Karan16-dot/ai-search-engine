from core.engine import process_query


class ChatService:

    def stream_response(self, query: str):
        """
        Stream a response for the user's query.
        """

        return process_query(query)