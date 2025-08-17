from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from art import f1_car

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

print(f1_car)
print("Bem Vindo ao Quiz de Formula 1\nSua primeira pergunta é:")
while quiz.still_has_questions():
    quiz.next_question()

print("Você completou o Quiz de Formula 1")
print(f"Seu resultado foi de {quiz.score}/{quiz.question_number}")
        





