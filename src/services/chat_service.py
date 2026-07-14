from pipeline.search_pipeline import SearchPipeline


class ChatService:

    def __init__(self):
        self.pipeline = SearchPipeline()

    async def chat(self, query: str):
        return self.pipeline.run(query)

    def stream_response(self, query: str):
        return self.pipeline.stream(query)