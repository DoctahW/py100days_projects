class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number+1}: {current_question.text} (True/False): ")
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)
    
    def check_answer(self,u_answer,cur_question):
        if u_answer.lower() == cur_question.lower():
            self.score +=1
            print("Correto")
        else:
            print("ERRADO!!!")
            print(f"A resposta correta era: {cur_question}")
        print(f"Sua pontuação é de: {self.score}/{self.question_number}")
        print("\n")