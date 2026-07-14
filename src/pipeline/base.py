from abc import ABC, abstractmethod


class PipelineStage(ABC):
    """
    Base class for every pipeline stage.
    """

    @abstractmethod
    def run(self, data):
        """
        Execute the pipeline stage.
        """
        pass