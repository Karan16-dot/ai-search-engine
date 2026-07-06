from llm.gemini_chat import GeminiChatClient

chat_client = GeminiChatClient()

def process_query(query: str)->str:
    """
    Process a user's query and return the AI response

    """
    return chat_client.send_message(query)