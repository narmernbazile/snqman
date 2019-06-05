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

    def run_quiz(self, random_flag):
        for question in self.question_list:
            print(question)
            if random_flag:
                question_dict_keys = list(question.answer_dict.keys())
                question_answer = question_dict_keys[randint(0, len(question_dict_keys) - 1)]
                print("Enter Answer Choice: %s" %(question_answer), end="")
            else:
                question_answer = str(input("Enter Answer Choice: "))
            print()
            self.answer_list.append(question_answer)
            #print("DEBUG: " + str(self.answer_list))

    def list_answers(self):
        result = ""
        if self.answer_list:
            for (question, answer) in list(zip(self.question_list, self.answer_list)):
                result +=  "QUESTION #%s | CORRECT ANSWER : %s | STUDENT ANSWER: %s" % ( question.question_ID, question.correct_answer, answer  ) + "\n"
        return result
    def grade_quiz(self) -> int:
        """ Return integer representing number of questions correct """
        num_correct = 0
        for (question, answer) in list(zip(self.question_list, self.answer_list)):
                if answer == question.correct_answer:
                    num_correct += 1
        return num_correct
