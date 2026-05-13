from pydantic import BaseModel, Field


"""Models for API validation"""
class CategoryPayload(BaseModel):
    num_categories: int = Field(description="The number of categories that are to be generated", default=6, gt=0, le=8) # if missing -> 6, if a different int -> that int
    # use_classic_categories: bool = False

class QuestionPayload(BaseModel):
    category: str = Field(description="The category that the generated question is a part of")
    difficulty: str = Field(description="The level of difficulty that the generated question should be")
    value: int = Field(description="How many points the generated question is worth")
    round: int = Field(description="What round of the game this question is generated for")
    is_daily_double: bool = Field(description="Whether or not this question is a daily double")
    # this may cause significant latency as the number of tokens per question will go up dramatically
    # ? consider making this something like 'previous_answers' if latency is too noticeable
    previously_asked_in_category: list[str] | None = Field(description='Previously asked questions in this category')

class QuestionAnswerPayload(BaseModel):
    category: str = Field(description="The category that the generated question is a part of")
    difficulty: str = Field(description="The level of difficulty that the generated question should be")
    value: int = Field(description="How many points the generated question is worth")
    round: int = Field(description="What round of the game this question is generated for")
    is_daily_double: bool = Field(description="Whether or not this question is a daily double")
    # this may cause significant latency as the number of tokens per question will go up dramatically
    # ? consider making this something like 'previous_answers' if latency is too noticeable
    previous_answers_in_category: list[str] | None = Field(description='Previously asked questions in this category')

class QuestionSummaryPayload(BaseModel):
    question: str = Field(description='The question that is to be summarized')

class QuestionTopicPayload(BaseModel):
    question: str = Field(description='The question thats topic is to be extracted')

class FinalQuestionPayload(BaseModel):
    difficulty: str
    correct_answer: str

class JudgePayload(BaseModel):
    question: str = Field(description="The question that the user answered")
    answer: str = Field(description="The actual answer to the question (format doesn't matter)")
    provided_answer: str = Field(description="The answer that the user provided")

class BotPayload(BaseModel):
    question: str = Field(description="A Jeopardy-style question")
    isCorrect: bool = Field(description="True/False representation of whether the answer should be correct")

