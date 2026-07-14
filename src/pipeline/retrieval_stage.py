from pipeline.base import PipelineStage
from retrieval.retrieval_service import RetrievalService


class RetrievalStage(PipelineStage):

    def __init__(self):
        self.service = RetrievalService()

    def run(self, query: str):

        return self.service.search(query)