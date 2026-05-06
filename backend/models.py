from pydantic import BaseModel, Field

"""Models for API validation"""
class CategoryPayload(BaseModel):
    num_categories: int = Field(description="The number of categories that are to be generated", default=6) # if missing -> 6, if a different int -> that int
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

class QuestionPayloadAnswers(BaseModel):
    category: str
    difficulty: str
    value: int
    round: int
    is_daily_double: bool
    # this may cause significant latency as the number of tokens per question will go up dramatically
    # ? consider making this something like 'previous_answers' if latency is too noticeable
    previous_answers_in_category: list[str] | None = Field(description='Previously asked questions in this category')

class QuestionPayloadSummary(BaseModel):
    category: str
    difficulty: str
    value: int
    round: int
    is_daily_double: bool
    # this may cause significant latency as the number of tokens per question will go up dramatically
    # ? consider making this something like 'previous_answers' if latency is too noticeable
    previous_questions_summarized: list[str] | None = Field(description='Summaries of previous questions in this category')


class FinalQuestionPayload(BaseModel):
    difficulty: str
    correct_answer: str

class JudgePayload(BaseModel):
    question: str = Field(description="The question that the user answered")
    provided_answer: str = Field(description="The answer that the user provided")


"""Models for structured output with LangChain"""
class CategoryOutput(BaseModel):
    categories: list[str] = Field(description="The list of generated category names")

class QuestionOutput(BaseModel):
    question: str = Field(description="A string that only consists of a Jeopardy-style question (that is not similar to any previously asked)")
    answer: str = Field(description="A string that only consists of a Jeopardy-style answer")

class JudgeOutput(BaseModel):
    verdict: bool = Field(description="A True or False verdict on whether the provided answer would be accepted in Jeopardy by Alex, including the format it was provided in")
    reason: str = Field(description="A brief explanation of the factor(s) that influenced the verdict") # comment out for debug purposes

class QuestionSummaryOutput(BaseModel):
    summary: str = Field(description="The most concise summary of the provided question in under 10 words")

class TopicOutput(BaseModel):
    topic: str = Field(description="The topic that this question covered in the fewest words")


