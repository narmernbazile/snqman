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

q = question.Question(1, "q data", "answer me", a_dict, "A")


quiz = Quiz([q])

quiz.run_quiz()
quiz.list_answers()
