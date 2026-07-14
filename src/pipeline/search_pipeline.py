from models.response import AIResponse
from pipeline.llm_stage import LLMStage
from pipeline.prompt_stage import PromptStage
from pipeline.retrieval_stage import RetrievalStage


class SearchPipeline:

    def __init__(self):
        self.retrieval = RetrievalStage()
        self.prompt = PromptStage()
        self.llm = LLMStage()

    def run(self, query: str) -> AIResponse:
        """
        Complete response.
        """

        search_response = self.retrieval.run(query)

        prompt = self.prompt.run(search_response)

        answer = self.llm.run(prompt)

        return AIResponse(
            answer=answer,
            sources=search_response.results,
        )

    def stream(self, query: str):
        """
        Stream only the LLM output.
        """

        search_response = self.retrieval.run(query)

        prompt = self.prompt.run(search_response)

        return self.llm.stream(prompt)