from pydantic import BaseModel, Field

"""Models for API validation"""
class CategoryPayload(BaseModel):
    num_categories: int = 6 # if missing -> 6, if a different int -> that int
    # use_classic_categories: bool = False

class QuestionPayload(BaseModel):
    category: str
    difficulty: str
    value: int
    round: int
    is_daily_double: bool

class FinalQuestionPayload(BaseModel):
    difficulty: str
    correct_answer: str

class JudgePayload(BaseModel):
    question: str
    provided_answer: str


"""Models for structured output with LangChain"""
class CategoryOutput(BaseModel):
    # categories: list[str]
    # ! Test whether 'Field(description...)' has any real effect on latency
    categories: list[str] = Field(description="The list of generated category names")

class QuestionOutput(BaseModel):
    question: str = Field(description="A string that consists only of a Jeopardy-style question")
    answer: str = Field(description="A string that consists only of a Jeopardy-style answer")

class JudgeOutput(BaseModel):
    verdict: bool = Field(description="A True or False verdict on whether the provided answer would be accepted in Jeopardy by Alex Trebek")
    reason: str = Field(description="A brief explanation of the factor(s) that influenced the verdict") # comment out for debug purposes


