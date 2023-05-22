import openai

from speechai.llm.abstract_llm import AbstractLLM


class OpenAI(AbstractLLM):
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_text(self, prompt):
        print("Generating text")
        response = openai.Completion.create(
            engine="text-davinci-003", prompt=prompt, max_tokens=100  # Adjust as per your API version
        )
        return response.choices[0].text.strip()
