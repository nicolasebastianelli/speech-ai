import os

from dotenv import load_dotenv

from speechai import SpeechAI
from speechai.llm import OpenAI
from speechai.tts import GTTS

load_dotenv()
api_key = os.getenv("OPENAI-KEY")

openai = OpenAI(api_key)
tts = GTTS()
speech_ai = SpeechAI(openai, tts)

speech_ai.generate_speech("What is the average height of giraffe?", "audio/giraffe.mp3")
[text, audio] = speech_ai.generate_speech("How fast can a tuna swim?", "audio/tuna.mp3")
print(text)
print(audio)
