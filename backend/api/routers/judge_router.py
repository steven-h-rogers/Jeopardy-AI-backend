from fastapi import APIRouter

from backend.src.AlexTrebek import AlexTrebek

router = APIRouter(prefix='/judge',
                   tags=['judge'])

judge = AlexTrebek()

@router.get('/')
async def health():
    return{'status':'judge is functional'}