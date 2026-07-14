from pipeline.base import PipelineStage
from core.engine import process_query


class LLMStage(PipelineStage):

    def run(self, prompt: str):

        return process_query(prompt)