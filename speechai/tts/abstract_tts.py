from abc import ABC, abstractmethod


class AbstractTTS(ABC):

    @abstractmethod
    def text_to_speech(self, text: str):
        pass
