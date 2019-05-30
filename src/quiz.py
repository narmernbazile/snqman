from random import randint


class Quiz(object):
    """
    #TODO: docstring goes here
    """
    def __init__(self, question_list: list, quiz_length: int = 1):
        self.question_list = []
        self.answer_list = []
        # add quiz_length number of randomly selected questions to self.question_list
        for i in range(quiz_length):
            self.question_list.append( question_list[ randint(0, len(question_list) - 1) ] )
        self.quiz_length = quiz_length

    def run_quiz(self):
        for question in self.question_list:
            print(question)
            question_answer  = str(input("Enter Answer Choice: "))
            self.answer_list.append(question_answer)

    def list_answers(self):
        if self.answer_list:
            for (question, answer) in list(zip(self.question_list, self.answer_list)):
                print("QUESTION #%s | CORRECT ANSWER : %s | STUDENT ANSWER: %s" % ( question.question_ID, question.correct_answer, answer  )  )
    #def
