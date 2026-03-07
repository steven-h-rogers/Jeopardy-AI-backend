from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()

# ! ADD DOCSTRINGS 
# ! FLESH THIS OUT
# ? Chat Model might be too heavy for this type of task, just need a simple comparison and output.
class AlexTrebek:
    def __init__(self):
        create_agent(
            model='',
            system_prompt='You are Jeopardy host Alex Trebek and you must judge answers to Jeopardy-style questions as strictly and fairly as Alex Trebek would.',
            api_key=OPENAI_KEY
        )
