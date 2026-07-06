from google import genai

from config.settings import settings


class GeminiLLM:

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

        self.chat = self.client.chats.create(
            model=settings.MODEL_NAME
        )

    def send_message(self, message: str) -> str:
        response = self.chat.send_message(message)
        return response.text

    def stream_message(self, message: str):
        for chunk in self.chat.send_message_stream(message):
            if chunk.text:
                yield chunk.text