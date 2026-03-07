import CategoryGenerator
import QuestionGenerator

class Game:

    def __init__(self, num_categories):

        self.num_categories = num_categories
        self.category_generator = CategoryGenerator()
        self.question_generator = QuestionGenerator()