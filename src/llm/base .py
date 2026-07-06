from abc import ABC, abstractmethod

class BaseLLM(ABC):
    @abstractmethod
    def send_message(self,message:str)->str
    """
    Send a message to the language model
    """
    pass