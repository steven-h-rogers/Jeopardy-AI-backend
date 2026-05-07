from fastapi import APIRouter

from backend.src.QuestionSummarizer import QuestionSummarizer

router = APIRouter(prefix='/summarizer',
                   tags=['summarizer'])

question_summarizer = QuestionSummarizer()


@router.get('/')
async def health():
    return{'status':'summarizer is functional'}