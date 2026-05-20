class QuizBrain:
    
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    # def check_answer(self, user_answer, correct_answer):
    #     if user_answer == correct_answer.lower():
    #         self.score += 1
    #         print("You got it!")
    #     else:
    #         print("That's wrong.")
    #     print(f"The correct answer was: {correct_answer}.")
    #     print(f"Your current score is: {self.score}/{self.question_number}")

    def next_question(self):
       index = self.question_number
       self.question_number += 1
       user_response = input(f"Q.{str(index)}: {self.question_list[index].text} (True/False)?: ").lower()
       self.check_answer(user_response, self.question_list[index].answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score += 1
            print("You got it!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
        
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    