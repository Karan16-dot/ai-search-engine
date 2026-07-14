from google import genai

from config.settings import settings


class GeminiLLM:
    """
    Wrapper around the Gemini Chat API.
    """

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

        self.chat = self.client.chats.create(
            model=settings.MODEL_NAME
        )

    def send_message(self, message: str) -> str:
        """
        Return the complete response.
        Used by REST endpoints.
        """
        response = self.chat.send_message(message)
        return response.text

    def stream_message(self, message: str):
        """
        Stream the response token-by-token.
        Used by the CLI and future SSE endpoint.
        """
        for chunk in self.chat.send_message_stream(message):
            if chunk.text:
                yield chunk.text