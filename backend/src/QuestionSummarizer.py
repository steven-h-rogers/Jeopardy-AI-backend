from langchain_openai import ChatOpenAI

from backend.models.src_models import QuestionSummaryOutput, TopicOutput
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
    def summarize_question(self, question: str):
        prompt = f"{question}\nSummarize briefly."
        return self.structured_llm.invoke(prompt)
    
    @timer
    def extract_topic(self, question: str):
        prompt = f"{question}\nExtract broad topic."
        return self.structured_llm.invoke(prompt)