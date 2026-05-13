from langchain_openai import ChatOpenAI
from backend.models.src_models import BotOutput

"""This class will be used to simulate contestant behavior on jeopardy"""
class Bot():

    def __init__(self):
        self._llm = ChatOpenAI(
            model='gpt-5-nano',
            reasoning_effort='low',
            temperature=0.25
        )

        self.structured_llm = self._llm.with_structured_output(BotOutput)

    def generate_bot_answer(self, question, isCorrect):
        prompt = f'{question=} {isCorrect=} based on the question and isCorrect create an appropriate answer'
        return self.structured_llm.invoke(prompt)