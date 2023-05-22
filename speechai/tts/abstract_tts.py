from abc import ABC, abstractmethod


class AbstractTTS(ABC):
    @abstractmethod
    def text_to_speech(self, text: str, save_to: str):
        pass

    @abstractmethod
    def set_language(self, language_code: str):
        pass
