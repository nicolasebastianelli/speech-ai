from ..llm.abstract_llm import AbstractLLM
from ..llm.openai import OpenAI
from ..tts.abstract_tts import AbstractTTS
from ..tts.gtts import GTTS


class Generator:

    llm: AbstractLLM
    tts: AbstractTTS

    def __init__(self, api_key):
        self.llm = OpenAI(api_key)
        self.tts = GTTS()

    def generate_speech(self, prompt):
        text = self.llm.generate_text(prompt)
        print(text)
        self.tts.text_to_speech(text)
