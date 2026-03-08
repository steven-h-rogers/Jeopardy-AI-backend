from flask import Flask, request, jsonify
from flask_cors import CORS
from CategoryGenerator import CategoryGenerator
from QuestionGenerator import QuestionGenerator
from AlexTrebek import AlexTrebek

category_generator = CategoryGenerator()
question_generator = QuestionGenerator()
alex_trebek = AlexTrebek()

app = Flask(__name__)
CORS(app)

@app.route('/')
def health():
    return {'status': 'ok'}

@app.route('/generate-categories', methods=['GET'])
def generate_categories():
    num_categories = request.headers.get('num-categories')
    category_list = category_generator.generate_categories(num_categories)['structured_response'].categories
    # print(category_list)
    return jsonify({'category-list': category_list})






if __name__ == "__main__":
    app.run(debug=True)