from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.routers.category_gen_router import router as category_gen_router
from backend.api.routers.question_gen_router import router as question_gen_router
from backend.api.routers.judge_router import router as judge_router
from backend.api.routers.summarizer_router import router as summarizer_router


app = FastAPI()

# allowed origins through CORS
origins = [None]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=["*"]
)

app.include_router(category_gen_router)
app.include_router(question_gen_router)
app.include_router(judge_router)
app.include_router(summarizer_router)


@app.get('/')
def health():
    return {'status': 'ok'}


