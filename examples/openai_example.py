import os

from dotenv import load_dotenv

from speechai import SpeechAI
from speechai.llm import OpenAI
from speechai.tts import GTTS

load_dotenv()
api_key = os.getenv("OPENAI-KEY")

openai = OpenAI(api_key)
tts = GTTS(language_code="en")
sa = SpeechAI(openai, tts)

sa.synthesize_dialog("What is the average height of giraffe?", "./output/giraffe-openai-en.mp3")
[text, audio] = sa.synthesize_dialog("Which is the fastest animal on earth?", "./output/fastest-openai-en.mp3")
print(text, audio)
