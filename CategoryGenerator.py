from dotenv import load_dotenv

from pydantic import BaseModel
from typing import List

from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy

load_dotenv()


class Categories(BaseModel):
    categories: List[str]


# ? implement a method to manually add categories and bypass using ai budget
class CategoryGenerator:
    def __init__(self):
        self.categories = []

        self.model = ChatOpenAI(
            model='gpt-5-mini' 
        )

        self.categoryAgent = create_agent(self.model, 
                                          system_prompt= f'You are tasked with creating jeopardy-style categories.',
                                          response_format=ToolStrategy(Categories))
    
    def generate_categories(self, num_categories):
        self.categoryAgent.invoke({'messages': [{'role': 'system', 'content': f'generate {num_categories} jeopardy-style categories' }]})

# *For Testing Purposes Only
num_categories = 6
categoryGenerator = CategoryGenerator()
response = categoryGenerator.generate_categories()
print(response)
print(response['structured_response'].categories)