import os

import speechai as sa

from dotenv import load_dotenv

load_dotenv()
generator = sa.Generator(os.getenv("OPENAI-KEY"))
generator.generate_speech("What is the average height of giraffe?")
