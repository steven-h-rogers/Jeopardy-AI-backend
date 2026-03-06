from dotenv import load_dotenv

from langchain.agents import create_agent


# ? implement a method to manually add categories
class CategoryGenerator:
    def __init__(self, num_categories):
        self.categories = []
        self.num_categories = num_categories

        self.category_agent = create_agent(
            model = '',
            system_prompt= f'You are tasked with creating {num_categories} jeopardy style categories'
        )