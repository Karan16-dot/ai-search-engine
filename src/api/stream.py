import json

from pipeline.search_pipeline import SearchPipeline


pipeline = SearchPipeline()


def generate_stream(query: str):
    """
    Generate a Server-Sent Events (SSE) stream.
    """

    # Stage 1
    yield f"data: {json.dumps({'type': 'status', 'message': 'Searching the web...'})}\n\n"

    # The pipeline performs retrieval + prompt building before streaming
    stream = pipeline.stream(query)

    yield f"data: {json.dumps({'type': 'status', 'message': 'Generating answer...'})}\n\n"

    # Stream LLM tokens
    for chunk in stream:
        yield f"data: {json.dumps({'type': 'token', 'content': chunk})}\n\n"

    # Completion event
    yield f"data: {json.dumps({'type': 'done'})}\n\n"