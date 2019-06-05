import filehandler
import question
import quiz
import student
import raffle


from time import sleep
from constants import *
from random import randint

def append_daily_data(snqtree_path, raffle_week_name, raffle_day_name, quiz_length = 2, random = False):
    stdtab_path = snqtree_path + "/stdtab"
    snq_dir = snqtree_path + "/questions"
    raffle_dir = snqtree_path + "/raffle"
    raffle_week_path = raffle_dir + "/" + raffle_week_name

    std_list  = filehandler.read_student_table(snqtree_path)
    question_list = filehandler.read_questions(snq_dir)

    filehandler.init_raffle_week(snqtree_path, raffle_week_name)
    for student in std_list:
        student.give_quiz(quiz.Quiz(question_list, quiz_length))
        print(student.name)
        print("-----------------------------------------------------------------")
        student.student_quiz.run_quiz(random)
        num_raffle_tickets = student.student_quiz.grade_quiz()
        filehandler.write_daily_data(snqtree_path, raffle_week_name, raffle_day_name, student)
        for i in range(num_raffle_tickets):
            filehandler.add_to_raffle(raffle_week_path, student.name)

def hold_weekly_raffle(snqtree_path, current_week_name, previous_winner_name = ""):
    stdtab_path = snqtree_path + "/stdtab"
    snq_dir = snqtree_path + "/questions"
    raffle_dir = snqtree_path + "/raffle"

    print("Determining raffle winner...")
    sleep(0.1)

    print("Parsing STDTAB...")
    sleep(0.1)
    std_list  = filehandler.read_student_table(snqtree_path)

    print("Parsing RAFFLE_BIN...")
    sleep(0.1)
    raffle_candidates_list = filehandler.read_raffle(raffle_dir + "/" + current_week_name)

    print("Purging absent students...")
    sleep(0.1)
    raffle_candidates_list = purge_absent_students(std_list, raffle_candidates_list)

    print("Purging previous winner entries...")
    sleep(0.1)
    raffle_candidates_list = purge_previous_winner(raffle_candidates_list, previous_winner_name)

    raffle_winner_name = raffle_candidates_list[randint(0, len(raffle_candidates_list) - 1)]
    cookie_choice = get_cookie_choice(raffle_winner_name, std_list)

    print("%s has won the raffle!" % (raffle_winner_name) )
    print("%s would like %s!" % (raffle_winner_name, cookie_choice))

def purge_absent_students(std_list, raffle_candidates_list):
    for student in std_list:
        if student.is_present == False:
            while student.name in raffle_candidates_list:
                raffle_candidates_list.remove(student.name)
    return raffle_candidates_list

def purge_previous_winner(std_list, name_to_purge):
    for student in std_list:
        while name_to_purge in std_list:
            std_list.remove(name_to_purge)
    return std_list

def get_cookie_choice(student_name, std_list):
    for student in std_list:
        if student.name == student_name:
            return student.favorite_cookie

#append_daily_data("/home/n01r/dev/git/snqman/snqtree", 2, "testweek2", "monday")
#hold_weekly_raffle("/home/n01r/dev/git/snqman/snqtree", "testweek1", "")
