class Question(object):
    """
    Represents an SNQ question
    Contructor arguemtns:
    :param: question_ID: number id of # QUESTION:
    :param: data_string: auxillary information displayed along with question
    :param: answer_dict: dictionary of uppercase letters as keys with answer \
        choices as values
    :param: correct_answer: contains uppercase letter representing key of \
        correct_answer

    """
    def __init__(self, question_ID, data_string, question_string, \
        answer_dict, correct_answer)
        self.question_ID = question_ID
        self.data_string = data_string
        self.question_string = question_string
        self.answer_dict = answer_dict
        self.correct_answer = correct_answer


class 
