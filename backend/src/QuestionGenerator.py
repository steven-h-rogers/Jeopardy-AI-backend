from dotenv import load_dotenv
from backend.models import QuestionOutput

from pydantic import BaseModel
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from langchain_openai import ChatOpenAI

load_dotenv()

class QuestionGenerator:

    def __init__(self):
        self.question_history = []


        self._llm = ChatOpenAI(model="gpt-5-mini", temperature=0, reasoning_effort='low')
        self.structured_llm = self._llm.with_structured_output()


        self.model = ChatOpenAI(
            model='gpt-5-mini' 
        )

        self.question_agent = create_agent(
            model=self.model,
            system_prompt=f"You are tasked with creating Jeopardy-style questions and answers. DO NOT repeat/ask questions that would be considered too similar to previously asked ones for the actual show. Responses should be given purely as QUESTION and ANSWER with no filler or redundancy",
            response_format=ToolStrategy(QuestionOutput)
        )
    
    def generate_question(self, category, num_points, isDailyDouble=False):
        return self.question_agent.invoke({'messages': 
                                           [{'role': 'user',
                                            'content': f'Generate a jeopardy-style question that is appropriate for the category: {category}, number of points: {num_points} and whether or not it is a daily double: {isDailyDouble}.'}]})

# # * For Testing Purposes Only
# //questionGenerator = QuestionGenerator()
# //response = questionGenerator.generate_question('Historical Monuments', 1000, False)
# //print(response['structured_response'].question, response['structured_response'].answer, sep='\n')
        
    