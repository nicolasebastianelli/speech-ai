import cohere

from speechai.llm.abstract_llm import AbstractLLM


class Cohere(AbstractLLM):
    def __init__(self, api_key):
        self.__client = cohere.Client(api_key)

    def generate_text(self, prompt):
        response = self.__client.generate(model="command", prompt=prompt, max_tokens=200, temperature=0.750)
        return response.generations[0].text.strip()
