class Question(object):
    """
    Represents an SNQ question
    Contructor arguemtns:
    :param: question_ID: number id of question
    :param: data_string: auxillary information displayed along with question
    :param: answer_dict: dictionary of uppercase letters as keys with answer \
        choices as values
    :param: correct_answer: contains uppercase letter representing key of \
        correct_answer
    """
    def __init__(self, question_ID, data_string, question_string, \
        answer_dict, correct_answer):
        self.question_ID = question_ID
        self.data_string = data_string
        self.question_string = question_string
        self.answer_dict = answer_dict
        self.correct_answer = correct_answer

    def __repr__(self):
        result = ""
        result += "Question #%s\n" % (str(self.question_ID))
        result += self.data_string + "\n"
        result += self.question_string + "\n"
        result += self.get_answer_choices()
        return result

    def print_answer_choices(self):
        for key in self.answer_dict:
            print("%s: %s" % (key, self.answer_dict[key]))

    def get_answer_choices(self):
        result = ""
        for key in self.answer_dict:
            result += "%s: %s\n" % (key, self.answer_dict[key])
        return result
