from google import genai
 
 from config.settings import settings


load_dotenv()

class GeminiLLM(BaseLLM):

    def __init__(self):
        self.client = genai.Client(
            api_key = settings.GEMINI_API_KEY
        )
        self.chat = self.client.chats.create(
            model = settings.MODEL_NAME
        )

    def send_message(self,message:str)->str:
       for chunk in self.chat.send_message_stream(message):
       yield chunk.text