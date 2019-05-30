from quiz import Quiz

class Student(object):
    """


    """

    def __init__(self, name: str, is_present: bool, favorite_cookie: str = "oreos", student_quiz: Quiz = None):
        self.name = name
        self.is_present = is_present
        self.favorite_cookie = favorite_cookie
        self.student_quiz = student_quiz

    def set_favorite_cookie(self, favorite_cookie):
        self.favorite_cookie = favorite_cookie

    def take_attendance(self, is_present: bool):
        self.is_present = is_present

    def give_quiz(self, student_quiz: Quiz):
        self.student_quiz = student_quiz
