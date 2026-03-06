from dotenv import load_dotenv

from langchain.agents import create_agent

class QuestionGenerator:

    def __init__(self, num_points, category):
        self.num_points = num_points
        self.category = category

        
        self.question_agent = create_agent(
            model='',
            system_prompt=f"You are tasked with creating a jeopardy style question that fits the category: {self.category} and is appropriate difficulty for the amount of points: {self.num_points}"
        )
        self.question_history = []
        