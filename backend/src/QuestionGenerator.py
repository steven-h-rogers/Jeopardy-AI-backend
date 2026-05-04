from dotenv import load_dotenv
from backend.models import QuestionOutput
from backend.src.utils import timer

from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from langchain_openai import ChatOpenAI

load_dotenv()

class QuestionGenerator:

    def __init__(self):
        self._llm = ChatOpenAI(model="gpt-5-mini", temperature=0.25, reasoning_effort='low')
        self.structured_llm = self._llm.with_structured_output(QuestionOutput)

        self.question_agent = create_agent(
            model=self._llm,
            system_prompt=f"You must create Jeopardy-style questions that are appropriate for the given information",
            response_format=ToolStrategy(QuestionOutput)
        )
    
    @timer
    def generate_question_with_agent(self, category, difficulty, value, round=1, is_daily_double=False, previously_asked_in_category=None):
        # print(f'Category: {category} Game Difficulty: {difficulty} Value: {value} Round: {round} Daily Double: {is_daily_double} Previously Asked Questions {previously_asked_in_category}')
        return self.question_agent.invoke({'messages': 
                                           [{'role': 'user',
                                            'content': f'Category: {category} Game Difficulty: {difficulty} Value: {value} Round: {round} Daily Double: {is_daily_double} Previously Asked Questions {previously_asked_in_category}\n Based on this information, generate an appropriate Jeopardy-style question (that can be answered solely based on the text of the question) with an expected answer. DO NOT ask questions that are too similar in nature to those previously asked (judge this on whether the show would allow it or not).'}]})
    
    @timer
    def generate_question_direct_structured(self, category, difficulty, value, round=1, is_daily_double=False, previously_asked_in_category=None):
        # print(f'Category: {category} Game Difficulty: {difficulty} Value: {value} Round: {round} Daily Double: {is_daily_double} Previously Asked Questions {previously_asked_in_category}')
        prompt = f'Category: {category} Game Difficulty: {difficulty} Value: {value} Round: {round} Daily Double: {is_daily_double} Previously Asked Questions {previously_asked_in_category}\n Based on this information, generate an appropriate Jeopardy-style question (that can be answered solely based on the text of the question) with an expected answer. Do not ask questions that are too similar in nature to questions already asked (judge this on whether the show would allow it or not).'
        return self.structured_llm.invoke(prompt)

        
    