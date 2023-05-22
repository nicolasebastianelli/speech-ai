from abc import ABC, abstractmethod


class AbstractLLM(ABC):
    @abstractmethod
    def generate_text(self, prompt: str):
        pass
