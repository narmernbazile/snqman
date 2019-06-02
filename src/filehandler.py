import os
import student
import question

DELIMETER = ","
COMMENT_SYMBOL = "#"

def read_student_table(student_table_path: str) -> list:
    std_list = []
    with open(student_table_path) as student_table:
        for entry in student_table.readlines():
            #entry = "".join(list(filter(lambda char: char not in "\n", entry)))
            if entry == "\n" or entry == "\r":
                continue
            elif COMMENT_SYMBOL not in entry:
                #print(entry, end='')
                #print(entry.index(DELIMETER))

                std_name = entry[0 : entry.index(DELIMETER)]
                entry = entry[entry.index(DELIMETER) + 2:]
                std_present = True if entry[0: entry.index(DELIMETER)] == "True" else False
                entry = entry[entry.index(DELIMETER) + 2:]
                std_cookie = entry[0:]
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

def init_raffle_week(raffle_dir, week_name):
    RAFFLE_BIN_FILENAME = "raffle-bin"
    os.chdir(raffle_dir)
    os.mkdir(weekname)
    os.chdir(raffle_dir)
    f = open(RAFFLE_BIN_FILENAME, "w+")
    f.close()

def write_daily_data(raffle_week_dir, day_name, data_string):
    os.chdir(raffle_week_dir)
    with open(day_name, "w+") as daily_file:

def init_snqtree(snqtree_dir):
if not os.listdir(os.getcwd()) and os.path.is_dir(snqtree_dir):
        os.chdir(snqtree)
        os.mkdir("snq")
        with open("stdtab", "w+") as stdtab_file:
            stdtab_file.write
            (
            """# stdtab: student student_table
            #NAME, IS_PRESENT(True/False), FAVORITE COOKIES"""
            )
        return True
    return False
