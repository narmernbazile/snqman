from random import randInt

class Quiz:
    """

    """
    def __init__(self, question_list, quiz_length=1):
        self.question_list = []
        # add quiz_length number of randomly selected questions to self.question_list
        for i in range(quiz_length):
            self.question_list.append( question_list[ randInt(0, len(question_list)) ] )
        self.quiz_length = quiz_length
