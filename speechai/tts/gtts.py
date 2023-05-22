from gtts import gTTS

from speechai.tts.abstract_tts import AbstractTTS


class GTTS(AbstractTTS):
    def __init__(self):
        print("Initialized GTTS")
        self.engine = ""

    def text_to_speech(self, text):
        tts = gTTS(text)
        tts.save("output.mp3")
        print("done")
