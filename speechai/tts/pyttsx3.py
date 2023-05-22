import pyttsx3

from speechai.tts.abstract_tts import AbstractTTS


class PyTTSx3(AbstractTTS):
    def __init__(self):
        print("Initialized PyTTSx3")
        self.engine = pyttsx3.init()

    def text_to_speech(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
        print("done")
