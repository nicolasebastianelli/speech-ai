from gtts import gTTS

from speechai.tts.abstract_tts import AbstractTTS


class GTTS(AbstractTTS):
    __language: str

    def __init__(self, language_code="en"):
        self.set_language(language_code)

    def text_to_speech(self, text: str, save_to: str):
        tts = gTTS(text, lang=self.__language)
        tts.save(save_to)
        return save_to

    def set_language(self, language_code: str):
        self.__language = language_code
