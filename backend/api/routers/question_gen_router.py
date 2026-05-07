from fastapi import APIRouter

from backend.src.QuestionGenerator import QuestionGenerator

router = APIRouter(prefix='/question-generator',
                   tags=['question-generation'])

question_generator = QuestionGenerator()

@router.get('/')
async def health():
    return{'status':'question_generator is functional'}