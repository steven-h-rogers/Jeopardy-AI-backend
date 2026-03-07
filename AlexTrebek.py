from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()

class AlexTrebek:
    def __init__(self):
        create_agent(
            model='',
            system_prompt='You are Jeopardy host Alex Trebek and you must judge answers to Jeopardy-style questions as strictly and fairly as Alex Trebek would.',
            api_key=OPENAI_KEY
        )
