from pipeline.base import PipelineStage
from core.engine import process_query, stream_query


class LLMStage(PipelineStage):
    """
    Pipeline stage responsible for interacting with the LLM.
    """

    def run(self, prompt: str) -> str:
        """
        Generate a complete response.
        """
        return process_query(prompt)

    def stream(self, prompt: str):
        """
        Stream the response chunk by chunk.
        """
        return stream_query(prompt)