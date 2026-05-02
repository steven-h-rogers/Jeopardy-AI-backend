from pydantic import BaseModel

class CategoryPayload(BaseModel):
    num_categories: int = 6 # if missing -> 6, if a different int -> that int
    # use_classic_categories: bool = False
    
class QuestionPayload(BaseModel):
    category: str
    difficulty: str
    value: int
    round: int
    is_double_jeopardy: bool
    correct_answer: str

class FinalQuestionPayload(BaseModel):
    difficulty: str
    correct_answer: str

