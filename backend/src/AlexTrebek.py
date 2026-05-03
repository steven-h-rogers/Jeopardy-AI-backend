from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# ! ADD DOCSTRINGS 
# ! FLESH THIS OUT
# ? Chat Model might be too heavy for this type of task, just need a simple comparison and output.
class AlexTrebek:
    def __init__(self):

        self.model = create_agent(
            model='gpt-5-mini',
            system_prompt='You are Jeopardy host Alex Trebek and you must judge answers to Jeopardy-style questions as strictly and fairly as Alex Trebek would.',
        )

        self._llm = ChatOpenAI(
            model='gpt-5-mini',
            reasoning_effort='low'
        )

        self.structured_llm = self._llm.with_structured_output()
