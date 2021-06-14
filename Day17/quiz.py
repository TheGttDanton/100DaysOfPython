from quiz_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    text = question['text']
    answer = question['answer']
    ques_obj = Question(text, answer)
    question_bank.append(ques_obj)

print(question_bank[0].text)

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_question():
    quiz_brain.next_question()
