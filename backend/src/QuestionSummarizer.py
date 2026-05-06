from langchain_openai import ChatOpenAI

from backend.models import QuestionSummaryOutput
from backend.src.utils import timer


class QuestionSummarizer():
    def __init__(self):
        self._llm = ChatOpenAI(
            model='gpt-5-nano',
            reasoning_effort='low',
            temperature=0.25
        )

        self.structured_llm = self._llm.with_structured_output(QuestionSummaryOutput)

    @timer
    def summarize_question(self, question: str) -> QuestionSummaryOutput:
        prompt = f'Question: {question}\nGiven the question simply summarize the essence of it using as few words as possible and do nothing else'
        return self.structured_llm.invoke(prompt)
    
    @timer
    def extract_topic(self, question: str) -> 