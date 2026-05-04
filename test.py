from backend.src.CategoryGenerator import CategoryGenerator
from backend.src.QuestionGenerator import QuestionGenerator
from backend.src.AlexTrebek import AlexTrebek

# * TESTING CATEGORY GENERATOR
num_categories = 6
categoryGenerator = CategoryGenerator()

response1 = categoryGenerator.generate_categories_direct(num_categories)
print(response1)

response2 = categoryGenerator.generate_categories_with_agent(num_categories)
print(response2['structured_response'].categories)

response3 = categoryGenerator.generate_categories_direct_structured(num_categories)
print(response3)

# * TESTING QUESTION GENERATOR
questionGenerator = QuestionGenerator()
question_payload = ['Historical Monuments', 'medium', 1000, 1]

response4 = questionGenerator.generate_question_with_agent(*question_payload)
print(response4['structured_response'].question, response4['structured_response'].answer, sep='\n')

response5 = questionGenerator.generate_question_direct_structured(*question_payload)
print(response5)

# * TESTING JUDGEMENT
judge = AlexTrebek()

judgement_payload_correct = ["This Chilean city whose name means ""valley of paradise"" lies on a wide inlet of the Pacific", "Valparaiso", "What is Valparaiso"]
judgement_payload_incorrect = ["This Chilean city whose name means ""valley of paradise"" lies on a wide inlet of the Pacific", "Valparaiso", "What is Patagonia"]
judgement_payload_correct_improperly_formatted =  ["This Chilean city whose name means ""valley of paradise"" lies on a wide inlet of the Pacific", "Valparaiso", "Valparaiso"]

response6 = judge.judge_answer_with_agent(*judgement_payload_correct)
print(f'correct {response6['structured_response'].verdict}\n reason {response6['structured_response'].reason}\n')

response7 = judge.judge_answer_with_agent(*judgement_payload_incorrect)
print(f'incorrect {response7['structured_response'].verdict}\n reason {response7['structured_response'].reason}\n')

response8 = judge.judge_answer_with_agent(*judgement_payload_correct_improperly_formatted)
print(f'correct improper format {response8['structured_response'].verdict}\n reason {response8['structured_response'].reason}')

response9 = judge.judge_answer_direct_structured(*judgement_payload_correct)
print(f'correct {response9.verdict}\n reason{response9.reason}\n')

response10 = judge.judge_answer_direct_structured(*judgement_payload_incorrect)
print(f'incorrect {response10.verdict}\n reason{response10.reason}\n')

response11 = judge.judge_answer_direct_structured(*judgement_payload_correct_improperly_formatted)
print(f'correct improper format {response11.verdict}\n reason{response11.reason}\n')
