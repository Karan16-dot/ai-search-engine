from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

class GeminiChatClient:

    def __init__(self):
        self.client = genai.Client(
            api_key = os.getenv("GEMINI_API_KEY")
        )
        self.chat = self.client.chats.create(
            model = "gemini-2.5-flash"
        )

    def send_message(self,message:str)->str:
        response = self.chat.send_message(message)
        return response.text