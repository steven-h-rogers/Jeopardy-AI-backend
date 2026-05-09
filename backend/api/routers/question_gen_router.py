from fastapi import APIRouter

from backend.src.QuestionGenerator import QuestionGenerator
from backend.models.api_models import QuestionPayloadAnswers, QuestionPayload, QuestionPayloadTopics

router = APIRouter(prefix='/question-generator',
                   tags=['question-generation'])

question_generator = QuestionGenerator()

@router.get('/')
async def health():
    return{'status':'question_generator is functional'}

@router.post('/generate-question/')
async def generate_question(question_payload: QuestionPayloadAnswers):
    category = question_payload.category
    difficulty = question_payload.difficulty
    value = question_payload.value
    round = question_payload.round
    is_daily_double = question_payload.is_daily_double
    previously_asked_in_category = question_payload.previous_answers_in_category
    question_and_answer = question_generator.generate_question_direct_structured(category, difficulty, value, round, is_daily_double, previously_asked_in_category)
    return {'question': question_and_answer.question, 'answer': question_and_answer.answer}