import question

a_dict = {
"A": "stuff",
"B": "test",
"C": "lkfgj ;klsjf",
"D": "100 pictures",
"E": "1000 words"
}

q = question.Question(1, "q data", "answer me", a_dict, "A")

#print(q.get_answer_choices())
print(q)
