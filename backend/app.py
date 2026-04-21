from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.src.CategoryGenerator import CategoryGenerator
from backend.src.QuestionGenerator import QuestionGenerator
from backend.src.AlexTrebek import AlexTrebek

category_generator = CategoryGenerator()
question_generator = QuestionGenerator()
alex_trebek = AlexTrebek()

# CHANGE THIS TO FASTAPI
app = FastAPI()

@app.get('/')
def health():
    return {'status': 'ok'}

# ! will need to restructure this endpoint
@app.get('/generate-categories')
def generate_categories():
    num_categories = request.headers.get('num-categories')
    category_list = category_generator.generate_categories(num_categories)['structured_response'].categories
    # print(category_list)
    return jsonify({'category-list': category_list})






if __name__ == "__main__":
    app.run(debug=True)