# driver.py: a dummy tester file for snqman project


import question
from quiz import Quiz

a_dict = {
"A": "stuff",
"B": "test",
"C": "lkfgj ;klsjf",
"D": "100 pictures",
"E": "1000 words"
}

print(a_dict["D"])

q = [ question.Question(1, "q data", "answer me", a_dict, "A"), question.Question(2, "trdewfsfsff", "answer me", a_dict, "B") ]


quiz = Quiz(q, 2)

quiz.run_quiz()
quiz.list_answers()
