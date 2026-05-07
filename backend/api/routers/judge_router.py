from fastapi import APIRouter

from backend.src.AlexTrebek import AlexTrebek
from backend.models.api_models import JudgePayload

router = APIRouter(prefix='/judge',
                   tags=['judge'])

judge = AlexTrebek()

@router.get('/')
async def health():
    return{'status':'judge is functional'}

@router.post('/judge-answer/')
async def judge_answer(judge_payload: JudgePayload):
    question = judge_payload.question
    answer = judge_payload.answer
    provided_answer = judge_payload.provided_answer
    verdict = judge.judge_answer_direct_structured(question, answer, provided_answer)
    return {'verdict': verdict}
