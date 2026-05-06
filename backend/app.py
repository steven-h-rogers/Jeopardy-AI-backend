from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from backend.src.CategoryGenerator import CategoryGenerator
from backend.src.QuestionGenerator import QuestionGenerator
from backend.src.AlexTrebek import AlexTrebek
from backend.src.QuestionSummarizer import QuestionSummarizer

from backend.models import CategoryPayload

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



category_generator = CategoryGenerator()
question_generator = QuestionGenerator()
alex_trebek = AlexTrebek()
question_summarizer = QuestionSummarizer()




@app.get('/')
def health():
    return {'status': 'ok'}

# ! will need to restructure this endpoint
@app.get('/generate-categories/')
async def generate_categories(category_payload: CategoryPayload = Depends()):
    num_categories = category_payload.num_categories
    # browser will handle custom categories
    category_list = category_generator.generate_categories(num_categories)['structured_response'].categories
    # print(category_list)
    return {'category-list': category_list}
