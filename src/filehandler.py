import os
import student
import question


DELIMETER = ","
COMMENT_SYMBOL = "#"

SNQTREE_PATH = ""
RAFFLE_PATH = SNQTREE_PATH + "raffle"
QUESTIONS_PATH = SNQTREE_PATH + "questions"
STDTAB_PATH = SNQTREE_PATH + "stdtab"
RAFFLE_BIN_FILENAME = "raffle-bin"

def read_student_table(snq_tree_path: str) -> list:
    SNQTREE_PATH = snq_tree_path
    std_list = []
    os.chdir(SNQTREE_PATH)
    with open(STDTAB_PATH) as student_table:
        for entry in student_table.readlines():
            if entry == "\n" or entry == "\r":
                continue
            elif COMMENT_SYMBOL not in entry:
                std_name = entry[0 : entry.index(DELIMETER)]
                entry = entry[entry.index(DELIMETER) + 2:]
                std_present = True if entry[0: entry.index(DELIMETER)] == "True" else False
                entry = entry[entry.index(DELIMETER) + 2:]
                std_cookie = entry[0: -1]
                std_list.append(student.Student(std_name, std_present, std_cookie))
        return std_list

def write_student_table(student_table_path: str, std_name: str, std_present: bool, std_cookie: str):
    with open(student_table_path, "r") as student_table:
        #always begin on new line
        line_list = student_table.readlines()
        if line_list[len(line_list) - 1] != "\n":
            needs_newline = True
    with open(student_table_path, "a+") as student_table:
        if needs_newline:
            student_table.write("\n")
        return student_table.write("%s%s %s%s %s" % (std_name, DELIMETER, str(std_present), DELIMETER, std_cookie))

def read_questions(snq_dir_path):
    question_list = []
    directory = os.fsencode(snq_dir_path)
    os.chdir(snq_dir_path)
    current_directory = os.getcwd()

    for question_file in os.listdir(current_directory):
        with open(question_file, "r") as current_file:
            lines = current_file.readlines()
        question_ID = str(lines[0][0:-1])
        data_string = str(lines[1][0:-1])
        question_string = str(lines[2][0:-1])
        correct_answer = str(lines[3][0:-1])

        question_dict = {}
        for answer_choice_line in lines[4:]:
            key = answer_choice_line[0:1]
            value  = answer_choice_line[4:-1]
            question_dict[str(key)] = value
        question_list.append(question.Question(question_ID, data_string, question_string, question_dict, correct_answer))
    return question_list

def init_raffle_week(snqtree_path, week_name):
    """Create new folder week_name inside raffle_dir """
    os.chdir(snqtree_path)
    os.chdir(RAFFLE_PATH)
    #print(os.path.isdir(week_name))
    #print(week_name)
    if not os.path.isdir(week_name):
        os.mkdir(week_name)
        os.chdir(week_name)
        f = open(RAFFLE_BIN_FILENAME, "w+")
        f.close()

def write_daily_data(snqtree_path, week_name, day_name, student):
    os.chdir(snqtree_path)
    os.chdir(RAFFLE_PATH)
    os.chdir(week_name)
    result = ""
    result += student.name + "\n"
    result += "-----------------------------------------------------------------" + "\n"
    result += student.student_quiz.list_answers()
    result += "\n"
    with open(day_name, "a+") as daily_file:
        daily_file.write(result)

def add_to_raffle(raffle_week_dir, student_name):
    with open(RAFFLE_BIN_FILENAME, "a") as raffle_bin_file:
        raffle_bin_file.write(student_name + "\n")

def read_raffle(raffle_week_dir):
    os.chdir(raffle_week_dir)
    raffle_candidates_list = []
    with open(RAFFLE_BIN_FILENAME, "r") as raffle_bin_file:
        temp_list = raffle_bin_file.readlines()
    #strip off newline characters
    for line in temp_list:
        raffle_candidates_list.append(line[:-1])
    return raffle_candidates_list

def init_snqtree(snqtree_dir):
    if os.path.isdir(snqtree_dir):
        os.chdir(snqtree_dir)
        os.mkdir("questions")
        os.mkdir("raffle")
        with open("stdtab", "w+") as stdtab_file:
            stdtab_file.write
            (
            """# stdtab: student student_table
            #NAME, IS_PRESENT(True/False), FAVORITE COOKIES"""
            )
        return True
    else:
        return False
