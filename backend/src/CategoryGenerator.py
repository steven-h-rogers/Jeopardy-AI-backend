from dotenv import load_dotenv

from pydantic import BaseModel, Field
from typing import List

from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy


load_dotenv()








# ! ADD DOCSTRINGS
class CategoryResponse(BaseModel):
    categories: List[str] = Field(description="The list of generated category names")

class Categories(BaseModel):
    categories: List[str]

# ! Move away from using an agent as it is slower for this task
# ? implement a method to manually add categories and bypass using ai budget
class CategoryGenerator:
    def __init__(self):
        self.categories = []

        self._llm = ChatOpenAI(model="gpt-5-nano", temperature=0)
        self.structured_llm = self._llm.with_structured_output(CategoryResponse)


        self.model = ChatOpenAI(
            model='gpt-5-mini' 
        )

        self.categoryAgent = create_agent(self.model, 
                                          system_prompt= f'You are tasked with creating jeopardy-style categories.',
                                          response_format=ToolStrategy(Categories))
    
    def generate_categories(self, num_categories):
        # ? consider using t strings as they are better at preventing injection type attacks
        return self.categoryAgent.invoke({'messages': [{'role': 'system', 'content': f'generate {num_categories} jeopardy-style categories' }]})
    
    def generate_categories_updated(self, num_categories):
        prompt = f'Generate exactly {num_categories} unique Jeopardy-style categories that can either be original or from the show'
        return self.structured_llm.invoke(prompt)

#  *For Testing Purposes Only
num_categories = 6
categoryGenerator = CategoryGenerator()

response1 = categoryGenerator.generate_categories_updated(6)
print(response1.categories)

response2 = categoryGenerator.generate_categories(num_categories)
print(response2.categories)
