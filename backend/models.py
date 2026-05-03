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
    correct_answer: str

class FinalQuestionPayload(BaseModel):
    difficulty: str
    correct_answer: str


"""Models for structured output with LangChain"""
class CategoryOutput(BaseModel):
    # categories: list[str]
    # ! Test whether 'Field(description...)' has any real effect on latency
    categories: list[str] = Field(description="The list of generated category names")

class QuestionOutput(BaseModel):
    question: str
    answer: str



