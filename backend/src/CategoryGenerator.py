from backend.src.utils import timer

from dotenv import load_dotenv
from backend.models import CategoryOutput

from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy


load_dotenv()


# ! Move away from using an agent as it is slower for this task
# ? implement a method to manually add categories and bypass using ai budget
class CategoryGenerator:
    def __init__(self):
        self.categories = []

        self._llm = ChatOpenAI(model="gpt-5-mini", temperature=0, reasoning_effort='low')
        self.structured_llm = self._llm.with_structured_output(CategoryOutput)


        self.model = ChatOpenAI(
            model='gpt-5-mini',
            reasoning_effort='low'
        )

        self.categoryAgent = create_agent(self.model, 
                                          system_prompt= f'You are tasked with creating jeopardy-style categories.',
                                          response_format=ToolStrategy(CategoryOutput))
    @timer
    def generate_categories(self, num_categories):
        # ? consider using prompt templates as they are better at preventing injection type attacks
        return self.categoryAgent.invoke({'messages': [{'role': 'user', 'content': f'generate {num_categories} jeopardy-style categories' }]})
    
    @timer
    def generate_categories_updated(self, num_categories):
        prompt = f"Generate {num_categories} Jeopardy-style categories (that don't require anything but text) that can either be original or from the show"
        return self.structured_llm.invoke(prompt)
    
    @timer
    def generate_categories_updated_optimized(self, num_categories):
        prompt = f"Generate {num_categories} Jeopardy-style categories (that don't require anything but text) that can either be original or from the show as a comma separated list"
        response = self._llm.invoke(prompt)
        categories = [c.strip() for c in response.content.split(',')]
        return categories
