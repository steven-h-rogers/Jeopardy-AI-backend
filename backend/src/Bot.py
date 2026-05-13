from langchain_openai import ChatOpenAI
from backend.models.src_models import BotOutput
from backend.src.utils import timer

"""This class will be used to simulate contestant behavior on jeopardy"""
class Bot():

    def __init__(self):
        self._llm = ChatOpenAI(
            model='gpt-5-nano',
            reasoning_effort='low',
            temperature=0.15
        )

        self.structured_llm = self._llm.with_structured_output(BotOutput)

    @timer
    def generate_bot_answer(self, question, is_correct):
        prompt = f'{question=} {is_correct=} based on the question and isCorrect, create an answer that a contestant would answer that accurately reflects an answer of that correctness. If the answer is correct, make sure it is in the proper Jeopardy format'
        return self.structured_llm.invoke(prompt)