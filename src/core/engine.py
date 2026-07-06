from llm.gemini_chat import GeminiChatClient

from llm.factory import get_llm
llm = get_llm()


def process_query(query: str):

    
    """
    Process a user's query and return the AI response

    """
    return llm.stream_message(query)