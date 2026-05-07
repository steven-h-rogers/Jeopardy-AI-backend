from backend.models.src_models import JudgeOutput
from backend.src.utils import timer

from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# ? Chat Model might be too heavy for this type of task, just need a simple comparison and output.
class AlexTrebek:
    def __init__(self):

        self._llm = ChatOpenAI(
            model='gpt-5-nano',
            reasoning_effort='low'
        )

        self.structured_llm = self._llm.with_structured_output(JudgeOutput)

        # self.judge_agent = create_agent(
        #     model=self._llm,
        #     system_prompt='Act as Jeopardy host Alex Trebek. You must judge the answer to a Jeopardy-style question strictly and fairly. Actual Answer should only be used as a safeguard. if provided answer not in Jeopardy format it is FALSE',
        #     response_format=ToolStrategy(JudgeOutput)
        # )

    # @timer
    # def judge_answer_with_agent(self, question, answer, provided_answer):
    #         return self.judge_agent.invoke({'messages':[{'role':'user', 'content': f'Question: {question} Actual Answer: {answer} Provided Answer: {provided_answer} Judge whether the provided answer is acceptable'}]})
            
    @timer
    def judge_answer_direct_structured(self, question, answer, provided_answer):
            prompt = f'Question: {question} Actual Answer: {answer} Provided Answer: {provided_answer}\nJudge the provided answer as strictly and fairly as Alex Trebek would. Actual Answer should be used to make sure there is no subject ambiguity and for spelling forgiveness. if provided answer not in Jeopardy format it is FALSE'
            return self.structured_llm.invoke(prompt)