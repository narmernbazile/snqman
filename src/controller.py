import filehandler
import question
import quiz
import student
import raffle

from constants import *

def append_daily_data(snqtree_path, quiz_length, raffle_week_name, raffle_day_name):
    stdtab_path = snqtree_path + "/stdtab"
    snq_dir = snqtree_path + "/questions"
    raffle_dir = snqtree_path + "/raffle"
    raffle_week_path = raffle_dir + "/" + raffle_week_name

    std_list  = filehandler.read_student_table(snqtree_path)
    question_list = filehandler.read_questions(snq_dir)
    daily_quiz = quiz.Quiz(question_list, quiz_length)

    filehandler.init_raffle_week(snqtree_path, raffle_week_name)
    for student in std_list:
        student.give_quiz(daily_quiz)
        print(student.name)
        print("-----------------------------------------------------------------")
        student.student_quiz.run_quiz()
        num_raffle_tickets = student.student_quiz.grade_quiz()
        filehandler.write_daily_data(snqtree_path, raffle_week_name, raffle_day_name, student)
        for i in range(num_raffle_tickets):
            filehandler.add_to_raffle(raffle_week_path, student.name)

def hold_weekly_raffle(snqtree_path, current_week_name, previous_week_name):
    stdtab_path = snqtree_path + "/stdtab"
    snq_dir = snqtree_path + "/questions"
    raffle_dir = snqtree_path + "/raffle"

    std_list  = filehandler.read_student_table(snqtree_path)
    raffle_candidates_list = filehandler.read_raffle(raffle_dir + "/" + current_week_name)
    raffle_candidates_list = purge_absent_students(std_list, raffle_candidates_list)
    print(raffle_candidates_list)

def purge_absent_students(std_list, raffle_candidates_list):
    for student in std_list:
        if student.is_present == False:
            while student.name in raffle_candidates_list:
                raffle_candidates_list.remove(student.name)
    return raffle_candidates_list

hold_weekly_raffle("/home/n01r/dev/git/snqman/snqtree", "testweek1", "")
#append_daily_data("/home/n01r/dev/git/snqman/snqtree", 2, "testweek1", "monday")
