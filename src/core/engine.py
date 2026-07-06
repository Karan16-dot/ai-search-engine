from llm.gemini import GeminiLLM

llm = GeminiLLM()


def process_query(query: str):
    """
    Process a user query and return a streaming generator.
    """
    return llm.stream_message(query)