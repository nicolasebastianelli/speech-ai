import os

from dotenv import load_dotenv

from speechai import SpeechAI
from speechai.llm import OpenAI
from speechai.tts import GTTS

load_dotenv()
api_key = os.getenv("OPENAI-KEY")

openai = OpenAI(api_key)
tts = GTTS(language_code="it")
speech_ai = SpeechAI(openai, tts)

# speech_ai.synthesize_dialog("What is the average height of giraffe?", "output/giraffe.mp3")
[text, audio] = speech_ai.synthesize_dialog("Quante sono le ostetriche in svizzera?", "output/doctors.mp3")
# [text, audio] = speech_ai.synthesize_dialog("How fast can a tuna swim?", "output/tuna.mp3")
print(text, audio)
