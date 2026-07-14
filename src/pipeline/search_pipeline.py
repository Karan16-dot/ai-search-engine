from models.response import AIResponse
from retrieval.prompt_builder import PromptBuilder
from retrieval.retrieval_service import RetrievalService
from search.query_rewriter import QueryRewriter

from core.engine import process_query


class SearchPipeline:
    """
    Orchestrates the complete AI Search pipeline.
    """

    def __init__(self):

        self.query_rewriter = QueryRewriter()

        self.retrieval = RetrievalService()

        self.prompt_builder = PromptBuilder()

    def run(self, query: str) -> AIResponse:

        rewritten_query = self.query_rewriter.rewrite(query)

        search_response = self.retrieval.search(
            rewritten_query
        )

        prompt = self.prompt_builder.build(
            search_response
        )

        answer = process_query(prompt)

        return AIResponse(
            answer=answer,
            sources=search_response.results
        )