from llm.gemini import GeminiLLM

llm = GeminiLLM()


def process_query(query: str) -> str:
    """
    Return the complete response.
    """
    return llm.send_message(query)


def stream_query(query: str):
    """
    Stream the response.
    """
    return llm.stream_message(query)