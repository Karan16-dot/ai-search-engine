from llm.client import generate_response
def process_query(user_query: str)->str:
    """
    Process a user's query and return the AI response

    """
    try:
        return generate_response(user_query)

    except Exception as e:
        return f"Something went wrong: {e}"

    return response