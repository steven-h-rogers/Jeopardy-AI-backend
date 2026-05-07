from pydantic import BaseModel, Field

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

