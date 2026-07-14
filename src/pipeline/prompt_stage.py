from pipeline.base import PipelineStage
from retrieval.prompt_builder import PromptBuilder


class PromptStage(PipelineStage):

    def __init__(self):
        self.builder = PromptBuilder()

    def run(self, search_response):

        return self.builder.build(search_response)