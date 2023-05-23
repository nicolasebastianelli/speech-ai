from ..llm.abstract_llm import AbstractLLM
from ..tts.abstract_tts import AbstractTTS
from ..utils import create_directory_from_path


class SpeechAI:
    __llm: AbstractLLM
    __tts: AbstractTTS

    def __init__(self, llm: AbstractLLM, tts: AbstractTTS):
        self.set_llm(llm)
        self.set_tts(tts)

    def synthesize_dialog(self, prompt: str, save_to: str):
        create_directory_from_path(save_to)
        text = self.__llm.generate_text(prompt)
        audio = self.__tts.text_to_speech(text, save_to)
        return [text, audio]

    def set_llm(self, llm: AbstractLLM):
        self.__llm = llm

    def set_tts(self, tts: AbstractTTS):
        self.__tts = tts

    def get_llm(self):
        return self.__llm

    def get_tts(self):
        return self.__tts

    def set_language(self, language_code: str):
        self.__tts.set_language(language_code)
